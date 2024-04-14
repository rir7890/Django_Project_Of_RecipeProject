from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.TextField()
    image_field = models.ImageField(upload_to='recipe/')
