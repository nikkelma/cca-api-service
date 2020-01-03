from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import (
    UserSerializer,
    GroupSerializer,
    StudentSerializer,
    SchoolSerializer,
)
from .models.school import School
from .models.student import Student


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAdminUser,
    )
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAdminUser,
    )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsAuthenticated,
    )
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
