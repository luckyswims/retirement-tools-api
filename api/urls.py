from django.urls import path
from .views import Annuities, AnnuityDetail

urlpatterns = [
    path('', Annuities.as_view(), name='annuties'),
    path('<int:pk>/', AnnuityDetail.as_view(), name='annuity-detail')
]
