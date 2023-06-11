from django.conf.urls import url
from rest_framework import routers
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'view-post', views.ViewPostViewSet, basename="view-post")  # NOQA
router.register(r'user-post', views.UserPostsViewSet, basename="user-post")  # NOQA
router.register(r'custom-post', views.CustomPostsViewSet, basename="custom-post")  # NOQA

urlpatterns = router.urls