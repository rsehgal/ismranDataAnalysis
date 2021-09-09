from django.db import models

# Create your models here.

class DataFiles(models.Model):
	fileName = models.CharField(max_length=500)
	size=models.CharField(max_length=20)
	publicationDate=models.DateTimeField('publicationDate')
	rollOver=models.BooleanField(default=False)
	remarks=models.CharField(max_length=500)


