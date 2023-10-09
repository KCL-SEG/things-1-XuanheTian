from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator
class Thing(models.Model):
    name = models.CharField(max_length=30, unique = False , blank = False)
    description = models.CharField(max_length =120, blank = True)
    quantity = models.IntegerField(
        validators = [MinValueValidator(0),MaxValueValidator(100)]
    )
    def __str__(self):
        return self.name


# Create your models here.
