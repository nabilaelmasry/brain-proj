from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

    def save(self):
        password = self.validated_data['password']

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': "Email is found"})

        account = User(username=self.validated_data['username'],
                       email=self.validated_data['email'])

        account.set_password(password)
        account.save()

        return account