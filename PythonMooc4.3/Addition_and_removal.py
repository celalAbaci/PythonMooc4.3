list=[]

a1=1
bool=True
while bool:
    print(f" The list is now {list} ")
    a=input("a(d)d, (r)emove or e(x)it: ")

    if a=="d":
        list.append(a1)
        a1+=1
    elif a=="r":
        list.remove(a1-1)
        a1-=1
    elif a=="x":
        bool=False