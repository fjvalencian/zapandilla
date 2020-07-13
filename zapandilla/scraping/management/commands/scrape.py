

from django.core.management.base import BaseCommand
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from scraping.models import Zapatilla


class Command(BaseCommand):
    help = "collect jobs"
    
    def handle(self, *args, **options):
   
        for page in range(1,7):
            
            html = urlopen('https://sparta.cl/zapatillas.html?p={}'.format(page))
            
            soup = BeautifulSoup(html ,'html.parser') 
                                       
            # grab all the zapatillas
            zapatillas = soup.find_all("div", class_="product-item-info")
           
            for z in zapatillas:
                local_url = z.find('a', class_='product-item-link')['href']
                description = z.find('a', class_='product-item-link').text                
                price = z.find('span', class_='price').text
                image = z.findAll('img')
               
                for img in image:                    
                    imgurl = img['src']                                    
                    
                try:
                    Zapatilla.objects.create(
                        local_url = local_url,
                        description = description,
                        price = price,
                        image = img['src'],
                       
                    )
                    print('added', local_url)
                except:                
                    print("Ya existe", price)
            self.stdout.write( '\n job complete' )