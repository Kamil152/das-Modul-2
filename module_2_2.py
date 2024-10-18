first = int(input('enter the first number: '))
second = int(input('enter the second number: '))
third = int(input('enter the third number: '))
if first != second and first != third and second != third :
    print('0')
elif first == second and second == third:
    print('3')
else:
    print('2')
    
    
    # if first != second and first != third and second != third :  Второй вариант решения задачи
    #    print('0')
    # elif first == second and second == third:
    #    print('3')
    # else:
    #   if first == second or first == third or second == third :
    #        print('2')

