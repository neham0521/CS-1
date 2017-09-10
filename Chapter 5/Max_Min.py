min = None
max = None
while True:
	i= input('Enter a number ')
	if i.lower() == 'done':
		break
	try:
		f=float(i)
	except:
		print('invalid input')
		continue
	if(min is None):
		min = f
	elif f < min:
		min = f
	if max is None:
		max =f
	elif f> max:
		max =f
print('Min =',min)
print('Max =',max)

	
