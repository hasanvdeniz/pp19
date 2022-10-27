from django.db import models

class Blog(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=250)
    file=models.FileField(upload_to='media/')

class Readers(models.Model):
    reader=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
