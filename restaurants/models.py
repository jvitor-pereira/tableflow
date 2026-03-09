
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Table(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    number = models.IntegerField()
    qr_code = models.ImageField(upload_to="qrcodes/", blank=True)

    def __str__(self):
        return f"Mesa {self.number}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.qr_code:
            qr_data = f"http://127.0.0.1:8000/menu/{self.id}"
            qr = qrcode.make(qr_data)

            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            file_name = f"table_{self.id}.png"
            self.qr_code.save(file_name, File(buffer), save=False)

            super().save(update_fields=["qr_code"])

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
