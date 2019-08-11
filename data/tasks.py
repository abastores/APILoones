from django.core.management import call_command
from celery import task

COMMAND_NAME = 'poolred_scraping'

@task(name='poolred_scraping_data') 
def poolred_scraping_data():
    call_command(COMMAND_NAME)
