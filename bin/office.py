#%% Env
from O365 import Account, MSGraphProtocol
import datetime as dt

CLIENT_ID = ""
SECRET_ID = ""

with open('client.key','r') as f:
    CLIENT_ID = f.read()
with open('secret.key','r') as f:
    SECRET_ID = f.read()
credentials = (CLIENT_ID, SECRET_ID)
#%% Auth
protocol = MSGraphProtocol('O365-Python') 
#protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>') 
scopes = ['Calendars.Read.Shared']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')

schedule = account.schedule()
calendar = schedule.get_default_calendar()
events = calendar.get_events(include_recurring=False) 
#events = calendar.get_events(query=q, include_recurring=True) 

for event in events:
    print(event)
#%% Get Schedule
#calendar = account.schedule
q = calendar.new_query('start').greater_equal(dt.datetime(2019, 11, 20))
q.chain('and').on_attribute('end').less_equal(dt.datetime(2019, 11, 24))