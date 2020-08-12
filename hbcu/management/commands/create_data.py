import csv, sys
from django.core.management.base import BaseCommand
from hbcu.models import College, Major, Degree

degrees= [
  'Advance Short-Term Certificate (AC)',
  'Associate of Arts (AA)',
  'Associate of Applied Science (AAS)',
  'Associate of Science (AS)',
  'Bachelor of Art (BA)',
  'Bachelors in Business Administration (BBA)',
  'Bachelor of Fine Art (BFA)',
  'Bachelor of Science (BS)',
  'Bachelor of Science in Clinical Laboratory Science (BSCLS)',
  'BS Accelerated (BSA)',
  'Bachelor in Nursing (BSN)',
  'Bachelor in Social Work (BSW)',
  'Career Certificate (CC)',
  'Certificate of Technical (CT)',
  'Doctor of Chiropractic (DC)',
  'Doctor of Nursing Practice (DNP)', 
  'Doctor of Philosophy (PhD)',
  'Doctor of Physical Therapy (DPT)', 
  'Educational Doctorate (EdD)',
  'Educational Specialist (EdS)', 
  'Masters of Architecture (MArch)',
  'Masters of Art (MA)',
  'Master of Business (MBA)',
  'Master of Divinity (MDiv)',
  'Masters of Education (MEd)', 
  'Master of Fine Art (MFA)',
  'Masters in Public Administration (MPA)', 
  'Masters of Science (MS)',
  'Master in Social Work (MSW)',
  'Masters of Arts in Teaching (MAT); Online – AA',
  'Online – AS',
  'Online – BA',
  'Online – BS',
  'Online – Certificate', 
  'Online – MA',
  'Online – MBA',
  'Online – MEd',
  'Online – MS', 
  'Online - PhD',  
  'Post-Masters Certificate (PMC)',

]

majors = [
  'Accounting',
  'Biology',
  'English',
  'Mathematics',
  'Chemistry',
  'Computer Science',
  'History',
  'Art',
]



# class CommandTwo(BaseCommand):

#   def add_arguments(self, parser):
#       parser.add_argument('hbcu3', type=str, help='This is the json file that contains colleges')

#   def handle(self, *args, **kwargs):
#     hbcu3 = kwargs ['hbcu']
#     with open(f'{hbcu3}.json') as file:
#         for row in file:
#           name = row
#           major
#           degree
#           state
#           virtual_tour

class CommandTwo(BaseCommand):
   def handle(self, *args, **kwargs):
    with open('HBCUdata.csv','r') as csvfile:
        reader= csv.reader(csvfile)
        for row in reader:
          College.objects.create(
            name=row[0],
            major=row[2],
            degree=row[3],
            city=row[4],
            state=row[5],
            virtual_tours=[11],
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

print("done!")





