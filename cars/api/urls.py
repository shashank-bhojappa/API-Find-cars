from django.urls import path
from django.conf.urls import url, include
from cars.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car_specs', views.CarSpecsViewSet, basename = 'car_specs')


urlpatterns = [
    path("api/showcars/<int:pk>/", views.get_car,name='get_car'),
    path("api/showcars/", views.create_car,name='create_car'),
    path("api/",include(router.urls)),
]
