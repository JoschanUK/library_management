from django.shortcuts import render, get_object_or_404
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

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "main_page/book_detail.html",
        {"post": post},
    )