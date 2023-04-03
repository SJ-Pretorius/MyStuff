#1.1 Prompts user for total eggs
egg = int(input('How many eggs would you like to order? '))

#1.2 Calculates the number of dozens and loose eggs
dozen = egg // 12
loose = egg % 12

#1.3 Sets prices and calculates total costs
dozen_price = 3.25
loose_price = 0.45
total= (dozen * dozen_price)+(loose * loose_price)

#1.4 Displays total prize with breakdown of dozen and loose eggs
print(f"You ordered {egg} eggs. That's {dozen} dozen at R3.25 per dozen and {loose} eggs at 45c each for a total of R{total}.")