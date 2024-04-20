from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_descirption = data.get('recipe_descirption')
        recipe_image = request.FILES.get('recipe_image')
        print(recipe_name)
        print(recipe_descirption)
        print(recipe_image)
        Recipe.objects.create(recipe_image=recipe_image,recipe_name=recipe_name,recipe_descirption=recipe_descirption)
        return redirect('http://127.0.0.1:8000/')
    return render(request, 'recipes.html')