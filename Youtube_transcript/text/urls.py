from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sitemapurl/', views.sitemap_upload, name='sitemap_upload'),
    path('sitemapxml/', views.sitemap, name='sitemap'),
]