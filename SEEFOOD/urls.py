from django.urls import path
from . import views

urlpatterns = [
    path('',views.upload),
    path('save/', views.save),
]
