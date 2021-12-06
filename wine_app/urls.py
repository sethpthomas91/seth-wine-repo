
from django.contrib import admin
from django.urls import path, include
from wine_app.views import *

urlpatterns = [
    path('', wine_list, name='wine_list'),
    path('create', create_wine, name='create_wine'),
    path('<int:wine_id>/', wine_detail, name='wine_detail'),
    path('<int:wine_id>/update', edit_wine, name='update_wine'),
    path('<int:wine_id>/delete', delete_wine, name='delete_wine'),
]
