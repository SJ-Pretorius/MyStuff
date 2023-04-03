while True:
    print()
    choice = int(input('Pick 1 for pine, 2 for oak or 3 for mahogany: '))
    if choice == 1:
        print('You chose a pine table which costs R100')
    elif choice == 2:
        print('You chose an oak table which costs R250')
    elif choice == 3:
        print('You chose a mahogany table which costs R350')
    else:
        print('You chose nothing or invalid code which costs R0')