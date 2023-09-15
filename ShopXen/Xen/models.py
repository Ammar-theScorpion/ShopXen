from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField()
    def __str__(self) -> str:
        return self.name