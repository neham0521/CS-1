str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
l=len(str)
value = (str[colon+1:]).strip()
print('Float_value:',float(value))
