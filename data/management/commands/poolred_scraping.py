#!/usr/bin/env python

"""
    Scrapping www.poolred.com to get the following data:
    - Extra Olive Oil
    - Virgin Olive Oil
    - Lampante (B.1º) Olive Oil 
"""

__author__ = "Rafael García Cuéllar"
__email__ = "rafa@loones.es"
__copyright__ = "Copyright (c) 2019 Loones - Rafael García Cuéllar"
__license__ = "Loones"

from django.core.management.base import BaseCommand, CommandError
from data.scraping.poolred import PoolRed 

class Command(BaseCommand):
    help = 'Scraping www.poolred.com'

    LAST_WEEK_URL = 'http://www.poolred.com/Publico/PreciosActualizados.aspx?tipo=0' 
    LAST_WEEK_URL_2 = 'http://www.poolred.com/Publico/PreciosActualizados.aspx?tipo=1' 
    LAST_MONTH_URL = 'http://www.poolred.com/Publico/PreciosActualizados.aspx?tipo=2'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        poolred = PoolRed(url=self.LAST_WEEK_URL)
        poolred.init_scraping()
        poolred.start_scraping()
        poolred.end_scraping()
        