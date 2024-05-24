from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=False)
    subscription_expiry = models.DateTimeField(null=True, blank=True)

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
