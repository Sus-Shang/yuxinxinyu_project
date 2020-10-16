from django.core.management.base import BaseCommand, CommandError
from squirrel.models import Sighting

import csv
import sys

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type = str)

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = Sighting._meta.fields
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i in Sighting.objects.all():
                row = [getattr(i, field.name) for field in fields]
                writer.writerow(row)
            f.close()
