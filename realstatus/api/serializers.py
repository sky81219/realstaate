from rest_framework import serializers
from totalprice.models import BasicUserInformation as BI


class UserSignupSerializerJWT(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=10, required=True,
        write_only=True
    )
    email = serializers.CharField(
        max_length=50, required=True,
        write_only=True
    )
    password = serializers.CharField(
        required=True, required=True,
        write_only=True, style={"input_type": "password"}
    )
    
    class Meta:
        model = BI
        fields = ("email", "name", "password")
    
    def save(self, request):
        user = super().save()
        
        user.email = self.validated_data['email']
        user.name = self.validated_data['name']
        
        user.set_password(self.validated_data["password"])
        user.save()
    
    def validate(self, data):
        email = data.get("email", None)
        
        if BI.objects.filter(email=email).exists():
            raise serializers.ValidationError("이미 있는 이메일 입니다")
        
        return data