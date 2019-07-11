#!/usr/bin/env python

"""
     Scrapping https://www.mapa.gob.es/app/precios-medios-nacionales/pmn_tabla.asp in order to obtain the following data:
     - Red Wine // Vino tinto sin DOP/IGP
     - White Wine // Vino blanco sin DOP/IGP
     - Shell Rice // Arroz cáscara
     - Barley Feed // Cebada pienso
     - Soft Bread Wheat // Trigo blando panificable
"""

__author__ = "Rafael García Cuéllar"
__email__ = "rafa@loones.es"
__copyright__ = "Copyright (c) 2019 Loones - Rafael García Cuéllar"
__license__ = "Loones"

from django.core.management.base import BaseCommand, CommandError
from data.scraping.mapgob import MapGob 

class Command(BaseCommand):
    help = 'Scraping https://www.mapa.gob.es/app/precios-medios-nacionales'

    # BASE URL's
    BASE_URL = 'https://www.mapa.gob.es/app/precios-medios-nacionales'
    DATA_URL = BASE_URL + '/pmn_historico.asp?codigo={}'

    # SubCategories CODE
    SOFT_BREAD_WHEAT_CODE = 1
    BARLEY_FEED_CODE = 2
    SHELL_RICE_CODE = 4
    RED_WINE_CODE = 7
    WHITE_WINE_CODE = 6
             
    # SubCategories URLS
    SUBCATEGORIES_URLS = [
        ('Red Wine', DATA_URL.format(RED_WINE_CODE)),
        ('White Wine', DATA_URL.format(WHITE_WINE_CODE)),
        ('Shell Rice', DATA_URL.format(SHELL_RICE_CODE)),
        ('Barley Feed', DATA_URL.format(BARLEY_FEED_CODE)),
        ('Soft Bread Wheat', DATA_URL.format(SOFT_BREAD_WHEAT_CODE)),
    ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for subcategory in self.SUBCATEGORIES_URLS:
            mapgob = MapGob(subcategory_name=subcategory[0], url=subcategory[1])
            mapgob.init_scraping()
            mapgob.start_scraping()
            mapgob.end_scraping()
        