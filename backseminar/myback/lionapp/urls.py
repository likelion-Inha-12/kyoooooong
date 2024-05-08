from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('create/',views.create_post),
    path('<int:pk>/',views.get_post),
    path('delete/<int:pk>',views.delete_post),
    path('comments/<int:post_id>',views.get_comment),
    path('member/', views.create_member),
    path('like/<int:user_id>/<int:post_id>', views.like),
    path('getlike/<int:post_id>', views.get_likes),
    path('sort', views.sort_post),
]