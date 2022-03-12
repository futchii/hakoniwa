from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
import hashlib
from datetime import timedelta

class AccountManager(BaseUserManager):

    def create_user(self,name,password=None):
        if not name:
            raise ValueError('Users must have an username')
        
        user = self.model(
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,name,password):
        user = self.create_user(
            name=name,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    name = models.CharField(
        max_length=30, 
        unique=True,
        validators=[MinLengthValidator(5,), RegexValidator(r'^[a-zA-Z0-9]*$',)]
        )
    email = models.EmailField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'name'
    #REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class AccountToken(models.Model):

    @staticmethod
    def create(account:Account):
        if AccountToken.objects.filter(account=account).exists():
            AccountToken.objects.get(account=account).delete()
        
        dt = timezone.now()
        str = account.name + account.password + dt.strftime('%Y%m%d%H%M%S%f')
        hash = hashlib.sha1(str.encode('utf-8')).hexdigest()

        token = AccountToken.objects.create(
            account = account,
            token = hash,
            datetime = dt
            )

        return token
    
    def get(token_str: str):
        if AccountToken.objects.filter(token=token_str).exists():
            return AccountToken.objects.get(token=token_str)
        else:
            return None

    def check_valid_token(self):
        delta = timedelta(minutes=30)
        if(delta < timezone.now() - self.datetime):
            return False

        return True

    def update_datetime(self):
        self.datetime = timezone.now()
        self.save()

    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    token = models.CharField(max_length=40)
    datetime = models.DateTimeField()

    def __str__(self):
        return self.token