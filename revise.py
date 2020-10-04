num=int(input ("enter the no:"))
for x in range(1,11):
    tab=num*x
    print(num,"*",x,tab)

raws=int(input("enter the no:"))

for r in range (1,raws+1):
    for c in range(1,r+1):
        print("*",end=" ")
        print()


