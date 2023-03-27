from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=120, null=False)
    handle = models.SlugField(unique=True),
    price = models.DecimalField(
        decimal_places=2, max_digits=10, default=9.99)
    og_price = models.DecimalField(
        decimal_places=2, max_digits=10, default=9.99)
    price_changed_timestamp = models.DateTimeField(
        auto_now=False, blank=True, auto_now_add=False)
    stripe_price = models.IntegerField(default=999)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.price != self.og_price:
            self.og_price = self.price
            self.stripe_price = int(self.price * 100)
            self.price_changed_timestamp = timezone.now()

        super().save(*args, **kwargs)
