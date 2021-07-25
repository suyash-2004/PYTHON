import time
pin = 1234
initial_balance = 10000
print("WELCOME TO THE ATM")

time.sleep(1)

def ch1(): #defining 1st function
    pin_input = int(input("ENTER YOUR PIN"))
    if pin_input == pin:
            time.sleep(1)
            withdraw_amount = float(input("ENTER THE WITHDRAW AMOUNT"))
            if withdraw_amount>initial_balance:
                print("insufficient balance")
            time.sleep(1)
            print("MONEY WITHDRAWED......")
            current_balance = initial_balance - withdraw_amount
            time.sleep(1)
            print("YOUR CURRENT ACCOUNT BALANCE IS :",current_balance)
    else:
            print("WRONG PIN")
def ch2(): #defining 2nd function
    time.sleep(1)
    pin_input = int(input("ENTER YOUR PIN"))
        
    if pin_input == pin:
            time.sleep(1)
            print("YOUR CURRENT BALANCE IS :", initial_balance)
    else:
            print("WRONG PIN")
def ch3(): #defining 3rd function 
    pin_input = int(input("ENTER YOUR PIN"))
    time.sleep(1)
        
    if pin_input==pin:
            deposite_amount = int(input("ENTER THE AMOUNT TO BE DEPOSITED : "))
            current_balance = initial_balance + deposite_amount
            time.sleep(1)
            print("\tMONEY DEPOSITED. YOUR CURRENT BALANCE IS ", current_balance)
    else:
            print("WRONG PIN")
    
    
print("ENTER YOUR CHOICE")

print("1.WITHDRAW CASH\n2.CHECH BALANCE\n3.DEPOSIT CASH\n")

x = 1


while x<=4: 
    ch = int(input("ENTER YOUR CHOICE"))
    time.sleep(1)
    
    if ch == 1:
        ch1()
    
    elif ch==2:
        ch2()
    
    elif ch==3:
        ch3()
    else:
        print('WRONG CHOICE')
        
    x = int(input("DO YOUR WANT TO REPEAT?4(YES)/5(NO)"))       
    time.sleep(1)
    if x == 5 :
        print("T H A N K   Y O U !")