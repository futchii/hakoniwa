from django.contrib import admin
from .models import Account,AccountToken

admin.site.register(Account)
admin.site.register(AccountToken)