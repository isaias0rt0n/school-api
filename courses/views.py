from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, mixins
from django.contrib.auth.models import User

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer, UserRegisterSerializer
from .permissions import EhSuperUser


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        self.pagination_class.page_size = 2
        ratings = Rating.objects.filter(course_id=pk)
        page = self.paginate_queryset(ratings)

        if page is not None:
            serializer = RatingSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


# Create a user on database
class UserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
