print()
#Type below this line

#Tuple
a_tuple = ('cat','dog','fish')
a,b,c = a_tuple
print(a)
print(b)
print(c)
print()

words = ('fresh','out','of','ideas')
for word in words:
    print(word)
print()

#Combine tuples
t1 = ('Cheese','Milk','Bread')
t2 = ('Butter',)
t1 += t2
print(t1)
print()

#Lists
list=['Cats','Dogs','Fishs']
print(list)
print(tuple(list))
print()

days = ['su','m','tu','w','th','f','sa']
print(f'{days[6]} {days[0]}')
print(days[1:6])
print()

#Append
ap = ['Meow','Woof']
add = ('fish')
print(ap)
ap.append(add)
print(ap)
print('+'.join(ap))
print(ap[2])
#del ap[2]
ap.remove('Woof')
print(ap)
ap.clear()
print(ap)
print()

a = [[1,2,3,4],[5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='')
        print()
print()

myList = []
for row in range(0,2):
    tempList=[]
    for column in range(0,3):
        tempList.append(int(input('Enter a number: ')))
    myList.append(tempList)
print(myList)

#Type above this line
print()