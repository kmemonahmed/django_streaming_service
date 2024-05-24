from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subscription/', SubscriptionViewSet.as_view({'post': 'create_subscription'})),
]
