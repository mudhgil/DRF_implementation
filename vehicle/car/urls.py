from django.urls import path,include
from rest_framework.routers import DefaultRouter
from car import views


router = DefaultRouter()
router.register('brands', views.BrandViewset, basename = 'brands')
router.register('cars', views.CarsViewset, basename = 'cars')



urlpatterns = [
    
    path('', include(router.urls)),
    
]