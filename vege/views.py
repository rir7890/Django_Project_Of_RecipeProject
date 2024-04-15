from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

        # this comment code is necessary when we are using the search input tag with button
        # And we have to add the search input tag in the form with post and get method
        # queryset = Recipe.objects.all()
        # if request.GET.get('search'):
        #     queryset = queryset.filter(
        #         recipe_name__icontains=request.GET.get('search'))
        return redirect('/home')
        # return render(request, 'register.html')
    else:
        return render(request, 'register.html')


@login_required(login_url="/login/")
def Home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes': recipes})


def DeleteData(request, recipe_id):
    # recipe_id = request.GET['recipe_id']
    Recipe.objects.filter(id=recipe_id).delete()
    return redirect('/home')


def UpdateData(request, recipe_id):
    if request.method == 'POST':
        # image_field=request.FILES.get('image_field')
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        # print(recipe_description, recipe_name)
        recipeInfo = Recipe.objects.get(id=recipe_id)
        recipeInfo.recipe_name = recipe_name
        recipeInfo.recipe_description = recipe_description
        # if image_field:
        #     recipeInfo.image_field = image_field
        recipeInfo.save()
    return redirect('/home')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/home')
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(first_name, last_name, username, password)
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User already exists")
            return redirect('/register')
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('/register')
    return render(request, 'rregister.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')
