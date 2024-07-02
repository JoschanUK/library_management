from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(template_name="main_page/index.html"), name='home'),
    path('<slug:slug>/', views.book_detail, name='book_detail'),
]