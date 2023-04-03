# Please enter pin to execute program
# pin1=1234 pin2=5678
print()
x=input('Type pin1: ')
y=input('Type pin2: ')

a='1234'
b='5678'

if x == a:
    if y == b:
        print()
        print('Both are Correct!')
    else:
        print()
        print('Pin2 is wrong!')
        exit()
elif y == b:
    print()
    print('Pin1 is wrong!')
    exit()
else:
    print()
    print('Both are Wrong!')
    exit()

print('Executing...')
print()

#Activity1
prince = 99
print(prince)
print(type(5)) #int
print(type(2.0)) #float
print(type(5+2.0)) #float