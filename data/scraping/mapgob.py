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

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import itertools
import time

import requests as rq
from bs4 import BeautifulSoup

from data.models import DataPrice
from .base import ScrapingBase

from data.models import SubCategory

class MapGob(ScrapingBase):

    def __init__(self, subcategory_name, url, *args, **kwargs):
        self.subcategory = SubCategory.objects.get(name=subcategory_name)
        self.month_number = 0

        super().__init__(url)

    # MODEL DATA METHODS
    # -------------------------------------------------

    def start_scraping(self):
        self.init_subcategory(self.subcategory)
        for row in self.get_rows_from_tbody():
            row_data = self.get_celds_from_row(row)
            week_number, self.month_number = self.get_week_number_and_month_number(row_data['week'])
            
            for data in dict(itertools.islice(row_data.items(), 1, 4)).items():
                data = data[1]
                if data[1] is not None:
                    self.create_price_data(subcategory=self.subcategory, price=data[1], date=self.get_date_range_from_week(data[0], week_number))

    # SCRAPING METHODS
    # -------------------------------------------------

    # Get Table given HTML attributes.
    def get_data_table(self):
        return self.soup_content.find('table', attrs={'summary':'Precios Medios Nacionales: Historico'})

    # Get Table Heads
    def get_theads_from_table(self):
        return self.get_data_table().find_all('thead', recursive=False)

    # Get TBody
    def get_tbody_from_table(self):
        return self.get_data_table().find('tbody')

    # Get Rows
    def get_rows_from_tbody(self):
        return self.get_tbody_from_table().find_all('tr', recursive=False)

    # Get Celds
    def get_celds_from_row(self, row):
        celds = row.find_all('td', recursive=False)
        result = {
            'week': celds[1].find('span').text
        }

        for i, year in enumerate(self.get_years()):
            result['year' + str(i+1)] = [int(year), self.format_to_float(celds[2+i].find('span').text)]  # 2 + i => Explain 2 positions in advance + the position of the years array.
        return result

    # Get Years from theads 
    def get_years(self):
        thead = self.get_theads_from_table()[3]
        year_heads = thead.find('tr').find_all('th', recursive=False)[2:]
        return [year_head.find('div').find('span', attrs={'class': 'tabla_texto_normal'}).text.split('/')[0] for year_head in year_heads]

    # Get Week Label in Row
    def get_week_number_and_month_number(self, label_week):
        label_week = [label.strip() for label in label_week.split('-')]
        if len(label_week) == 2:
            month_number = self.get_number_month_by_month_abrv(label_week[1])
        else:
            month_number = self.month_number

        return int(label_week[0]), month_number

    def get_avg_price_per_subcategory(self, row_number):
        row = self.get_row_per_subcategory(row_number)
        return self.get_avg_price_by_row(row)