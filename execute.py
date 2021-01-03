import os

os.system("date")
os.system("wget https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv")
os.system("csvgrep -c 1 -m US Global_Mobility_Report.csv > filtered.csv")
os.system("sudo python3 main.py")
os.system("python3 mainpagemap.py")
os.system("python3 usgenerator.py")
os.system("sudo service apache2 restart")
os.system("rm Global_Mobility_Report.csv")
os.system("rm filtered.csv")
os.system("curl -X POST https://maker.ifttt.com/trigger/refresh_completed/with/key/pFZnCr7wPDPkWd4beiAhV7DbyijBuvPUfArve3_Eoha")

