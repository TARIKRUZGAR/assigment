
prime_number = []
for i in range (2,101):
    flag = True
    for a in range (2,i):
        if i %a ==0:
            flag=False

    if flag:
        prime_number.append(i)    

print("dcf",prime_number)


