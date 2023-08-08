import json
from typing import Any, Optional
from faker import Faker
from django.core.management.base import BaseCommand
from core.models import Transaction  # Replace 'your_app' with the actual name of your Django app
from datetime import datetime
import pytz

fake = Faker()

class Command(BaseCommand):
    help = 'Generate and save fake transaction data to the Transaction model'
    def handle(self, *args: Any, **options: Any) -> str :

        # Load data from a JSON file
        with open('data.json', 'r') as f:
            data = json.load(f)

        # Create and save Transaction objects
        for item in data:
            naive_dt = datetime.strptime(item['time'], '%d %b %Y %H:%M:%S')

            tz = pytz.timezone('Asia/Kolkata')

            aware_dt = tz.localize(naive_dt)
            transaction = Transaction(
                transactionHash=item['transactionHash'],
                type=item['type'],
                logo=item['logo'],
                sender=item['sender'],
                amount=item['amount'],
                reciever_to=item['reciever']['to'],
                reciever_amount=item['reciever']['amount'],
                time=aware_dt
            )
            transaction.save()

