//Avanish.K.a

import random

a = str(input('Enter a value: '))

b = str(input('Enter a value: '))

c = str(input('Enter a value: '))

d = str(input('Enter a value: '))

e = str(input('Enter a value: '))

f = str(input('Enter a value: '))

g = str(input('Enter a value: '))

h = str(input('Enter a value: '))

i = str(input('Enter a value: '))

j = str(input('Enter a value: '))

k = str(input('Enter a value: '))

l = str(input('Enter a value: '))

data=[a,b,c,d,e,f,g,h,i,j,k,l]

x=random.choice(data)

y=random.choice(data)

z=random.choice(data)

m=x+y+z

n = (''.join(reversed(m)))

if(m==n):

    print("Palindrome")

else:

    print("Not a Palindrome")
    

    
