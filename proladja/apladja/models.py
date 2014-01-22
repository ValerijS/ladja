from django.db import models

# Create your models here.
class users(models.Model):

 name=models.CharField(max_length=128,unique=True)

 paycheck=models.IntegerField(default=0)

 date_joined=models.DateField()

class rooms(models.Model):

 department=models.CharField(max_length=128,unique=True)

 spots=models.IntegerField(default=0)



class users2(models.Model):
 name2=models.CharField(max_length=128,unique=True)
 paycheck2=models.IntegerField(default=0)
 date_joined2=models.DateField()
class rooms2(models.Model):
 department2=models.CharField(max_length=128,unique=True)
 spots2=models.IntegerField(default=0)
