fname = input('Enter file name')
try:
	fhand = open(fname)
except:
	print('File not found:',fname)
	quit()
for x in fhand:
	print(x.upper())