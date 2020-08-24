from django.urls import path
from .views import Annuities, AnnuityDetail, PresentValue

urlpatterns = [
    path('annuities/', Annuities.as_view(), name='annuties'),
    path('annuities/<int:pk>/', AnnuityDetail.as_view(), name='annuity-detail'),
    path('pv/', PresentValue.as_view(), name='present-value')
]
