stringRevertida = "23511011501782351112179911801562340161171141148"[::-1] 
stringcaracter = ""
num = 0 

for c in stringRevertida:  
  num = (num * 10) + int(c)
  if num >= 65:
      if num <= 122:
         
        stringcaracter = stringcaracter + chr(num)
        num=0
    
  elif (num) == 32:
        stringcaracter = stringcaracter + chr(32)
        num= 0      
    
print(stringcaracter)