from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError


class UserRecords(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()

            print(request.data)
            print(serializer.data['username'])
            print(serializer.data['email'])

            data['response'] = "Successful Registration!"
            data['username'] = serializer.data['username']
            data['email'] = serializer.data['email']

            Token.objects.get_or_create(user=account)
            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            print('Error')
            data = serializer.errors

        return Response(data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ResetPassword(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        try:
            account = User.objects.get(email=email)
            account.set_password(password)
            account.save()
            return Response({"data": "Password successfully changed"}, status=status.HTTP_200_OK)
        except:
            raise ValidationError({"error": "Email doesn't exist"})
