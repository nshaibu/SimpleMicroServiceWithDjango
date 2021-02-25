from django.urls import path

from . import views

app_name = "set_api"

urlpatterns = [
    path('set/values/', views.set_redis),
]