import os
os.system('pip install elevate')
from elevate import elevate
elevate(os.system('powershell.exe wininit'))

