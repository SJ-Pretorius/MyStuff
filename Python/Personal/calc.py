print()
while True:
    #Takes the first number
    num1 = (input('Type the initial number: '))
    #Check if the number is valid
    if num1.isdigit() == False:
        print()
        print('Only use digits from 0-9!')
        print()
        continue
    else:
        print()
        #Takes the action
        act = input('Type the operator: ')
        #Check if action is valid
        while True:
            if act == '*' or act == '+' or act == '-' or act == '/' or act == 'x' or act == '%':       
                print()
                #Takes second number
                num2 = (input('Type the number to manipulate with: '))
                #Check if number is valid
                if num2.isdigit() == False:
                    print()
                    print('Only use digits from 0-9!')
                    continue
                else:
                #Calculate result from act num1 num2
                    print()
                    if act == '*' or act == 'x':
                        ans = int(num1) * int(num2) 
                    elif act == '+':
                        ans = int(num1) + int(num2)
                    elif act == '-':
                        ans = int(num1) - int(num2)
                    elif act == '/' or act == '%':
                        if num2 == '0': #Detects devision by 0
                            print('Cannot divide by 0!')
                            continue
                        else:
                            ans = int(num1) / int(num2)
                #Prints result
                print('--------------------------')
                print('Answer is ' + str(ans) + '!')
                print('--------------------------')
                print()
                #Optional repeat feature / exit
                num1 = ans
                act = input('Type the operator (Clear / Exit also accepted here): ')
                if act == 'Exit' or act == 'exit':
                    print()
                    print("Thank You!")
                    print()
                    exit()
                elif act == 'Clear' or act == 'clear':
                    num1 = 0
                    print()
                    print('--------------------------')
                    print('Answer is 0!')
                    print('--------------------------')
                    print()
                    act = input('Type the operator: ')
                    continue
                else:
                    continue
            else:
                #Part of action validity test
                print()
                print('Invalid Operator!')
                print()
                act = input('Type the operator: ')
                continue