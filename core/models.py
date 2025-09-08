from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]  

    def __str__(self):
        print(f"__str__ called, returning: {self.username}")
        return self.username


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        print(f"__str__ called, returning: {self.name}")
        return self.name


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ("Dessert", "Dessert"),
        ("Main Course", "Main Course"),
        ("Appetizer", "Appetizer"),
        ("Side Dish", "Side Dish"),
        ("Beverage", "Beverage"),
        ("Other", "Other"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Other")
    preparation_time = models.IntegerField(help_text="Time in minutes")
    cooking_time = models.IntegerField(help_text="Time in minutes")
    servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField("Ingredient", through="RecipeIngredient")

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)


class SharedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="shared")
    shared_with = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shared_recipes")
    created_at = models.DateTimeField(auto_now_add=True)