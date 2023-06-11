from django.conf.urls import url
from rest_framework import routers
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'view-post', views.ViewPostViewSet, basename="view-post")  # NOQA

urlpatterns = [
  # other urls
]

urlpatterns += router.urls