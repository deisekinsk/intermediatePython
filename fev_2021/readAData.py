data = input("Insert a data: ")

print(
    "\n",
    "O tipo primitivo é:", type(data),"\n",
    "Só tem espaços?", data.isspace(),"\n",
    "É numérico?", data.isnumeric(), "\n",
    "É alfabético?", data.isalpha(), "\n",
    "É alfanumérico?", data.isalnum(), "\n",
    "Está em maiúscula", data.isupper(), "\n",
    "Está em minúscula", data.islower(),"\n", 
    "Está Capitalizada?", data.istitle(), "\n", "\n",


)