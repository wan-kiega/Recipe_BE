from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from typing import Any
from .models import Ingredient, Recipe, SharedRecipe
from .serializers import (
    UserSerializer, IngredientSerializer, RecipeSerializer, SharedRecipeSerializer
)
from .permissions import IsOwnerOrReadOnly

User = get_user_model()
Ingredient: Any



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "category", "ingredients__name"]
    filterset_fields = ["category", "preparation_time", "cooking_time", "servings"]
    ordering_fields = ["created_at", "preparation_time", "cooking_time", "servings"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SharedRecipeViewSet(viewsets.ModelViewSet):
    queryset = SharedRecipe.objects.all()
    serializer_class = SharedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SharedRecipe.objects.filter(shared_with=self.request.user)
