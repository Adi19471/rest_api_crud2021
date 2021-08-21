from django.db import models

# Create your models here.
from datetime import  datetime
class BooksModel(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=100)
    ready_by = models.CharField(max_length=120)
    posted_date= models.DateField(auto_now_add=True)