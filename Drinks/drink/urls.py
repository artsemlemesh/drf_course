from django.urls import path
from .views import drink_list, drink_detail


urlpatterns = [
    path('drinks/', drink_list),
    path('drinks/<int:pk>', drink_detail)
]