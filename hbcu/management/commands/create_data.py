import csv, sys
from django.core.management.base import BaseCommand
from hbcu.models import College, Major, Degree, State

DEGREES = [
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

MAJORS = [
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

class Command(BaseCommand):
   def handle(self, *args, **kwargs):
     for major in MAJORS:
        Major.objects.get_or_create(name=major)
     for degree in DEGREES:
        Degree.objects.get_or_create(name=degree)
     College.objects.all().delete()
     with open('HBCUdata.csv','r') as csvfile:
        reader= csv.reader(csvfile)
        # reads one line and throws it away
        next(reader)
        for row in reader:
          name = row[0]
          url = row[1]
          majors_names = row[2].split('; ')
          degrees_names = row[3].split('; ')
          city = row[4]
          state_name = row[5]
          state, created=State.objects.get_or_create(name=state_name)
          # print(name, url, majors)
          technology = row[6].split('; ')
          financial_aid = row[7].split('; ')
          logo = row[8]
          campus_image = row[9]
          # virtual_tour = row[11]
          history = row[15]

          college = College.objects.create(
            name=name,
            url=url,
            city=city,
            state=state,
            technology=technology,
            financial_aid=financial_aid,
            logo=logo,
            campus_image=campus_image,
            # virtual_tour=virtual_tour,
            history=history,
            )
          for major in Major.objects.filter(name__in=majors_names):
            college.majors.add(major)
          for degree in Degree.objects.filter(name__in=degrees_names):
            college.degrees.add(degree)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))

     print("done!")





