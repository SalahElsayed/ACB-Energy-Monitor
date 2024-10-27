from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ACBUnitViewSet

router = DefaultRouter()
router.register('acb-units', ACBUnitViewSet, basename='acb-units')

urlpatterns = [
    path('', include(router.urls)),
]