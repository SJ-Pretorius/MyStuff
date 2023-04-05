#3.1 Function to generate two random numbers
def randomNum():
    import random
    a=random.randint(1,10)
    b=random.randint(1,10)
    return a,b

#3.2 Function to prompt the player for the answer
def userPrompt(x,y): #X=num1 Y=num2
    print(f'What is the product of {x} and {y}?')
    a=int(input(f'What is {x} x {y}? '))
    return a #a=user input

#3.3 Function to check if answer is correct
def answerCheck(a,x,y): #a=user input, X=num1 Y=num2
    ans = x*y
    if a == ans:
        check = True
    else:
        check = False
    return ans,check #ans=Correct answer, check=True/False if user answered correctly

#3.4 Function to start the game
def play_game():
    score = 0
    print()
    print(f"Let's play a multiplication game!")
    while True:
        num1,num2 = randomNum() #Gets the numbers
        print()
        user = userPrompt(num1,num2) #Prompts the user for answer
        answer,correct = answerCheck(user,num1,num2) #Check if answer is correct
        #Score system
        if correct == True:
            score += 1
            print(f'Correct! Your score is {score}')
        elif correct == False:
            print(f'Incorrect! The answer was {answer}, your score remains at {score}')
        #Play again
        again = input(f'Do you want to play again? (y/n) ')
        if again == "y" or  again == "Y":
            continue
        else:
            break

#3.5 Call the play_game function and let the fun begin!
play_game()