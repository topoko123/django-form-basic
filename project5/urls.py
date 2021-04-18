from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('request-obj/', views.request_obj),
    path('form-get/', views.form_get),
    path('form-post/', views.form_post),
    path('search/', views.search),
    path('product/', views.product),
]
