from rest_framework import serializers



class BvnVerificationSerializer(serializers.Serializer):
    user_email = serializers.EmailField(required=True)
    selfie_image = serializers.CharField(required=True)
    bvn = serializers.CharField(required=True)