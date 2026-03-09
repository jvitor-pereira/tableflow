from django.urls import path
from orders import views

urlpatterns = [
    # The admin URL is best placed in the project's root urls.py
    path("kitchen/", views.kitchen, name="kitchen"),
    path("create-order/", views.create_order, name="create_order"),

    path(
        "update-status/<int:order_id>/<str:status>/",
        views.update_order_status,
        name="update_order_status",
    ),
]