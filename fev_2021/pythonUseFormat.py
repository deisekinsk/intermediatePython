#Saída formatada que usa as 'chaves'
var = input("Qual é o seu nome: ")
print("Muito prazer {}!".format(var))

#Soma com entrada de valores
num1 = input("Fale um número: ")
num2 = input("Fale o segundo número: ")
soma = int(num1) + int(num2) #lembrar de converter

print("A soma entre {} e {} é {}!".format(num1, num2, soma))