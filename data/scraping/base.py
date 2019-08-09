#!/usr/bin/env python

"""
    Scraping Base Class - Common Methods & Functions. 
"""

__author__ = "Rafael García Cuéllar"
__email__ = "rafa@loones.es"
__copyright__ = "Copyright (c) 2019 Loones - Rafael García Cuéllar"
__license__ = "Loones"

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

import requests as rq
from requests.exceptions import SSLError
from bs4 import BeautifulSoup

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from data.models import DataPrice

class ScrapingBase(ABC):
    
    def __init__(self, url, *args, **kwargs):
        self.url = url
        self.content = self.get_content()
        self.soup_content = self.soup_content(self.content)

    def init_scraping(self):
        init_message = '\n- Starting Scraping {} ...'.format(self.url) 
        print(init_message)
        return init_message
    
    def end_scraping(self):
        end_message = '- End Scraping {} .'.format(self.url)
        print(end_message)
        return end_message

    def get_content(self):
        try:
            response = rq.get(self.url)    
        except SSLError as e:
            response = rq.get(self.url, verify=False)
        return response.content
    
    def soup_content(self, content=None):
        if content is not None:
            return BeautifulSoup(content, 'html.parser')

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
        print('\t+ Data Price -> price: {price:.2f}, date: {date} subcategory: {subcategory}.'.format(price=price, date=str(date), subcategory=subcategory.name))

    # ABSTRACT METHODS
    # ------------------------------------------------
    @abstractmethod
    def start_scraping(self):
        raise NotImplementedError

    # FORMATS
    # ------------------------------------------------
    def format_to_float(self, avg_price_string):
        try:
            result = float(avg_price_string.replace('.', '').replace(',', '.')) 
        except ValueError as e:
            result = None
        return result

    def get_date_range_from_week(self, p_year,p_week):
        firstdayofweek = datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w")#.date()
        lastdayofweek = firstdayofweek + timedelta(days=6.9)
        return firstdayofweek #, lastdayofweek

    # https://stackoverflow.com/questions/17087314/get-date-from-week-number
    def get_date_by_year_and_number_week(self, year, week_number):
        if year != []:
            string_date = "{0}-W{1}".format(str(year), str(week_number))
            return datetime.strptime(string_date + '-1', "%Y-W%W-%w")
        return None

    def get_number_month_by_month_abrv(self, month_abrv):
        return {
        'En.': 1,
        'Fb.': 2,
        'Mr.': 3,
        'Ab.': 4,
        'My.': 5,
        'Jn.': 6,
        'Jl.': 7,
        'Ag.': 8,
        'Sp.': 9,
        'Oc.': 10,
        'Nv.': 11,
        'Dc.': 12,
        '': None
    }[month_abrv]
