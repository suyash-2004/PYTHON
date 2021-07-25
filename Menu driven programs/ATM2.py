import time
pin=1234
balance=100000
print("welcome")
print("enter your name")
a=input()
print("please wait.....")

if a=='suyash':
        time.sleep(2)
        print("enter your age")
        b=int(input())
        print("please wait.....")
        
        if b==17:
                time.sleep(2)
                print("enter your pin")
                c=int(input())
                print("please wait.....")
                if c==pin:
                        time.sleep(2)
                        print("welcome")
                        time.sleep(2)
                        print("enter your choice:")
                        time.sleep(0.5)
                        print('''1.check balance \t 2.withdraw cash \t 3.deposit cash''')
                        selection=int(input())
                        if selection==1:
                            time.sleep(1)
                            print("enter your pin again")
                            e=int(input())
                            if e==pin:
                                print("your current balance is:100000 ")
                                time.sleep(2)
                            else:
                                print("wrong pin")
                        elif selection==2:
                            time.sleep(1)
                            print("enter your pin again")
                            f=int(input())
                            if f==pin:
                                print("enter the ammount to be with drawn")
                                amount=int(input())
                                time.sleep(2)
                                print("amount succefully withdrawed")
                                time.sleep(1)
                                print("current balance is : ",balance-amount)
                                time.sleep(2)
                            else:
                                print("wrong pin")
                        elif selection==3:
                            time.sleep(1)
                            print("enter your pin again")
                            g=int(input())
                            if g==pin:
                                print("enter the amount to be deposited")
                                deposit=int(input())
                                print("submmit the cash in the slot and press the button")
                                time.sleep(2)
                                print("this will take some time....")
                                time.sleep(3)
                                print("money succesfully deposited current account balance is ",balance + deposit)
                                time.sleep(2)
                            else:
                                time.sleep(2)
                                print("wrong pin")
                        else:
                            time.sleep(2)
                            print("wrong selection")
                                
                else:
                        time.sleep(2)
                        print("wrong pin")
        else:
            time.sleep(2)
            print("wrong age")
else:
    time.sleep(2)
    print("wrong name")
    print("try again")