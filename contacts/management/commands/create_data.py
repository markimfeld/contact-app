from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from contacts.models import Contact

import random
import datetime



categories = [
    'FR',
    'FY',
    'CO',
    'OR'
]

numbers = [
    4745553004,
    4759555463,
    4759555229,
    4759555535,
    4795551074,
    4795559062,
    4795551346,
    4795552036,
    4745557358,
    4759555689,
    4795552631,
    4759555634,
    4795552961,
    4795558928,
    4795553044,
    4745551396,
    4795556371,
    4759555670,
    4759555854,
    4759555665,
    4795552038,
    4795551261,
    4745551141,
    4759555414,
    4759555568,
    4759555370,
    4795553885,
    4745553302,
    4795552823,
    4759555841,
    4745557300,
    4759555125,
    4795553813,
    4759555939,
    4759555514,
    4795551023,
    4759555335,
    4759555115,
    4745553335,
    4759555952
]

addresses = [
    '6 Brandywine Drive Montgomery, NY 12549',
    '534 Bridgeway Dr. Chase Mills, NY 13621',
    '625 Timber Court Amityville, NY 11708',
    '20 N. St Louis Ave. Syracuse, NY 13218',
    '8321 Wintergreen Drive New York, NY 101',
    '599 New Castle Street Brookhaven, NY 11',
    '7907 E. Champion Lane East Randolph, NY',
    '54 Bald Hill Street Walker Valley, NY 1',
    '21 Leeton Ridge Street Portville, NY 14',
    '9634 Riverside Drive Islip Terrace, NY ',
    '768 New Street New York, NY 10160',
    '221 Bishop St. Silver Lake, NY 14549',
    '3 Mammoth St. Glen Spey, NY 12737',
    '568 W. Spring Street Cooperstown, NY 13326',
    '805 West Country Lane Bronx, NY 10470',
    '8780 Edgemont Street Keene Valley, NY 12943',
    '7376 Rocky River Drive Caroga Lake, NY 12032',
    '11 Pennington Road Rensselaer, NY 12144',
    '395 Petal St. Inlet, NY 13360',
    '734 Old Poplar St. Palisades, NY 10964',
    '9056 East Bloomfield St. Huntington, NY 11743',
    '9757 Virginia Avenue Star Lake, NY 13690',
    '598 West Linden St. Poplar Ridge, NY 13139',
    '9497 National Street Woodstock, NY 12498',
    '741 W. Cave Road Buffalo, NY 14204',
    '12 Clove Lane Getzville, NY 14068',
    '9934 Knight Lane Mallory, NY 13103',
    '606 Coral Drive Elmira, NY 14901',
    '124 Berkshire Ave. Liberty, NY 12754',
    '32 Grand Street Marilla, NY 14102',
    '69 Station St. Bellport, NY 11713',
    '315 Fairground Ave. Hartwick, NY 13348',
    '9897 North Inverness St. Buffalo, NY 14214',
    '100 Trusel Lane Rochester, NY 14639',
    '7553 Barley Road Monroe, NY 10949',
    '134 South Lafayette Lane Congers, NY 10920',
    '8713 Selby Drive Otto, NY 14766',
    '8965 Duchess Ave. Cape Vincent, NY 13618',
    '960 Law Avenue Wainscott, NY 11975',
    '484 Harvard St. Delhi, NY 13753'
]

jobs = [
    'Plumber',
    'Housekeeper',
    'Telemarketer',
    'Medical Secretary',
    'Cashier',
    'Economist',
    'Economist',
    'Software Developer',
    'Computer Programmer',
    'Computer Systems Analyst',
    'Court Reporter',
    'Systems Analyst',
    'Chemist',
    'Radiologic Technologist',
    'Customer Service Representative',
    'Painter',
    'Cost Estimator',
    'Massage Therapist',
    'Carpenter',
    'Veterinarian'
]

names = [
    'Talya',
    'Veronika',
    'Ralph',
    'Sylvester',
    'Lyuba',
    'Anna',
    'Alana',
    'Iara',
    'Alfher',
    'Maja',
    'Achab',
    'Borko',
    'Seppo',
    'Prince',
    'Gilberta',
    'Lumír',
    'Muriel',
    'Tuana',
    'Dezső',
    'Prokhor',
    'Agnes',
    'Alex',
    'Gregorios',
    'Nello',
    'Aristaeus',
    'Silvija',
    'Charlize',
    'Nettuno',
    'Xun',
    'İskender',
    'Benedetto',
    'Silvanus',
    'Bonifacy',
    'Nanuq',
    'Grid',
    'Ade',
    'Jan',
    'Shadi',
    'Diamanto',
    'Euterpe'
]

emails = [
    'generate+louisharris63@gmail.com',
    'generate+malcolmealy54@gmail.com',
    'generate+xzavierviana22@gmail.com',
    'generate+clayhadder28@gmail.com',
    'generate+saigegagnon63@gmail.com',
    'generate+ryleighshawn07@gmail.com',
    'generate+georgeharber24@gmail.com',
    'generate+avajackowski38@gmail.com',
    'generate+tylercaffee31@gmail.com',
    'generate+aniyaharris32@gmail.com',
    'generate+cierraabelson03@gmail.com',
    'generate+rubybacon09@gmail.com',
    'generate+karissacampbell83@gmail.com',
    'generate+addisonphillips32@gmail.com',
    'generate+emilyviana96@gmail.com',
    'generate+louislee66@gmail.com',
    'generate+richardurick41@gmail.com',
    'generate+kevinparker35@gmail.com',
    'generate+gavintabbert52@gmail.com',
    'generate+raymondturner26@gmail.com',
    'generate+timothylee60@gmail.com',
    'generate+hollyroberts01@gmail.com',
    'generate+sophiawhite59@gmail.com',
    'generate+essenceurick49@gmail.com',
    'generate+jazlynnwaggett40@gmail.com',
    'generate+jaydenking18@gmail.com',
    'generate+dixiecabler58@gmail.com',
    'generate+emmanuelrobinson03@gmail.com',
    'generate+jamesxavier48@gmail.com',
    'generate+jimmywilson76@gmail.com',
    'generate+ethengabbert78@gmail.com',
    'generate+taylortaylor52@gmail.com',
    'generate+reaganmartinez03@gmail.com',
    'generate+brentonharris89@gmail.com',
    'generate+annagonzalez08@gmail.com',
    'generate+jaydenraisner39@gmail.com',
    'generate+rubyurick77@gmail.com',
    'generate+dixiedahn33@gmail.com',
    'generate+davidcarter62@gmail.com',
    'generate+leonelallen77@gmail.com'
]

def generate_name():
    index = random.randint(0, 39)
    return names[index]

def generate_phone_number():
    index = random.randint(0, 39)
    return numbers[index]

def generate_address():
    index = random.randint(0, 39)
    return addresses[index]

def generate_category():
    index = random.randint(0, 3)
    return categories[index]

def generate_job():
    index = random.randint(0, 19)
    return jobs[index]

def generate_email():
    index = random.randint(0, 39)
    return emails[index]

def generate_date_created():
    year = random.randint(2000, 2030)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for c in range(0,40):
            contact = Contact(
                first_name = generate_name(),
                phone_number = generate_phone_number(),
                email = generate_email(),
                category = generate_category(),
                job = generate_job(),
                address = generate_address(),
                city = 'New York',
                country = 'United States',
                created = generate_date_created(),
                user = User.objects.get(pk=1)
            )

            contact.save()

        self.stdout.write(self.style.SUCCESS('Data created successfully'))
