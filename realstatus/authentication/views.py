from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers import UserSignupSerializerJWT


class SignupView(APIView):
    serializer_class = UserSignupSerializerJWT
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=False):
            user = serializer.save(request)
            
            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)
            
            data = {
                "user": user,
                "access": access,
                "refresh": refresh
            }
            
            return JsonResponse(data)