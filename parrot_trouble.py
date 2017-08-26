import sys
import time
while True:
	P_talking = input('Is the parrot talking(y/n)').lower()
	if P_talking not in ('y','n'):
		print('Please enter only Y or N')
		continue
	else:
		break
if P_talking == 'n':
	print('False: You are safe')
else:
	if (int(time.strftime('%H')) < 7 or int(time.strftime('%H')) > 20):
	#hour = int(input('enter current hour'))
	#if (hour < 7 or hour > 20):
		print('True: you are in trouble!')
	sys.exit()
