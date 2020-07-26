from celery import shared_task
from celery.signals import worker_ready
from .models import Discipline, Position
from .models import Employee, Client, Region, Site, DayRate
from .models import Rate, Equipment, EquipmentCharge, ManHoursCharge
from .models import RateSheet, Worklog, Dispute



mechanical = "mechanical"
electrical = "electrical"
electrician = "electrician" 
welder = "welder"
client = "client"
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
rates_ = "rates"
hours = "hours"
employee = "employee"
worklog = "worklog"
notes = "notes"


disciplines = [
   mechanical,
   electrical
]

positions = [
   {
      name: electrician,
      discipline: disciplines[1]
   },
   {
      name: welder,
      discipline: disciplines[0]
   }
]

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
      clients_: clients,
      region: regions[0]
   },
   {
      name: site2,
      lat: -47.903,
      lon: 74.523,
      clients_: clients,
      region: regions[1]
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
      number: 1,
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
      rates_: rates
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

manhourscharges = [
   {
      hours: 8,
      employee: employees[0],
      position: positions[0],
      worklog: worklogs[0]  
   },
   {
      hours: 4,
      employee: employees[0],
      position: positions[1],
      worklog: worklogs[0]  
   },
]

equipmentcharges = [
   {
      hours: 4,
      equipment_: equipment[0],
      worklog: worklogs[0]
   },
   {
      hours: 4,
      equipment_: equipment[1],
      worklog: worklogs[0]
   },
]


disputes = [
   {
      worklog: worklogs[0],
      summary: 'wrong hours at site a',
      notes: 'test employee charged one too many hours',
      employee: employees[0]
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
      print(f"adding position {pos}")
      Position(
         name=pos[name],
         discipline=Discipline.objects.filter(name=pos[discipline]).first()
      ).save()

   for c in clients:
      print(f"adding client {c}")
      Client(name=c).save()

   for reg in regions:
      print(f"adding region {reg}")
      rg = Region(
         name=reg
      )
      rg.save()
      for c in Client.objects.all():
         rg.clients.add(c)
      # rg.save()
   
   for i, s in enumerate(sites):
      print(f"adding site {site}")
      st = Site(
         name=s[name],
         lat=s[lat],
         lon=s[lon],
         region=Region.objects.filter(name=s[region]).first()
      )
      st.save()
      
      for c in s[clients_]:
         st.clients.add(Client.objects.filter(name=c).first())

   for eqp in equipment:
      Equipment(
         name=eqp[name],
         number=eqp[number],
      ).save()

   for dr in dayrates:
      DayRate(
         name=dr[name],
         cur_token=dr[cur_token],
         cur_per_day=dr[cur_per_day],
         equipment=Equipment.objects.filter(number=dr[equipment_][number]).first()
      ).save()

   for r in rates:
      Rate(
         name=r[name],
         cur_token=r[cur_token],
         cur_per_hr=r[cur_per_hr],
         ot_cur_per_hr=r[ot_cur_per_hr],
         position=Position.objects.filter(name=r[position]).first(),
      ).save()
      
   for e in employees:
      Employee(
         name=e[name],
         number=e[number],
         email=e[email],
         position=Position.objects.filter(name=e[position]).first(),
         discipline=Discipline.objects.filter(name=e[discipline]).first()
      ).save()

   for r in ratesheets:
      rs = RateSheet(
         name = r[name],
         client = Client.objects.filter(name=r[client]).first(),
         region = Region.objects.filter(name=r[region]).first(),
      )
      rs.save()

      for rate in r[rates_]:
         rs.rates.add(Rate.objects.filter(name=rate[name]).first())

      for drate in r[day_rates]:
         rs.day_rates.add(DayRate.objects.filter(name=drate[name]).first())

   
   wl = Worklog(
      summary= worklogs[0][summary],
      client= Client.objects.filter(name=worklogs[0][client]).first(),
      site = Site.objects.filter(name=worklogs[0][site][name]).first(),
      approved = worklogs[0][approved],
      disputed = worklogs[0][disputed]
   )
   wl.save()
   

   for m in manhourscharges:
      mc = ManHoursCharge(
         hours = m[hours],
         employee = Employee.objects.filter(name=m[employee][name]).first(),
         position = Position.objects.filter(name=m[position][name]).first(),
         worklog = wl
      )
      mc.save()

   for e in equipmentcharges:
      ec = EquipmentCharge(
         hours = e[hours],
         equipment=Equipment.objects.filter(name=e[equipment_][name]).first(),
         worklog = wl
      )
      ec.save()

   
   for d in disputes:
      ds = Dispute(
         worklog = wl,
         summary = d[summary],
         notes= d[notes]
      )
      ds.save()

      ds.manhours_charges.add(ManHoursCharge.objects.filter(employee__name=d[employee][name], hours=8).first())

   