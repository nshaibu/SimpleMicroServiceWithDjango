from django.urls import path

from . import views

app_name = "get_api"

urlpatterns = [
    path('get/<str:key>/', views.get_redis),
]