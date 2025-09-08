from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Ingredient, Recipe, RecipeIngredient, SharedRecipe

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name"]


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), source="ingredient", write_only=True
    )

    class Meta:
        model = RecipeIngredient
        fields = ["id", "ingredient", "ingredient_id", "quantity"]


class RecipeSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    ingredients = RecipeIngredientSerializer(
        source="recipeingredient_set", many=True, required=False
    )

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "description",
            "instructions",
            "category",
            "preparation_time",
            "cooking_time",
            "servings",
            "created_at",
            "owner",
            "ingredients",
        ]

    def create(self, validated_data):
        ingredients_data = validated_data.pop("recipeingredient_set", [])
        recipe = Recipe.objects.create(**validated_data)
        for ing in ingredients_data:
            RecipeIngredient.objects.create(recipe=recipe, **ing)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop("recipeingredient_set", [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if ingredients_data:
            instance.recipeingredient_set.all().delete()
            for ing in ingredients_data:
                RecipeIngredient.objects.create(recipe=instance, **ing)
        return instance


class SharedRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        queryset=Recipe.objects.all(), source="recipe", write_only=True
    )
    shared_with = UserSerializer(read_only=True)
    shared_with_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="shared_with", write_only=True
    )

    class Meta:
        model = SharedRecipe
        fields = ["id", "recipe", "recipe_id", "shared_with", "shared_with_id", "created_at"]
