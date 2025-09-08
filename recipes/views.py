from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import Ingredient, Recipe, SharedRecipe
from .serializers import (
    UserSerializer, IngredientSerializer, RecipeSerializer, SharedRecipeSerializer
)
from .permissions import IsOwnerOrReadOnly

# Create your views here.

User = get_user_model()

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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SharedRecipeViewSet(viewsets.ModelViewSet):
    queryset = SharedRecipe.objects.all()
    serializer_class = SharedRecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SharedRecipe.objects.filter(shared_with=self.request.user)
