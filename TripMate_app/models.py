from django.db import models
from django.utils.text import slugify

class Season(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='season_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Destination(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='destinations')
    name = models.CharField(max_length=100)
    description = models.TextField()
    best_months = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)

    def __str__(self):
        return self.name
