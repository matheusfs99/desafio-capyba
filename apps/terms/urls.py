from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TermsViewSet

router = DefaultRouter()
router.register("term", TermsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
