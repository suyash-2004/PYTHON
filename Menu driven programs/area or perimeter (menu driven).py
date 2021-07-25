# make a menu driven programme to find out area of perimeter of rectangle

# ch=1
# while ch==1:
#     print("1.area\n2.perimeter")
#     choice=int(input("enter your choice"))
#     if choice==1:
#         l=int(input("enter the length"))
#         b=int(input("enter the bredth"))
#         area=l*b
#         print(area)
#     elif choice==2:
#         l=int(input("enter the length"))
#         b=int(input("enter the breadth"))    
#         perimeter=2*(l+b)
#         print(perimeter)
#     else:
#         print("invalid choice")
#     ch=int(input("do u want to repeat??(1/2)")
# 

# wap to count the number of occurence of a character in an inputted string
string=input("enter the string")
search=input("what do u want to search")
count=0
for i in string:
    if i==search:
        count+=1
print(count)
    

