import sys
def computepay(hours,rate):
	if hours <= 40:
		return hours*rate
	else:
		return ( (40*rate) + ((hours-40)*rate*1.5))
	
while True:
	try:
		hours = int(input('hours'))
		rate=int(input('rate'))
	except:
		print('please enter a numeric input')
		continue
	else:
		break


print('Pay =',computepay(hours,rate))	
#Ques: I want to again prompt the user for input - This can be done by using while loop
