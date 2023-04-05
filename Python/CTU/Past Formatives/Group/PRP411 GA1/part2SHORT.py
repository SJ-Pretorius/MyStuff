word=input('Please input a word or phrase: ')
if word[0:int(len(word.lower())/2)] == word[::-1][0:int(len(word.lower())/2)]:
    x=(f"{word.capitalize()} is a palindrome!")
else:
    x=(f"{word.capitalize()} is not a palindrome!")
print('-'*len(x))
print(x)
print('-'*len(x))