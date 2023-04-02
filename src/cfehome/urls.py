
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home_view),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
