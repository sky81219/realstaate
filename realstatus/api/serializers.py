from typing import Dict
from totalprice.models import BasicUserInformation as BI 

from rest_framework import serializers
from rest_framework import permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate


# user create 
class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)
    name = serializers.CharField(max_length=10)
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = BI.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )
        user.save()
        
        return user
    
    class Meta:
        model = BI
        fields = "__all__"



# JWT CUSTOM OR LOGIN
class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages: Dict = {
        "no_active_account": {
            "message": "이메일이나 비밀번호 확인해주세요",
            "success": False,
            "status": 401
        }
    }
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        refresh = self.get_token(self.user)
        data["email"] = self.user
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["success"] = True
        
        return data


class UserLoginObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny)
    serializer_class = UserTokenObtainPairSerializer