import os

os.system("python3 mainpagemap.py")
os.system("python3 usgenerator.py")
os.system("python3 main.py")
os.system("sudo service apache2 restart")
os.system("curl -X POST https://maker.ifttt.com/trigger/refresh_completed/with/key/pFZnCr7wPDPkWd4beiAhV7DbyijBuvPUfArve3_Eoha")