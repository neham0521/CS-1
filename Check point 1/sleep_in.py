
Day= input('Please enter what day it is').lower()
Vacation = input('Are you on vacation-please enter yes/no').lower()
#weekday[] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday']

if (Day == 'saturday' or Day == 'sunday'):
	print('You can sleep_in!')
elif Vacation == 'yes':
	print('you can Sleep_in!')
else:
	print('You can not sleep_in!')