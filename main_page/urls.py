from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(template_name="main_page/book_list.html"), name='home'),
]