
from django.shortcuts import render,get_object_or_404
from .models import MenuItem,Table

def landing(request):
    return render(request,"landing.html")

def menu_view(request,table_id):
    table = get_object_or_404(Table,id=table_id)
    menu = MenuItem.objects.filter(restaurant=table.restaurant)
    return render(request,"menu.html",{"menu":menu,"table":table})
