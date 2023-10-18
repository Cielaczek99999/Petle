n = int(input('podaj liczbe powtorzen'))

for i in range(10):  # range(0, n) - bez n
    print(i)


'''lista_liczb = []
q = int(input('ile liczb chcesz podać'))

for i in range('n'):
    x = int(input('Podaj kolejną liczbę'))
    lista_liczb.append(x)
    print(lista_liczb)

print(lista_liczb)'''

'''lista_liczb2 = [5, 10, 15, 20, 78]

for i in lista_liczb2:
    print(i + 2)
    lista_liczb2[j] = i + 2
    j = j + 1'''


'''for i in range(3, 101, 3):
        print(i)
        '''


'''lista_liczb3 = [1, 2, 3, 4, 5, 7, 8, 9]
for i in range(0, len(lista_liczb3), 2):
    print(lista_liczb3[0:len(lista_liczb3):2])'''


'''for x in range(3, 103, 3):
    #print(str(x) + '\t'+ str(x/2+3))
    print('{0}\t{1}'.format(x, x / 2+3))'''


#b)
x=-3.0
for i in range(100):
    print('{}\t{}' .format(x, x/2+3))
    x=x + 0.1





