from django.db import models
from account.models import Account

# Create your models here.

class Islands(models.Model):

    account = models.ForeignKey(Account,on_delete=models.CASCADE,unique=True)
    name = models.CharField(max_length=30)
    turn = models.IntegerField(default=0)
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
    contributor = models.ForeignKey(Islands,on_delete=models.SET_NULL,blank=True,null=True)
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title

class Bbs_content(models.Model):
    contributor = models.ForeignKey(Bbs,on_delete=models.CASCADE,blank=True,null=True)
    content = models.TextField()

    def __str__(self):
        return self.content

class Note(models.Model):
    contributor = models.ForeignKey(Islands,on_delete=models.SET_NULL,blank=True,null=True)
    title = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title

class Note_content(models.Model):
    contributor = models.ForeignKey(Note,on_delete=models.CASCADE,blank=True,null=True)
    content = models.TextField()

    def __str__(self):
        return self.content