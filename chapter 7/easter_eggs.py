fname = input('Enter file name')
try:
	fhand = open(fname)
except:
	if fname.lower().strip() == 'na na boo boo':
		print("NA NA BOO BOO TO YOU - You have been punk'd!")
		quit()
	print('File not found:',fname)
	quit()
count = 0		
for x in fhand:
	if x.startswith('Subject') or x.startswith('subject'):
		count= count+1
print('There were',count,'subject lines in', fname)

