from rest_framework import viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

import stripe
from django.conf import settings
from rest_framework.views import APIView

class SubscriptionViewSet(viewsets.ViewSet):
    def create_subscription(self, request):
        user = request.user
        stripe.Customer.create(
            email=user.email,
            name=user.username,
        )
        return Response({"status": "Subscription created"})
