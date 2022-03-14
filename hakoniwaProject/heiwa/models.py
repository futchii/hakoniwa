from django.db import models
from account.models import Account

# Create your models here.

class Islands(models.Model):

    account = models.ForeignKey(Account,on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=30)
    island = models.TextField()
    money = models.IntegerField(default=0)
    food = models.IntegerField(default=0)
    people = models.IntegerField(default=0)
    farm_worker = models.IntegerField(default=0)
    factory_worker = models.IntegerField(default=0)
    mine_worker = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Bbs(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title