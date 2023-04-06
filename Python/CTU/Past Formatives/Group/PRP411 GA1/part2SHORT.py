word=input('Please input a word or phrase: ')
if word.lower()[0:int(len(word)/2)] == word.lower()[::-1][0:int(len(word)/2)]:
    x=(f"{word.capitalize()} is a palindrome!")
else:
    x=(f"{word.capitalize()} is not a palindrome!")
print('-'*len(x))
print(x)
print('-'*len(x))