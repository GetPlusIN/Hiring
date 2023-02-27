from django.db import models





class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    published_date=models.DateField(max_length=10)
    description=models.TextField(max_length=200)

