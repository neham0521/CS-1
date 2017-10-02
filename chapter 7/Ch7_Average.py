fname = input('Enter file name')
try:
	fhand = open(fname)
except:
	print('File not found:',fname)
	quit()
len = len('X-DSPAM-Confidence:')
count=0
value =0
for x in fhand:
	if x.startswith('X-DSPAM-Confidence:'):
		count = count+1
		value = value + float(x[len:].strip())
#print(count,value)
print('Average spam confidence:',value/count)