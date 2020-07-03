# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from scraping.models import Zapatilla


class Command(BaseCommand):
    help = "collect jobs"
    
    def handle(self, *args, **options):
        html = urlopen('https://sparta.cl/zapatillas.html?p=2')        
        soup = BeautifulSoup(html, 'html.parser')        
        # grab all the zapatillas
        zapatillas = soup.find_all("div", class_="product-item-info")
        for z in zapatillas:
            local_url = z.find('a', class_='product-item-link')['href']
            description = z.find('a', class_='product-item-link').text
            price = z.find('span', class_='price').text            

            #check urls
            try:
                Zapatilla.objects.create(
                    local_url = local_url,
                    description = description,
                    price = price,
                )
                print('added', local_url)
            except:
                
                print("Ya existe", price)
        self.stdout.write( '\n job complete' )