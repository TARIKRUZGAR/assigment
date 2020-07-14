fibonacci=[]

a=1
b=1
fibonacci.append(a)
fibonacci.append(b)
c=0
while c<55:
    c=a+b
    fibonacci.append(c)
    a=b
    b=c

print(fibonacci)
