from .models import Account,AccountToken
from rest_framework import authentication,exceptions,status

class AccountAuthentication(authentication.BaseAuthentication):
    def authenticate(self,request):
        token_str = request.META.get('HTTP_X_AUTH_TOKEN')
        if not token_str:
            raise exceptions.AuthenticationFailed({'message': 'token injustice.'})

        token = AccountToken.get(token_str)
        if token == None:
            raise exceptions.AuthenticationFailed({'message': 'Token not found.'})

        if not token.check_valid_token():
            raise exceptions.AuthenticationFailed({'message': 'Token expired.'})

        token.update_datetime()

        return (token.account, None)