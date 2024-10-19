#while 100:
#    a = int(100)
#    number = int(input('Enter a number: '))
#    if number % 2 == 0:
#        print('This is an even number')
#    else:
#       print('This is an odd number')
#        a = a - number
#        break

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while len(my_list) > index:
    if my_list[index] < 0:
        break
    if my_list[index] > 0:
        print(my_list[index])
    index +=1