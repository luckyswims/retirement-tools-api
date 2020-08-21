from django.urls import path
from .views import Annuities

urlpatterns = [
    path('', Annuities.as_view(), name='annuties')
]
