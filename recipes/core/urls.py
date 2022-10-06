from django.urls import path

from recipes.core.views import show_index, create_recipe, edit_recipe, delete_recipe, show_recipe

urlpatterns = [
    path('', show_index, name='show index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', show_recipe, name='show recipe'),
]
