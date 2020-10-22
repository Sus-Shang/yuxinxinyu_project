import csv

import datetime

from django.core.management.base import BaseCommand
from squirrel.models import Sighting


class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        path = options['path']

        def makebool(x):
            if x.lower() == 'true':
                return 'True'
            else:
                return 'False'
        with open(path,'r') as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        squirrel_data=[]
        squirrel_id = []
        for dict_ in data:
            if dict_['Unique Squirrel ID'] in squirrel_id:
                    continue
            else:
                squirrel_data.append(Sighting(
                longitude = float(dict_['X']),
                latitude = float(dict_['Y']),
                unique_squirrel_ID = dict_['Unique Squirrel ID'],
                shift = dict_['Shift'],
                date = datetime.datetime.strptime(dict_['Date'],'%m%d%Y'),
                age = dict_['Age'],
                primary_fur_color = dict_['Primary Fur Color'],
                location = dict_['Location'],
                specific_location = dict_['Specific Location'],
                running =makebool(dict_['Running'].capitalize()),
                chasing =makebool( dict_['Chasing'].capitalize()),
                climbing =makebool( dict_['Climbing'].capitalize()),
                eating =makebool( dict_['Eating'].capitalize()),
                foraging =makebool(dict_['Foraging'].capitalize()),
                other_activities = dict_['Other Activities'],
                kuks =makebool( dict_['Kuks'].capitalize()),
                quaas =makebool( dict_['Quaas'].capitalize()),
                moans =makebool( dict_['Moans'].capitalize()),
                tail_flags =makebool( dict_['Tail flags'].capitalize()),
                tail_twitches =makebool( dict_['Tail twitches'].capitalize()),
                approaches =makebool(dict_['Approaches'].capitalize()),
                indifferent =makebool( dict_['Indifferent'].capitalize()),
                runs_from =makebool( dict_['Runs from'].capitalize()),
                ))
                squirrel_id.append(dict_['Unique Squirrel ID'])
        Sighting.objects.bulk_create(squirrel_data)

