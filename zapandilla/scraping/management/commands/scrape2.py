from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from zapandilla.scraping.models import Zapatilla


class Command(BaseCommand):
    help = "collect jobs"
    
    def handle(self, *args, **kwargs):
        html = urlopen('https://sparta.cl/zapatillas.html')
        soup = BeautifulSoup(html, 'html.parser')
        
        # grab all the zapatillas
        zapatillas = soup.find_all("li", class_="item product product-item")
        for z in zapatillas:
            local_url = z.find('a', class_='product-item-link')['href']
            description = z.find('a', class_='product-item-link').text
            price = z.find('div', class_='price')
            # image = z.find('img', class_='product-image-photo').text 

            #check urls
            try:
                Zapatilla.objects.create(
                    local_url = local_url,
                    description = description,
                    price = price,
                    # image = image
                )
                print('%s added' % (description,) )
            except:
                print('%s already exists' % (description,) )
        self.stdout.write('Job complete!')



