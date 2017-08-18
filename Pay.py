try:
	hours = int(input('hours'))
	rate=int(input('rate'))
	if hours <= 40:
		print('Pay=',hours*rate)
	if hours > 40:
		extrahours = hours - 40
		print('extrahours =',extrahours)
		extrapay = extrahours*rate*1.5
		pay = ((hours-extrahours)*rate) + extrapay
		print('Pay=',pay)
except:
	print('please enter a numeric input')
#Ques: I want to again prompt the user for input - not sure how.
