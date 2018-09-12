l = [19,-7,23,80,1,45,0,-99]  //Can be changed 
print(l)

n = len(l)

for i in range(n):

    for j in range(1, n-i):

        if l[j-1] < l[j]:

            (l[j-1],l[j]) = (l[j],l[j-1])

print(l)