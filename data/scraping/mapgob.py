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
from data.models import SubCategory

from .base import ScrapingBase

class MapGob(ScrapingBase):

    def __init__(self, subcategory_name, url, *args, **kwargs):
        self.subcategory = SubCategory.objects.get(name=subcategory_name)
        self.month_number = None
        self.week_number = None
        self.measure = None
        self.year_change = False

        self.clean_data = []

        super().__init__(url)

    # MODEL DATA METHODS
    # -------------------------------------------------

    def start_scraping(self):
        self.init_subcategory(self.subcategory)
        self.measure = self.get_measure_from_thead()

        # Get bulk of Data Price's
        data = []
        for row in self.get_rows_from_tbody():
            data += self.get_celds_from_row(row)

        self.clean_data = self.order_data_prices_by_date(data)
        self.perform_linear_insertion()

    def delete_old_data(self):
        print("Deleting Old Data from: {}".format(self.subcategory.name))
        deleted = DataPrice.objects.filter(subcategory=self.subcategory).delete()
        print("Successfully deleted {} records".format(deleted[0]))

    def perform_linear_insertion(self):
        for data_line in self.clean_data:
            if data_line[2] != None:
                data_line = self.prepare_data_line_to_insertion(data_line)
                if data_line[1] != []:
                    self.create_price_data(subcategory=self.subcategory, date=data_line[0], price=data_line[1])

    def prepare_data_line_to_insertion(self, data_line):
        clean_data_line = []
        if self.get_week_number_and_month_number(data_line[0]) != None:
            self.week_number, self.month_number = self.get_week_number_and_month_number(data_line[0])
        clean_data_line.append(self.get_date_by_year_and_number_week(self.get_year(data_line[1]), self.week_number))
        clean_data_line.append(data_line[2] * 10 if self.measure == '(euros / 100 kg)' else data_line[2])    # Convert from 100kg to T
        return clean_data_line


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
        celds = [celd for celd in reversed(row.find_all('td', recursive=False))]
        label_week = celds[3].find('span').text

        result = []
        for i, year_range in enumerate(reversed(self.get_years())):
            result.append([label_week, year_range, self.format_to_float(celds[i].find('span').text)])
        return result

    # Get Years from theads 
    def get_years(self):
        thead = self.get_theads_from_table()[3]
        year_heads = thead.find('tr').find_all('th', recursive=False)[2:]
        
        years = []
        for year_head in year_heads:
            year_head = year_head.find('div').find('span', attrs={'class': 'tabla_texto_normal'}).text
            years.append(year_head)
        return years

    # Get Year from range based on Month number
    def get_year(self, year_range):

        # If is Jan. then reinitialice the cycle otherwise if is Dec. get the old year. 
        if self.month_number == 1:
            self.year_change = True
        elif self.month_number == 12 or year_range == []:
            self.year_change = False
        
        year = year_range[:2] + year_range[-2:] if self.year_change else year_range[:-3]
        return year

    # Get Measure
    def get_measure_from_thead(self):
        label_measure = self.get_theads_from_table()[0].find('tr').find('th').find('div').find('span').text
        measure = label_measure[label_measure.find('('):]
        return measure

    # Get Week Label in Row
    def get_week_number_and_month_number(self, label_week):
        if label_week != []:
            label_week = [label.strip() for label in label_week.split('-')]
            if len(label_week) == 2:
                month_number = self.get_number_month_by_month_abrv(label_week[1])
            else:
                month_number = self.month_number

            return int(label_week[0]), month_number
        return None

    # Order the Data Price by Date 
    def order_data_prices_by_date(self, data):
        ordered_data_prices = []
        for i, year_range in enumerate(reversed(self.get_years())):
            ordered_data_prices.append([[], [], []])
            for line_data in data:
                if year_range == line_data[1]:
                    ordered_data_prices.append(line_data)
        return ordered_data_prices