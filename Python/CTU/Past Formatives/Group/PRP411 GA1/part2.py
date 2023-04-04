#User input for phrase or word and lower cases it
word=input('Please input a word or phrase: ')
word=word.lower()
#Determine the length of word/phrase to 'split' the word in halve
length=int(len(word)/2)
#Split the first halve from the word/phrase and set it in a variable
first=word[0:length]
#Reverse the word/phrase to get the second halve in the correct order
word_rev = word[::-1]
#Split the second halve from the word/phrase and set it in a variable
second=word_rev[0:length]
#Compare the two variables and see if it's the same
if first == second:
    x=(f"{word.capitalize()} is a palindrome!")
    print('-'*len(x))
    print(x)
    print('-'*len(x))

else:
    x=(f"{word.capitalize()} is not a palindrome!")
    print('-'*len(x))
    print(x)
    print('-'*len(x))