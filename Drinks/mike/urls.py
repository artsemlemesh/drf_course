from django.urls import path
from .views import name_list, name_detail


urlpatterns = [
    path('names/', name_list),
    path('names/<int:pk>', name_detail)

]