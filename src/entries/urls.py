from .views import EntryViewSet
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', EntryViewSet)

urlpatterns = router.urls