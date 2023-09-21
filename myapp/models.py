from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Gsk(models.Model):
    Patient_name=models.CharField(max_length=200)
    Patient_ID=models.IntegerField()
    Patient_address=models.TextField(max_length=200)
    Patient_Bill=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)



