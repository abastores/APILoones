# Commands to run Periodic tasks in Production
redis-server
celery -A apiloones worker -B -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler