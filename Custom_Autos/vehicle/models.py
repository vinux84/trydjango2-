from django.db import models
from .validators import validate_category
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save


class VehicleProfile(models.Model):
    make = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    sub_model = models.CharField(max_length=120, blank=True)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    category = models.CharField(max_length=120, validators=[validate_category])
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.make

    @property
    def title(self):
        return self.make

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


def vehicleprofile_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(vehicleprofile_pre_save_receiver, sender=VehicleProfile)

