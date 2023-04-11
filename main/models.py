from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

class Product(models.Model):
    name  = models.CharField(max_length=200)
    desc = models.TextField()
    price  = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)])
    slug  = models.SlugField(unique=True, max_length=200, blank= True)
    image = models.URLField(blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name