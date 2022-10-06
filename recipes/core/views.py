from django.shortcuts import render, redirect

from recipes.core.forms import RecipeForm, DeleteRecipeForm
from recipes.core.models import Recipe


# Create your views here.


def show_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = RecipeForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('show index')
    else:
        recipe_form = RecipeForm(instance=recipe)

    context = {
        'recipe_form': recipe_form,
        'pk':pk
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe_form = DeleteRecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe_form.save()
            return redirect('show index')
    else:
        recipe_form = RecipeForm(instance=recipe)

    context = {
        'recipe_form': recipe_form,
        'pk': pk
    }
    return render(request, 'delete.html', context)


def show_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe_ingredients = recipe.ingredients.split(", ")
    context = {
        'recipe':recipe,
        'ingredients': recipe_ingredients
    }
    return render(request, 'details.html', context)
