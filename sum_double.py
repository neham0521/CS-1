while True:
	try:
		num1 = int(float(input('Enter first number')))
	except:
		print('Enter a numeric value')
		continue
	else:
		while True:
			try:
				num2 = int(float(input('Enter second number')))
			except:
				print('Enter a numeric value')
				continue
			else:
				break
		break

if num1 == num2:
	sum = 2*(num1+num2)
else:
	sum = num1+num2
print('Sum =',sum)