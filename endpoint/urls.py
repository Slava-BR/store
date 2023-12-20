from django.urls import path

from endpoint.views import *

urlpatterns = [
    path('main/', main),
    path('collection/', collection),
    path('image/<slug:slug_title>/', image, name='image'),
    path('price/<slug:slug_title>/', price, name='price'),
    path('title/<slug:slug_title>/', title, name='title'),
    path('size/<slug:slug_title>/', size, name='size'),
    path('textile/<slug:slug_title>/', textile, name='textile'),
    path('material/<slug:slug_title>/', material, name='material'),
    path('collection/<slug:slug_title>/', title, name='collection'),
    path('type/<slug:slug_title>/', title, name='type'),
    path('detail/<slug:slug_title>/', detail, name='detail'),
]