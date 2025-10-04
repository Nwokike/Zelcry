from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zelcry.core'
    
    def ready(self):
        try:
            from . import scheduler
            scheduler.start_scheduler()
        except Exception as e:
            print(f"Scheduler initialization error: {e}")
