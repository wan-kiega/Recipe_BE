from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    # You can add custom fields here later (bio, avatar, etc.)
    pass

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField("Ingredient", through="RecipeIngredient")

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)  # e.g. "2 cups"

class SharedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="shared")
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shared_recipes")
    created_at = models.DateTimeField(auto_now_add=True)
