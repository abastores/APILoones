redis-server
celery -A apiloones worker -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler