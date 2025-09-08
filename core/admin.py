from django.contrib import admin
from .models import User, Ingredient, Recipe, RecipeIngredient, SharedRecipe

# Register your models here.

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(SharedRecipe)
