from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CarSpecsViewset

router = DefaultRouter()
router.register('car-specs', CarSpecsViewset, basename='car-specs')


urlpatterns = [
    url('', include(router.urls))
]
