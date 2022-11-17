n=input("Enter the string")
flag=0
for i in n:
    for j in n:
        if(i==j):
            flag=flag+1
    print(i,"is found ",flag,"times")
    flag=0