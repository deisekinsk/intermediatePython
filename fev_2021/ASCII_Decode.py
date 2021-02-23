stringRevertida = "23511011501782351112179911801562340161171141148"[::-1] 
stringcaracter = "" 
num = "" 

for c in stringRevertida:  

    num = num + c; 
    
    if int(num) >= 65:
        if int(num) <= 122:
            valor = int(num) 
            stringcaracter = stringcaracter + chr(valor) 
            num="" 

    elif int(num) == 32:
          stringcaracter = stringcaracter + chr(32)
          num=""      
    
print(stringcaracter)