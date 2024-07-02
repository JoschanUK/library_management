from django.db import models
from django.contrib.auth.models import User

class Booklist(models.Model):
    bookid = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    
