
from django.contrib import admin
from .models import Restaurant,Table,MenuItem


class TableAdmin(admin.ModelAdmin):
    list_display = ("number", "restaurant", "qr_code")

admin.site.register(MenuItem)
admin.site.register(Restaurant)
admin.site.register(Table, TableAdmin)
