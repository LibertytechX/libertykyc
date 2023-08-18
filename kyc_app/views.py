from django.conf import settings

from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from kyc_app.serializers import BvnVerificationSerializer
from kyc_app.helpers.dojah_manager import DojahVerifications
from kyc_app.models import DojahVerificationRecord

import requests, json




class DojahBvNverificationView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = BvnVerificationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            selfie_image = serializer.validated_data.get("selfie_image")
            bvn = serializer.validated_data.get("bvn")
            user_email = serializer.validated_data.get("user_email")


            dojah_verf_resp = DojahVerifications.verify_bvn_selfie_image_with_dojah(
                selfie_image, 
                bvn, 
                user = None
            )


            verification_status = DojahVerificationRecord.check_verification_status(
                confidence_value=dojah_verf_resp["entity"]["selfie_verification"]["confidence_value"],
                match=dojah_verf_resp["entity"]["selfie_verification"]["match"]=="true"
            )
            
            # process and store image
            existing_verf = DojahVerificationRecord.create_verification_record(
                            user_email = user_email, 
                            bvn = bvn, 
                            selfie_image = selfie_image, 
                            payload = dojah_verf_resp, 
                            verification_type = "BVN_SELFIE_VERIFICATION", 
                            is_verified = True if verification_status is True else False
                            )

            # Process outgoing data
            dojah_outgoing = dojah_verf_resp.copy()
            del dojah_outgoing["entity"]["image"]
            dojah_outgoing["entity"]["user_email"] = user_email

            out_going_data = {
                "eventName": "verification_completed || verification_updated",
                "metdata": {"user_email":"", "user_type":""},
                "resource": dojah_outgoing["entity"],
                "status": verification_status
            }

            call_back_url = settings.AGENCY_BANKING_DOJAH_BVN_VERF_CALLBACK_URL
            headers = {
                "content-type": "application/json"
            }
            
            payload = json.dumps(out_going_data)
            response = requests.request("POST", call_back_url, headers=headers, data=payload)
            return Response({"message": dojah_verf_resp}, status=status.HTTP_200_OK)