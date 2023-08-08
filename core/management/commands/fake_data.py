import random
from datetime import datetime, timedelta
from faker import Faker
from django.core.management.base import BaseCommand
from core.models import Transaction  # Replace 'your_app' with the actual name of your Django app

fake = Faker()

class Command(BaseCommand):
    help = 'Generate and save fake transaction data to the Transaction model'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, nargs='?', default=100, help='Number of fake records to generate')

    def handle(self, *args, **options):
        num_fake_records = options['num_records']
        self.generate_and_save_fake_data(num_fake_records)
        self.stdout.write(self.style.SUCCESS(f'Successfully generated and saved {num_fake_records} fake transactions'))

    def generate_fake_transaction(self):
        return Transaction(
            address=fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'),
            type_of_event=random.choice(['Transfer', 'Transaction', 'Deposit']),
            sender_address=fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'),
            recipient_address=fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'),
            time_of_transaction=fake.date_time_between(start_date='-30d', end_date='now'),
            previous_report=fake.word(),
            block_height=fake.random_int(min=10000, max=20000),
            type_of_blockchain=random.choice(['Ethereum', 'Bitcoin', 'Ripple']),
        )

    def generate_and_save_fake_data(self, num_records):
        for _ in range(num_records):
            fake_transaction = self.generate_fake_transaction()
            fake_transaction.save()
