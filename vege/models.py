from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.TextField()
    image_field = models.ImageField(upload_to='recipe/')
    recipe_view_count = models.IntegerField(default=1)
