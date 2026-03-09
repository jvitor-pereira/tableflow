
from django.db import models
from restaurants.models import Table,MenuItem

class Order(models.Model):

    STATUS_CHOICES = [
        ("new", "Novo"),
        ("preparing", "Em preparo"),
        ("ready", "Pronto"),
        ("delivered", "Entregue"),
    ]

    table = models.ForeignKey("restaurants.Table", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total(self):
        return sum(item.get_total() for item in self.items.all())
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey("restaurants.MenuItem", on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def get_total(self):
        return self.quantity * self.menu_item.price

