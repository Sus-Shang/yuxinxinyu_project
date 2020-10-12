import csv

import datetime

from django.core.management.base import BaseCommand
from .models import Sighting


class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        path = options['path']
        with open(path,r) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        squirrel_data=[]
        for dict_ in data:
            squirrel_data.append(Sighting(
                latitude = float(dict_['Y']),
                longitude = float(dict_['X']),
                unique_squirrel_ID = dict_['Unique Squirrel ID'],
                shift = dict_['Shift'],
                date = datetime.datetime.strptime(dict_['Date'],'%m%d%Y'),
                age = dict_['Age'],
                primary_fur_color = dict_['Primary Fur Color'],
                location = dict_['Location'],
                specific_location = row['Specific Location'],
                running = dict_['Running'],
                chasing = dict_['Chasing'],
                climbing = dict_['Climbing'],
                eating = dict_['Eating'],
                foraging = dict_['Foraging'],
                other_activities = dict_['Other Activities'],
                kuks = dict_['Kuks'],
                quaas = dict_['Quaas'],
                moans = dict_['Moans'],
                tail_flags = dict_['Tail flags'],
                tail_twitches = dict_['Tail twitches'],
                approaches = dict_['Approaches'],
                indifferent = dict_['Indifferent'],
                runs_from = dict_['Runs from'],
                ))

         Sighting.objects.bulk_create(squirrel_data)

