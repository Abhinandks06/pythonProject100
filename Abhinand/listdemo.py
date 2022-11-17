list1=["apple","mango","banana"]
print(list1)
x=type(list1)
print(x)
list1[0]="grapes"
list1.insert(3,"orange")
for i in list1:
    print(i)
list1.remove("orange")
for i in list1:
    print(i)
    list1.pop()
    print(list1)
    list1.clear()
    print(list1)
