from django.db import models
from .validators import validate_category


class VehicleProfile(models.Model):
    make = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    sub_model = models.CharField(max_length=120)
    year = models.IntegerField(max_length=4)
    color = models.CharField(max_length=50)
    category = models.CharField(max_length=120, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.make

