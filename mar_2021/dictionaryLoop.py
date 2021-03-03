#Get and dictionary

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}


a = 'Italy'

for x, y in data.items():
 
 if x == a:
  print(y)
   
 
 else:
 
  print ('Not found')
