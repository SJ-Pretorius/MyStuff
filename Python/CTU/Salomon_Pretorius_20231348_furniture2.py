#Melissa approved!
def choice():
    wood = int(input('Pick 1 for pine, 2 for oak or 3 for mahogany: '))
    if wood == 1:
        cost = 100
        print('You chose a pine table which costs R100.')
    elif wood == 2:
        cost = 250
        print('You chose an oak table which costs R250.')
    elif wood == 3:
        cost = 350
        print('You chose a mahogany table which costs R350.')
    else:
        cost = 0
        print('You chose nothing or invalid code which costs R0.')
    return cost

def size(pay):
    size_pay = int(input('Large table (1) or Small table (2): '))
    if size_pay == 1:
        pay += 40
        print('Large selected!')
    elif size_pay == 2:
        print('Small selected!')
    else:
        print('Invalid size! Defaulting to small!')
    return pay

print()
price=choice()
if price == 0:
    final_price = 0
else:
    print()
    final_price = size(price)
print()
#print('Final price is R'+str(final_price)+'.')
print(f'Final price is R{final_price}.')
print()