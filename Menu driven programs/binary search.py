lst=list(input("enter the list"))
key=int(input("enter the key"))
mid=0+int(len(lst))//2
print(mid)
if lst[int(mid)-1]==int(key):
    print("the number is at",mid,"th index")
else:
    print("hi")