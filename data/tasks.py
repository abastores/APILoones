from django.core.management import call_command
from django.db import connection
from celery import task

POOLRED_COMMAND_NAME = 'poolred_scraping'
MAPGOB_COMMAND_NAME = 'mapgob_periodic_scraping'
FILE_PATH = 'scraping/delete_bad_data_prices.sql'

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

