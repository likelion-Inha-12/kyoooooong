from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/',views.create_post),
    path('post/<int:pk>/',views.get_post),
    path('delete/<int:pk>/',views.delete_post),
    path('v2/post/<int:pk>/',views.PostApiView.as_view()),
    path('v2/post',views.create_post_v2)
]