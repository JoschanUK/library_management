from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import booklist

# Create your views here.
#def index(request):
#   return HttpResponse("Leave Management System")

class PostList(generic.ListView):
    model = booklist
    template_name = "blog/index.html"
    paginate_by = 6