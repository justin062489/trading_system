from django.urls import path
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'order', views.OrderViewSet, basename='order')

urlpatterns = router.urls