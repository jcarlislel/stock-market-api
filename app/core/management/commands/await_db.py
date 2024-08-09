""""
Django command to wait for the database to be available
"""
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

class Command(BaseCommand):

    def handle(self, *args, **options):
        MAX_RETRIES: int = 5
        db_conn_attempts: int = 0

        while db_conn_attempts < MAX_RETRIES:  
            try: 
                self.check(databases=['default'])
                self.stdout.write(self.style.SUCCESS('Database connection [SUCCESS]'))
                break

            except OperationalError as e:
                print(e)
                self.stdout.write(self.style.ERROR('Database connection failed. Attempting to reconnect.'))
                db_conn_attempts += 1
    