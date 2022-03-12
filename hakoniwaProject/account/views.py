import json
from rest_framework import generics
from rest_framework.views import APIView
from django.http.response import JsonResponse 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import update_last_login
from .models import Account,AccountToken
from .serializers import AccountSerializer,AccountCreateSerializer

class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format=None):
        try:
            data = json.loads(request.body)
            name = data['name']
            password = data['password']
        except:
            return JsonResponse({'message': 'Post data injustice'}, status=400)

        if not Account.objects.filter(name=name).exists():
            return JsonResponse({'message': 'Login failure.'}, status=403)

        user = Account.objects.get(name=name)
        update_last_login(None, user)

        if not user.check_password(password):
            return JsonResponse({'message': 'Login failure.'}, status=403)

        token = AccountToken.create(user)

        return JsonResponse({'token': token.token})

class YesView(APIView):
    def post(self,request,format=None):
        return JsonResponse({'message':'Yes','name':request.user.name})

class AccountCreateView(generics.CreateAPIView):#post
    authentication_classes = ()
    permission_classes = ()

    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer

class AccountReadView(APIView):
    def get(self,request):
        return JsonResponse({'name':request.user.name})

class AccountListView(generics.ListAPIView):#get
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountUpdateView(APIView):

    def patch(self,request):
        newdata = json.loads(request.body)
        olddata = Account.objects.get(id=request.user.id)
        try:
            if newdata['name']:
                olddata.name = newdata['name']
            
            if newdata['password']:
                olddata.password = make_password(newdata['password'])
            
            olddata.save()

            return JsonResponse({'message':'update success.'})
        except:
            return JsonResponse({'message':'update failure.'})
        

class AccountDeleteView(APIView):
    def delete(self,request):
        Account.objects.filter(id=request.user.id).delete()
        return JsonResponse({'message':'delete OK!'})