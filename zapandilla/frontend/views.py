from django.shortcuts import render
from django.views.generic.list import ListView
# scraping models
from scraping.models import Zapatilla

class ZapatillaListView(ListView):

    model = Zapatilla
    template_name = 'frontend/home.html'
    paginate_by = 20  # if pagination is desired
    
