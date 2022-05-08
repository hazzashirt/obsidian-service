from importlib import import_module


import os
import subprocess
from datetime import datetime
print(datetime.today())

command = 'gcalcli --calendar "Calendar" agenda --details all --tsv --nodeclined  --client-id=742044796558-il3kfgccsmhm5lppapofos65383rrsqc.apps.googleusercontent.com --client-secret=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'
args = command.split(' ')
result = subprocess.run(['gcalcli', 'agenda', '--calendar "Calendar"'], stdout = subprocess.PIPE)
result.stdout.decode('utf-8')

#calendar_raw = os.system('gcalcli --calendar "Calendar" agenda --details all --tsv --nodeclined  --client-id=742044796558-il3kfgccsmhm5lppapofos65383rrsqc.apps.googleusercontent.com --client-secret=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')
#events = calendar_raw.split('\n')/
#print(events)
#subprocess.Popen('gcalcli --calendar "Calendar" agenda --details all --tsv --nodeclined  --client-id=742044796558-il3kfgccsmhm5lppapofos65383rrsqc.apps.googleusercontent.com --client-secret=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')
