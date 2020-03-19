from django.db import models

# Create your models here.
#
# class Movies:
#     str:'title'
#     str:'cast'
#     str:'img'

class Movies(models.Model):
    title=models.CharField(max_length=100)
    cast=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
