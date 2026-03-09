
from django.shortcuts import render
from django.http import JsonResponse
from .models import Order,OrderItem
from restaurants.models import MenuItem,Table
import json
from django.shortcuts import get_object_or_404, redirect
from .models import Order

def kitchen(request):

    new_orders = Order.objects.filter(status="new").order_by("-created_at")
    preparing_orders = Order.objects.filter(status="preparing").order_by("-created_at")
    ready_orders = Order.objects.filter(status="ready").order_by("-created_at")

    return render(request,"kitchen.html",{
        "new_orders":new_orders,
        "preparing_orders":preparing_orders,
        "ready_orders":ready_orders
    })

def create_order(request):

    if request.method == "POST":

        data = json.loads(request.body)

        table_id = 1

        order = Order.objects.create(table_id=table_id)

        for item in data["items"]:

            menu_item = MenuItem.objects.get(id=item["id"])

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=1
            )

        return JsonResponse({"status":"ok"})
    
def update_order_status(request, order_id, status):
    order = get_object_or_404(Order, id=order_id)
    order.status = status
    order.save()

    return redirect("kitchen")