from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey


class DishType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price =  models.DecimalField(max_digits=8, decimal_places=2)

    dish_type = ForeignKey(
        DishType,
        on_delete=models.SET_NULL,
        related_name="dishes",
        null=True,
        blank=True
    )

    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes"
    )