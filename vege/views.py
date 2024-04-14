from django.shortcuts import render, redirect
from .models import Recipe


def Register(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        image_field = request.FILES.get('image_field')
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            image_field=image_field
        )
        # print(recipe_name, recipe_description, image_field)
        return redirect('/home')
        # return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def Home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})


def DeleteData(request, recipe_id):
    # recipe_id = request.GET['recipe_id']
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('/home')


def UpdateData(request, recipe_id):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        # print(recipe_description, recipe_name)
        recipeInfo = Recipe.objects.get(id=recipe_id)
        recipeInfo.recipe_name = recipe_name
        recipeInfo.recipe_description = recipe_description
        recipeInfo.save()
    return redirect('/home')
