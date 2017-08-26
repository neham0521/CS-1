import sys
import datetime
#Birthdate = input('Enter your birthday in "YYYY-MM-DD" format')
while True:
	try:
		speed = float(input('Enter speed'))
	except:
		print('Enter speed in number')
		continue
	else:
		while True:
			try:
				Birthdate = input('Enter your birthday in "DD-MM" format')
				bd= datetime.datetime.strptime(Birthdate, '%d-%m')
			except:
				print('Incorrect format')
				continue
			else:
				break
		break
today = datetime.datetime.today()
if (bd.month == today.month and bd.day == today.day):
	#print(Birthdate)
	if speed <= 65:
		print('0')
	elif 66<=speed<=85:
		print('1')
	else:
		print('2')
else:
	if speed <= 60:
		print('0')
	elif 61<=speed<=80:
		print('1')
	else:
		print('2')
sys.exit()