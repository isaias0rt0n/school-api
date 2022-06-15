from django.urls import include
from django.urls.conf import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'users', views.UserRegisterViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
