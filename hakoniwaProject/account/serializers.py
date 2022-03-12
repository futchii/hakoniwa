from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        #fields = ('name','id')
        fields = '__all__'

class AccountCreateSerializer(serializers.ModelSerializer):

    def validate_password(self, value: str) -> str:
        return make_password(value)

    class Meta:
        model = Account
        fields = ('name','password')
        extra_kwargs = {'password': {'write_only': True}}