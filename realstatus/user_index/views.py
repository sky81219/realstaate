from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from api.serializers import UserTokenObtainPairSerializer as ULS
from api.serializers import UserCreateSerializer as UCS
from totalprice.models import BasicUserInformation as BI 


@api_view(["POST"])
@permission_classes([AllowAny]) # 인증이 필요한 API 아님 
def create_user_view(request):
    if request.method == "POST":
        serializer = UCS(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"messase": "Request Body error"}, status=status.HTTP_409_CONFLICT)
        
        if BI.objects.filter(email=serializer.validated_data["email"]).first() is None:
            serializer.save()
            return Response({"messase": "ok"}, status=status.HTTP_201_CREATED)

        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_user_view(request):
    if request.method == "POST":
        serializer = ULS(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"messase": "Request Body error"}, status=status.HTTP_409_CONFLICT)

        if serializer.validated_data["email"] is None:
            return Response({"messase": "fail"}, status=status.HTTP_200_OK)
        
        response = {
            "success": True,
            "token": serializer.data["token"]
        }
        
        return Response(response, status=status.HTTP_200_OK)