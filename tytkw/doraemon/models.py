from django.db import models
class nhanvat(models.Model):
       tennhanvat = models.CharField(max_length=400)
       catinh = models.CharField(max_length=600)
       nhiemvu = models.CharField(max_length=700)  
