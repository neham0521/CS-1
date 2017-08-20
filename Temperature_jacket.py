import sys
try:
	temp_Celcius = float(input('Enter temperature in Celcius'))
except:
	print('Error: Enter a numeric value for temperature')
	sys.exit()
if temp_Celcius < 20:
	print('Bring a heavy Jacket!')
elif temp_Celcius >=20 and temp_Celcius<=30:
	print('Bring a light Jacket!')
else:
	print('Please do not bring any Jacket!')
