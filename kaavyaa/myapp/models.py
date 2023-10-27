from django.db import models
from django.contrib import admin
class Football_Players(models.Model):
    stuid=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    scores=models.IntegerField()

class Football_PlayersAdmin(admin.ModelAdmin):
    list_display=('stuid','name','age','address','scores')



# Create your models here.
