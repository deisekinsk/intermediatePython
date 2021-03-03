#contador range, divisível por 3 e 5, ou por 3 ou pr 5. usando as três condições do range (a, b, c). a= começa em a; b= termina antes de b; c= a + c


n = 15 #int(input())

for x in range(1, n, 2):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
