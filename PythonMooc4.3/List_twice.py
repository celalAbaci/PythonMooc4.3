list=[]
bool=True
while bool:
    a1=int(input("enter number :"))
    if a1==0:
        print("bye!")
        break
    else:
        list.append(a1)
        print(f"list is :  {list}")
        print("sıralı liste : " , end="")
        print(sorted(list))