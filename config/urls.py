from core import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name='index'),
    path('v1', include('config.v1_router')),
]
