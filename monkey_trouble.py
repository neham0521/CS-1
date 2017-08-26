
while True:
	Monkey_a= input('Hey Monkey_a: Are you smiling(Y/N)').lower()
	if Monkey_a not in ('y','n'):
		print('Please enter only Y or N')
		continue
	else:
		break

while True:
	Monkey_b = input('Hey Monkey_b: Are you smiling(Y/N)').lower()
	if Monkey_b not in ('y','n'):
		print('Please enter only Y or N')
		continue
	else:
		break

if (Monkey_a == Monkey_b):
	print('You are in trouble!')
else:
	print('You are safe!')