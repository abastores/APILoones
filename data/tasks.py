from django.core.management import call_command
from celery import task

POOLRED_COMMAND_NAME = 'poolred_scraping'
MAPGOB_COMMAND_NAME = 'mapgob_periodic_scraping'

@task(name='poolred_scraping_data') 
def poolred_scraping_data():
    call_command(POOLRED_COMMAND_NAME)

@task(name='mapgob_periodic_scraping_data') 
def mapgob_periodic_scraping_data():
    call_command(MAPGOB_COMMAND_NAME)

