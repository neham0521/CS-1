#test.py
import datetime

Actualday = int(datetime.datetime.today().weekday())
if 0 <= Actualday <= 5: 
	Day= Actualday+1
else:
	Day = 0
	
while True:
	Vac = input('Are you on vacation. [True/False]').lower()
	if Vac not in ('true','false'):
		print('Please enter only True/False')
		continue
	else:
		break

if Vac == 'true':
	if 1<= Day<=5:
		Print("'10:00'")
	else:
		print("'Off'")
else:
	if 1<=Day <= 5:
		Print("'7:00'")
	else:
		print("'10:00'")

