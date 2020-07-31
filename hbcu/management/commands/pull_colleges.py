import csv, sys
from hbcu.models import College
from django.core.management.base import BaseCommand

class Command(BaseCommand):
   def handle(self, *args, **kwargs):
    with open('schools.csv','r') as csvfile:
        reader= csv.reader(csvfile)
        for row in reader:
          College.objects.create(name=row[0],city=row[2],state=row[3])
    
    print("Done!")