user =['dave','jhon','sara']

data = ['dave' ,42, True]

emptylist = []

print("dave" in emptylist)

print(user[0])
print(user[-2])

print(user.index('sara'))

print(user[0:2])
print(user[1:])
print(user[-3:-1])

print(len(data))

user.append('Elsa')
print(user)

user += ['jason']
print(user)

user.extend(['Robert', 'jimmy'])
print(user)

#user.extend(data)
#print(user)
user.insert(0, 'Bob')
print(user)

user[1:3] = ['Robert','JPJ']
print(user)

user.remove('Bob')
print (user)

print(user.pop())
print(user)

del user[0]
print(user)

#del data
data.clear()
print(data)

user.sort(key=str.lower)
print(user)

num = [4, 42, 78, 1, 5]
num.reverse()
print(num)

#num.sort(reverse=True)
#print(num)

print(sorted(num, reverse=True))
print(num)

numscopy = num.copy()
mynum =list(num)
mycopy = num[:]

print(numscopy)
print(mynum)
mycopy.sort()
print(mycopy)
print(num)

print(type(num))

mylist = list([1, "neil", True])
print(mylist)

# Tuples

mytuple = tuple(('Dave' , 42,True))

anothertuple = (1, 4, 2, 8)

print (mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
