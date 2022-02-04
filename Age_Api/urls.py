from django.urls import include, path

from rest_framework import routers

from Age_Api.views import AgeViewSet

router = routers.DefaultRouter()
router.register(r'Age', AgeViewSet)


urlpatterns = [
   path('', include(router.urls)),
]