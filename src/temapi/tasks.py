from celery import shared_task
from celery.signals import worker_ready
from .models import EntryDate, Discipline, Position
from .models import Employee, Client, Region, Site, DayRate
from .models import Rate, Equipment, EquipmentCharge, ManHoursCharge


disciplines = [
   'mechanical',
   'electrical'
]

positions = {
   'electrician': disciplines[1],
   'welder': disciplines[0]
}

clients = [
   'clientA',
   'clientB'
]


regions = [
   'west texas 1',
   'south new mexico 2'
]


sites = [
   {
      'name': 'site1',
      'lat': -45.643,
      'lon': 44.322,
      'clients': clients
   }
]

dayrates = [
   {
      'name':'test day rate',
      'cur_token': '$',
      'cur_per_day': 300.50
   }
]

rates = [
   {
      'name': 'test rate',
      'cur_token': '$',
      'cur_per_hr': 5,
      'ot_cur_per_hr': 7.50,
      'client': 'clientA',
      'position': 'electrician',
      'discipline': disciplines[1],
      'region': 'west texas 1'
   }
]

employees = [
   {
      'number': 1,
      'position': 'electrician',
      'discipline': disciplines[1],
      'name': 'test employee',
      'email': 'email@example.com'
   }
]

equipment = [
   {
      'name': 'test equipment',
      'number': 1,
      'dayrate': 'test day rate'
   }
]

@shared_task
def do_data_update():
   pass 


@worker_ready.connect
def load_example_data(sender=None, conf=None, **kwargs):

   for disc in disciplines:
      print(f"adding discipline {disc}")
      Discipline(name=disc).save()
   
   for pos in positions:
      Position(
         name=pos,
         discipline=Discipline.objects.filter(name=positions[pos]).first()
      ).save()

   for client in clients:
      print(f"adding client {client}")
      Client(name=client).save()

   for reg in regions:
      rg = Region(
         name=reg
      )
      rg.save()
      for c in Client.objects.all():
         rg.clients.add(c)
      # rg.save()
   
   for site in sites:
      st = Site(
         name=site['name'],
         lat=site['lat'],
         lon=site['lon'],
         region=Region.objects.filter(name='west texas 1').first()
      )
      st.save()
      st.clients.add(Client.objects.filter(name='clientA').first())

   for dr in dayrates:
      DayRate(
         name=dr['name'],
         cur_token=dr['cur_token'],
         cur_per_day=dr['cur_per_day']
      ).save()

   for r in rates:
      Rate(
         name=r['name'],
         cur_token=r['cur_token'],
         cur_per_hr=r['cur_per_hr'],
         ot_cur_per_hr=r['ot_cur_per_hr'],
         client=Client.objects.filter(name=r['client']).first(),
         position=Position.objects.filter(name=r['position']).first(),
         discipline=Discipline.objects.filter(name=r['discipline']).first(),
         region=Region.objects.filter(name=r['region']).first()
      ).save()
      
   for e in employees:
      Employee(
         name=e['name'],
         number=e['number'],
         email=e['email'],
         position=Position.objects.filter(name=e['position']).first(),
         discipline=Discipline.objects.filter(name=e['discipline']).first()
      ).save()

   for eqp in equipment:
      Equipment(
         name=eqp['name'],
         number=eqp['number'],
         dayrate=DayRate.objects.filter(name=eqp['dayrate']).first()
      ).save()