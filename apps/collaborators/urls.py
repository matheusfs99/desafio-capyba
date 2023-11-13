from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CollaboratorsViewSet

router = DefaultRouter()
router.register("collaborator", CollaboratorsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
