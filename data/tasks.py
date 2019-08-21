from django.core.management import call_command
from django.db import connection
from celery import task
import os

module_dir = os.path.dirname(__file__)  # get current directory

POOLRED_COMMAND_NAME = 'poolred_scraping'
MAPGOB_COMMAND_NAME = 'mapgob_periodic_scraping'
FILE_PATH = os.path.join(module_dir, 'scraping/delete_bad_data_prices.sql')

@task(name='poolred_scraping_data') 
def poolred_scraping_data():
    call_command(POOLRED_COMMAND_NAME)

@task(name='mapgob_periodic_scraping_data') 
def mapgob_periodic_scraping_data():
    call_command(MAPGOB_COMMAND_NAME)
    with connection.cursor() as cursor:
        with open(FILE_PATH) as fp:
            for line in fp:
                cursor.execute(line)
        fp.close()
    cursor.close()

