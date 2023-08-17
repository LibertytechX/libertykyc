from django.db import models

# Create your models here.


class DojahVerificationRecord(models.Model):
    BVN_SELFIE_VERIFICATION = "BVN_SELFIE_VERIFICATION"

    VERFICATION_TYPES = (
        (BVN_SELFIE_VERIFICATION, BVN_SELFIE_VERIFICATION),
    )
    
    user_email = models.EmailField()
    selfie_image = models.TextField(blank=True, null=True)
    bvn = models.CharField(max_length=11, blank=True, null=True)
    payload = models.TextField(blank=True, null=True)
    verification_type = models.CharField(max_length=200, choices=VERFICATION_TYPES)
    is_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    @classmethod
    def create_verification_record(cls, user_email, bvn, selfie_image, payload, verification_type, is_verified):
        """
        Creates unique records of verifications. 
        New record is not created for an existing 
        successful verification.
        """

        existing_record = cls.objects.filter(
            user_email = user_email,
            bvn = bvn,
            verification_type = verification_type,
            is_verified = True
        )

        if existing_record.exists():
            return existing_record
        else:
            new_record = cls.objects.create(
                user_email = user_email,
                selfie_image = selfie_image,
                bvn = bvn,
                payload = payload,
                verification_type = verification_type,
                is_verified = is_verified
            )
            return new_record
        
    @staticmethod
    def check_verification_status(confidence_value, match):
        if confidence_value >= 70 and match == "true":
            return "verified"
        else:
            "not verified"