from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class OnTap(models.Model):
    name = models.CharField(max_length=255)
    production = models.CharField(max_length=255, blank=True, null=True)
    alcohol = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Enter a percentage value (0 - 100)",
    )
    ibu = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],  # Ensure IBU is a non-negative integer
    )
    style = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
