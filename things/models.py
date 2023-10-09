from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
class Thing(models.Model):
    name = models.CharField(max_length=30, unique = True)
    description = models.TextField(max_length =120, blank = True)
    def __str__(self):
        return self.name


# Create your models here.
