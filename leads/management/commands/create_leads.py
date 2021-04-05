from _csv import reader
from csv import DictReader

from django.core.management import BaseCommand

from leads.models import Lead, UserProfile


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)
        parser.add_argument('organisor_email', type=str)

    def handle(self, *args, **options):
        file_name = options['file_name']
        organisor_email = options['organisor_email']

        organisation = UserProfile.objects.get(user__email=organisor_email)

        with open(file_name, 'r') as read_object:
            csv_reader = DictReader(read_object)
            for row in csv_reader:
                first_name = row['first_name']
                last_name = row['last_name']
                age = row['age']
                email = row['email']
                Lead.objects.create(
                    organisation=organisation,
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    email=email,
                )
