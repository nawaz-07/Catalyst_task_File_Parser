from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to='files')

class CSVData(models.Model):
    emp_id=models.CharField(max_length=20, null=True, blank=True)
    name=models.CharField(max_length=100, null=True, blank=True)
    year=models.CharField(max_length=29, null=True, blank=True)
    domain=models.CharField(max_length=100, null=True, blank=True)
    industry=models.CharField(max_length=100, null=True, blank=True)
    size=models.CharField(max_length=10, null=True, blank=True)
    area=models.CharField(max_length=500, null=True, blank=True)
    