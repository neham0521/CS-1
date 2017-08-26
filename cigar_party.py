import sys
import datetime
while True:
	try:
		Cigar = int(float(input('Enter the number of cigars')))
	except:
		print('Enter a numeric value for Cigars')
		continue
	else:
		break	

if (datetime.datetime.today().weekday() in ('5','6')):
	if Cigar >= 40:
		print('CigarParty(',Cigar,', True) True')
	else:
		print('CigarParty(',Cigar,', True) False')
else:
	if 40 <= Cigar <= 60:
		print('CigarPart(', Cigar, ', False) True')
	else:
		print('CigarPart(', Cigar, ', False) False')
sys.exit()