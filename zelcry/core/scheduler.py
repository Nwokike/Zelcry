from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)

def seed_crypto_data_job():
    """Background job to seed crypto data"""
    try:
        logger.info("Running automated crypto data seeding...")
        call_command('seed_crypto_data')
        logger.info("Crypto data seeding completed successfully")
    except Exception as e:
        logger.error(f"Error in crypto data seeding: {e}")

def start_scheduler():
    """Start the background scheduler for automated tasks"""
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(
        seed_crypto_data_job,
        'interval',
        hours=1,
        id='seed_crypto_data',
        replace_existing=True,
        name='Seed Cryptocurrency Data'
    )
    
    scheduler.start()
    logger.info("Crypto data scheduler started - running every hour")
