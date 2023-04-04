def func1(word_list):
    total = 0
    for num in word_list:
        total += num
    return total

def func2(word_list):
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word), longest_word


def func3(norm_str):
    rev_str = norm_str[::-1]
    return rev_str

while True:
    print()
    main_list=[]
    while len(main_list)<=9:
        list_app=int(input(f'Please input a number ({10 - len(main_list)} remaining): '))
        main_list.append(list_app)
    sum_num=func1(main_list)
    x=(f'The total is {sum_num}!')
    print('-'*len(x))
    print(x)
    print('-'*len(x))
    again1=input(f'Do you want to try again? (Y or N): ')
    if again1 == "y" or again1 == "Y":
        continue
    break
while True:
    print()
    main_list=[]
    while len(main_list)<=9:
        list_app=(input(f'Please input a word ({10 - len(main_list)} remaining): '))
        main_list.append(list_app)
    len_word, long_word=func2(main_list)
    x=(f'The longest word {long_word} has a length of {len_word}!')
    print('-'*len(x))
    print(x)
    print('-'*len(x))
    again2=input(f'Do you want to try again? (Y or N): ')
    if again2 == "y" or again2 == "Y":
        continue
    break
while True:
    print()
    string=input(f'Please input a word to reverse: ')
    string_rev=func3(string)
    x=(f'The reverse for {string} is {string_rev}!')
    print('-'*len(x))
    print(x)
    print('-'*len(x))
    again3=input(f'Do you want to try again? (Y or N): ')
    if again3 == "y" or again3 == "Y":
        continue
    break