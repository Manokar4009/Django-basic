from django.urls import path
from . import views

urlpatterns = [
  
    path('', views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewphoto, name='photo'),
    path('add/', views.addphoto, name='add'),
    #path('photo/<int:pk>/', views.deletephoto, name='delete'),
    #path('delete-product/<str:pk>/', views.deleteProduct, name='delete-prod'),
    path('delete/<int:id>/', views.deleteItem, name='delete'),

]