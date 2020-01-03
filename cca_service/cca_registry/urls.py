from django.urls import path, include
from rest_framework import routers
from . import views

ROUTER = routers.DefaultRouter()
ROUTER.register(r"users", views.UserViewSet)
ROUTER.register(r"groups", views.GroupViewSet)
ROUTER.register(r"schools", views.SchoolViewSet)
ROUTER.register(r"students", views.StudentViewSet)

urlpatterns = [path("", include(ROUTER.urls))]
