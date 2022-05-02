
Alice = int(input('Zerinho ou um, Alice: '))
Beto = int(input('Zerinho ou um, Beto: '))
Clara = int(input('Zerinho ou um, Clara: '))

if Alice != Beto and Alice != Clara:
    print('A')
    
elif Beto != Alice and Beto != Clara:
    print('B')

elif Clara != Alice and Clara != Beto:
    print('C')
    
else:
    print('*')
