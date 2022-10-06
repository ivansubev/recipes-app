from django.forms import ModelForm

from recipes.core.models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(ModelForm):
    def save(self, commit=True):
        self.instance.delete()

    class Meta:
        model = Recipe
        fields = '__all__'
