from django.urls import path
from .views import ZapatillaListView

urlpatterns = [    
    path('',ZapatillaListView.as_view(), name="home" ),   
]
 