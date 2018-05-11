import csv

from django.core.management.base import BaseCommand
from crmapp.models import Bank, Partner


class Command(BaseCommand):

    def csv_reader(self, file):
        reader = csv.DictReader(file, delimiter=';')
        return reader

    def import_data(self, csv_content):
        Partner.objects.all().delete()
        for row in csv_content:
            partners = row.values()
            Partner.upload_to_db(self, list(partners))

    def handle(self, *args, **options):
        filename = 'partners.csv'
        with open(filename, 'r') as csv_file:
            csv_content = self.csv_reader(csv_file)
            self.import_data(csv_content)