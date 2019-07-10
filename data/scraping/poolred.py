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

import pytz
from datetime import datetime
import requests as rq
from bs4 import BeautifulSoup

from data.models import SubCategory, DataPrice

class PoolRed(object):

    def __init__(self, url, *args, **kwargs):
        self.url = url
        self.content = self.get_content()
        self.soup_content = self.soup_content(self.content)

        self.ROW_NUMBER_VIRGIN_EXTRA_OLIVE_OIL = 1
        self.ROW_NUMBER_VIRGIN_OLIVE_OIL = 2
        self.ROW_NUMBER_LAMPANTE_OLIVE_OIL = 3

        self.oils = [
            (SubCategory.objects.get(name='Extra Virgin Olive Oil'), self.ROW_NUMBER_VIRGIN_EXTRA_OLIVE_OIL),
            (SubCategory.objects.get(name='Virgin Olive Oil'), self.ROW_NUMBER_VIRGIN_OLIVE_OIL),
            (SubCategory.objects.get(name='Lampante Olive Oil'), self.ROW_NUMBER_LAMPANTE_OLIVE_OIL)
        ]

    def init_scraping(self):
        init_message = '- Starting Scraping {}...'.format(self.url) 
        print(init_message)
        return init_message
    
    def end_scraping(self):
        end_message = '- End Scraping {}.'.format(self.url)
        print(end_message)
        return end_message

    def get_content(self):
        response = rq.get(self.url)
        return response.content
    
    def soup_content(self, content=None):
        if content is not None:
            return BeautifulSoup(content, 'html.parser')

    # MODEL DATA METHODS
    # -------------------------------------------------

    def start_scraping(self):
        for subcategory, row_number in self.oils:
            self.init_subcategory(subcategory)
            price = self.get_avg_price_per_subcategory(row_number)
            self.create_price_data(subcategory, price)

    def init_subcategory(self, subcategory):
        message = '------------ {} ------------'.format(subcategory.name)
        print(message)
        return message

    def create_price_data(self, subcategory, price, date=datetime.today()):
        dataprice = DataPrice.objects.create(
                        price=price,
                        date=date,
                        subcategory=subcategory
                    )
        print('\t+ Data Price created with price {price:.2f} assigned to {subcategory}.'.format(price=price, subcategory=subcategory.name))

    # SCRAPING METHODS
    # -------------------------------------------------

    # Get Table given HTML attributes.
    def get_data_table(self):
        return self.soup_content.find('table', attrs={'class': 'tExterior', 'align': 'center', 'width': 460})

    # Get Row per SubCategory
    def get_row_per_subcategory(self, row_number):
        return self.get_data_table().find_all('tr', recursive=False)[row_number]

    # Get Average Price and (€/t) and parse to float
    def get_avg_price_by_row(self, row):
        COLUMN_NUMBER = 2
        avg_price_string = row.find_all('td', recursive=False)[COLUMN_NUMBER].find('span', recursive=False).text
        avg_price = float(avg_price_string.replace('.', '').replace(',', '.'))
        return avg_price

    def get_avg_price_per_subcategory(self, row_number):
        row = self.get_row_per_subcategory(row_number)
        return self.get_avg_price_by_row(row)