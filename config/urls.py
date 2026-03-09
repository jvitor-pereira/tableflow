
from django.contrib import admin
from django.urls import path, include
from restaurants.views import landing, menu_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("orders.urls")),  # Handles all order-related URLs
    path('', landing, name='landing'),
    path('menu/<int:table_id>/', menu_view, name='menu'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
