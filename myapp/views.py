from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.


def index(request):
    consumed_food=None

    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()
        if request.user.is_authenticated:
            consumed_food = Consume.objects.filter(user=request.user)

    else:
        foods = Food.objects.all()
    

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')