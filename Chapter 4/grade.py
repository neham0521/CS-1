import sys

def computegrade(score):
	try:
		score = float(score)
	except:
		return 'badscore'
	if 0 <= score <=1:
		if score >= 0.9:
			return 'A'
		elif score >=0.8:
			return 'B'
		elif score >=0.7:
			return 'C'
		elif score >=0.6:
			return 'D'
		else:
			return 'F'
	else:
		return 'badscore'

print('Grade: ', computegrade(0.95))
print('Grade: ', computegrade('perfect'))
print('Grade: ', computegrade(10.0))
print('Grade: ', computegrade(0.75))
print('Grade: ', computegrade(0.5))
