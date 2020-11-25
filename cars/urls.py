from django.urls import path, include
from cars import views

urlpatterns = [
    path('', views.all_cars, name='cars'),
    path('accounts/', include("django.contrib.auth.urls")),
    path("oauth/", include("social_django.urls", namespace='social')),
    path('register/', views.register, name="register"),
    path('userdetails/', views.userDetails, name='userDetails'),
    path('display/', views.userDetails, name='display'),
    path('showcars/', views.all_cars, name='cars'),
    path("showcars/<int:pk>/", views.all_car_details,name='all_car_details'),
    path("updatecar/<int:pk>/",views.update_details,name='update_details'),
    path("deletecar/<int:pk>/",views.delete_car,name='delete_car'),
]
