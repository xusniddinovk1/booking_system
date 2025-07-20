from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema


class LoginView(APIView):
    @extend_schema(
        request=LoginSerializer,
        responses={
            200: {
                'type': 'object',
                'properties': {
                    'refresh': {'type': 'string'},
                    'access': {'type': 'string'},
                }
            },
            400: {'type': 'object'},  # yoki error serializer qo‘shsa ham bo‘ladi
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            return Response({
                'Refresh': str(refresh),
                'Access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
