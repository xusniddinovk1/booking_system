from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import RegisterSerializer
from rest_framework import status


class RegisterView(APIView):
    @extend_schema(
        request=RegisterSerializer,
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
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            return Response({
                'Refresh': str(refresh_token),
                'Access': str(access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
