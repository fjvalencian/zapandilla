# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Zapatilla(models.Model):
    """Model definition for Zapatilla."""    
    name = models.CharField(max_length=250)    
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    currrent_price = models.CharField(max_length=250)
    image = models.CharField(max_length=250, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    origin = models.CharField(max_length=255, blank=True)
    local_url = models.CharField(max_length=255, blank=True, unique=True)
    store = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
    
    class Meta:
        """Meta definition for Zapatilla."""
        ordering = ['name']
        verbose_name = 'Sparta Zapatilla'
        verbose_name_plural = 'Sparta Zapatillas'
        unique_together = ("description", "price")        

    def __str__(self):
        """Unicode representation of Zapatilla."""
        return self.description
        
        


