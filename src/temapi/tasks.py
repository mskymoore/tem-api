from celery import shared_task
from celery.signals import worker_ready
from .models import EntryDate, Discipline, Position
from .models import Employee, Client, Region, Site, DayRate
from .models import Rate, Equipment, EquipmentCharge, ManHoursCharge



mechanical = "mechanical"
electrical = "electrical"
electrician = "electrician"
welder = "welder"
clientA = "clientA"
clientB = "clientB"
westtx = "west-texas-1"
dayrate = "dayrate"
southnm = "south-new-mexico-2"
name = "name"
lat = "lat"
lon = "lon"
clients_ = "clients"
client = "client"
number = "number"
dollars = "$"
site = "site"
site1 = "site1"
site2 = "site2"
cur_token = "cur_token"
cur_per_day = "cur_per_day"
summary = "summary"
day_rates = "day_rates"
ot_cur_per_day = "ot_cur_per_day"
cur_per_hr = "cur_per_hr"
ot_cur_per_hr = "ot_cur_per_hr"
equipment_ = "equipment"
position = "position"
discipline = "discipline"
approved = "approved"
disputed = "disputed"
email = "email"
region = "region"


disciplines = [
   mechanical,
   electrical
]

positions = {
   electrician: disciplines[1],
   welder: disciplines[0]
}

clients = [
   clientA,
   clientB
]


regions = [
   westtx,
   southnm
]


sites = [
   {
      name: site1,
      lat: -45.643,
      lon: 44.322,
      clients_: clients
   },
   {
      name: site2,
      lat: -47.903,
      lon: 74.523,
      clients_: clients
   }
]

equipment = [
   {
      name: 'test equipment',
      number: 1,
   },
   {
      name: 'other test equipment',
      number: 2,
   },
]

dayrates = [
   {
      name:'test day rate',
      cur_token: dollars,
      cur_per_day: 300.50,
      equipment_: equipment[0]
   },
   {
      name:'2 test day rate',
      cur_token: dollars,
      cur_per_day: 560.50,
      equipment_: equipment[0]
   },
   {
      name:'3 test day rate',
      cur_token: dollars,
      cur_per_day: 930.50,
      equipment_: equipment[1]
   },
]

rates = [
   {
      name: 'test rate',
      cur_token: dollars,
      cur_per_hr: 5,
      ot_cur_per_hr: 7.50,
      client: clientA,
      position: electrician,
      discipline: disciplines[1],
   },
   {
      name: '2 test rate',
      cur_token: dollars,
      cur_per_hr: 10,
      ot_cur_per_hr: 15,
      client: clientB,
      position: welder,
      discipline: disciplines[0],
   },
]

employees = [
   {
      'number': 1,
      position: electrician,
      discipline: disciplines[1],
      name: 'test employee',
      email: 'email@example.com'
   }
]


ratesheets = [
   {
      name: 'Client A west-texas-1',
      client: clients[0],
      region: regions[0],
      day_rates: dayrates,
      rates: rates
   },
]

worklogs = [
   {
      summary: 'an example worklog',
      client: clients[0],
      site: sites[0],
      approved: True,
      disputed: False
   },
]

equipmentcharges = [
   {
      client
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
         name=site[name],
         lat=site[lat],
         lon=site[lon],
         region=Region.objects.filter(name=westtx).first()
      )
      st.save()
      st.clients.add(Client.objects.filter(name=clientA).first())

   for dr in dayrates:
      DayRate(
         name=dr[name],
         cur_token=dr[cur_token],
         cur_per_day=dr[cur_per_day]
      ).save()

   for r in rates:
      Rate(
         name=r[name],
         cur_token=r[cur_token],
         cur_per_hr=r[cur_per_hr],
         ot_cur_per_hr=r[ot_cur_per_hr],
         client=Client.objects.filter(name=r[client]).first(),
         position=Position.objects.filter(name=r[position]).first(),
         discipline=Discipline.objects.filter(name=r[discipline]).first(),
         region=Region.objects.filter(name=r[region]).first()
      ).save()
      
   for e in employees:
      Employee(
         name=e[name],
         number=e[number],
         email=e[email],
         position=Position.objects.filter(name=e[position]).first(),
         discipline=Discipline.objects.filter(name=e[discipline]).first()
      ).save()

   for eqp in equipment:
      Equipment(
         name=eqp[name],
         number=eqp[number],
         dayrate=DayRate.objects.filter(name=eqp[dayrate]).first()
      ).save()