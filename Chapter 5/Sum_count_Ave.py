total=0
count =0
while True:
	i= input('Enter a number ')
	if i.lower() == 'done':
		break
	try:
		f=float(i)
	except:
		print('invalid input')
		continue
	total = total+f
	count = count+1

print('Sum = ',total)
print('Count = ',count)
print('Average =',total/count)
