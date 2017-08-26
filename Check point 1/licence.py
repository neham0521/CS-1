import sys
try:
	age = float(input('Enter your age'))
	practice_hours = float(input('Enter number of practise hours'))
except: 
	print('Error: Enter a numeric value')
	sys.exit()
if age < 16:
	print('you do not qualify for a licence')	
else:
	if practice_hours >200: 
		print('Congrats! you are qualified for a licence. Licence will be mailed to your postal address within 7 business days')
	else:
		print('you do not qualify for a licence')	
sys.exit()
