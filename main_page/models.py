from django.db import models
from django.contrib.auth.models import User

class booklist(models.Model):
    bookid = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

class member_records(models.Model):
    userid = models.IntegerField(unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    books_allowed = models.IntegerField()

class comment(models.Model):
    commentid = models.IntegerField(unique=True)
    userid = models.ForeignKey(
        member_records, on_delete=models.CASCADE
    )
    comments = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

class book_borrowed(models.Model):
    bookid = models.OneToOneField(booklist, on_delete=models.CASCADE)
    userid = models.OneToOneField(member_records , on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    time_extended = models.IntegerField(default=0)


    
