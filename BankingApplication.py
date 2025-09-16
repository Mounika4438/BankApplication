import random


class Bank:
    account_holders=[]  #class variable
    def create_account(self):
        print(" ******** Welcome to Mana Andhari Bank ******** ")
        print()
        new_holder={}
        new_holder["Holder_name"]=input("Enter holder name : ")
        new_holder["mobile"]=int(input("Enter mobile num : "))
        new_holder["Aadhar"]=int(input("enter aadhar number : "))
        data=random.randint(100000000000,999999999999)
        new_holder["account_number"]=data
        n1=input("enter type of account saving/zero : ").lower()
        if n1=="saving":
            while True:
                n2=int(input("your account is saving you have to deposite 1000 : "))
                if n2==1000:
                    new_holder["balance"]=n2
                    break
                else:
                    print("please deposite 1000 rupees")
            
        if n1=="zero":
            while True:
                n3=int(input("your account is zero you have to deposite 500 : "))
                if n3==500:
                    new_holder["balance"]=n3
                    break
                else:
                    print("please deposite 500 rupees")
            
        Bank.account_holders.append(new_holder)
        print()
        print(Bank.account_holders)
        print()
    def deposite(self):
        print(" ******** Welcome to Deposite section ******** ")
        print()
        s3=int(input("enter deposite money : "))
        isdeposite=True
        while isdeposite:
            s1=input("Enter holder name: ")
            s2=int(input("enter account number :"))
        
            for i in Bank.account_holders:
                if i["account_number"]==s2 and i['Holder_name']==s1:
                    res=i.get('balance')
                    i['balance']=res+s3
                    isdeposite=False
                else:
                    print("Invaild ACCOUNT NUMBER or HOLDER NAME ")
        print()
        print(Bank.account_holders)
        print()
    def withdraw(self):
        print(" ******** Welcome to Withdraw section ******** ")
        print()
        withdraw_money=int(input("Enter withdraw amount : "))
        iswithdraw=True
        while iswithdraw:
        
            holder_name=input("Enter holder name : ")
            acc_number=int(input("Enter account number : "))
        
            for i in Bank.account_holders:
                if i["account_number"]==acc_number and i["Holder_name"]==holder_name:
                    res=i.get("balance")
                    i["balance"]=res-withdraw_money
                    iswithdraw=False
            else:
                print("Invaild ACCOUNT NUMBER or HOLDER NAME ")
        print()
        print(Bank.account_holders)
        print()
    def check_details(self):
        print(" ******** You can check your details by entring your ACCOUNT HOLDER NAME and ACCOUNT NUMBER ******** ")
        print()
        isdetails=True
        while isdetails:
            holder_name=input("Enter holder name to check the details : ")
            acc_num=int(input("Enter account number : "))
            print()
            for i  in Bank.account_holders :
                if i["account_number"]==acc_num and i["Holder_name"]==holder_name:
                    for a,b in i.items():
                        print(a," =====> ",b)
                        isdetails=False
            if isdetails:
                print("Invaild ACCOUNT NUMBER or HOLDER NAME ")
        print()
    def check_balance(self):
        print(" ******** You can check your BALANCE by entring your ACCOUNT HOLDER NAME and ACCOUNT NUMBER ******** ")
        print()
        isbalance=True
        while isbalance:
            holder_name=input("Enter holder name to check the BALANCE : ")
            acc_num=int(input("Enter account number : "))
            for i  in Bank.account_holders :
                if i["account_number"]==acc_num and i["Holder_name"]==holder_name:
                    print()
                    remaining_balance=i["balance"]
                    print(f"Total balance of {holder_name} is {remaining_balance}")
                    print()
                    isbalance=False
            if isbalance:
                print("Invaild ACCOUNT NUMBER or HOLDER NAME ")

obj=Bank()
while True:
    n=int(input('''1) Create new account
2) Deposite
3) WithDraw
4) Check Details
5) Check Balance
6) Break
Please enter a number between 1 to 6 :   '''))
    print()
    if n==1:
        obj.create_account()
    elif n==2:
        obj.deposite()
    elif n==3:
        obj.withdraw()
    elif n==4:
        obj.check_details()
    elif n==5:
        obj.check_balance()
    elif n==6:
        break

#  Sample output:
# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   1

#  ******** Welcome to Mana Andhari Bank ******** 

# Enter holder name : Mounika
# Enter mobile num : 789045673
# enter aadhar number : 7056784356278
# enter type of account saving/zero : saving
# your account is saving you have to deposite 1000 : 100 
# please deposite 1000 rupees
# your account is saving you have to deposite 1000 : 1000

# [{'Holder_name': 'Mounika', 'mobile': 789045673, 'Aadhar': 7056784356278, 'account_number': 651407053810, 'balance': 1000}]

# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   1

#  ******** Welcome to Mana Andhari Bank ********

# Enter holder name : Bindu
# Enter mobile num : 9087656743
# enter aadhar number : 897654638965
# enter type of account saving/zero : zero
# your account is zero you have to deposite 500 : 500

# [{'Holder_name': 'Mounika', 'mobile': 789045673, 'Aadhar': 7056784356278, 'account_number': 651407053810, 'balance': 1000}, {'Holder_name': 'Bindu', 'mobile': 9087656743, 'Aadhar': 897654638965, 'account_number': 175779084752, 'balance': 500}]

# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   1

#  ******** Welcome to Mana Andhari Bank ********

# Enter holder name : Maha Farjana
# Enter mobile num : 7098656748
# enter aadhar number : 890765235689 
# enter type of account saving/zero : zero
# your account is zero you have to deposite 500 : 500

# [{'Holder_name': 'Mounika', 'mobile': 789045673, 'Aadhar': 7056784356278, 'account_number': 651407053810, 'balance': 1000}, {'Holder_name': 'Bindu', 'mobile': 9087656743, 'Aadhar': 897654638965, 'account_number': 175779084752, 'balance': 500}, {'Holder_name': 'Maha Farjana', 'mobile': 7098656748, 'Aadhar': 890765235689, 'account_number': 414863694113, 'balance': 500}]

# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   2

#  ******** Welcome to Deposite section ********

# enter deposite money : 50000
# Enter holder name: Mounika
# enter account number :651407053810
# Invaild ACCOUNT NUMBER or HOLDER NAME 
# Invaild ACCOUNT NUMBER or HOLDER NAME

# [{'Holder_name': 'Mounika', 'mobile': 789045673, 'Aadhar': 7056784356278, 'account_number': 651407053810, 'balance': 51000}, {'Holder_name': 'Bindu', 'mobile': 9087656743, 'Aadhar': 897654638965, 'account_number': 175779084752, 'balance': 500}, {'Holder_name': 'Maha Farjana', 'mobile': 7098656748, 'Aadhar': 890765235689, 'account_number': 414863694113, 'balance': 500}]

# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   3

#  ******** Welcome to Withdraw section ********

# Enter withdraw amount : 1000
# Enter holder name : Mounika
# Enter account number : 651407053810
# Invaild ACCOUNT NUMBER or HOLDER NAME 

# [{'Holder_name': 'Mounika', 'mobile': 789045673, 'Aadhar': 7056784356278, 'account_number': 651407053810, 'balance': 50000}, {'Holder_name': 'Bindu', 'mobile': 9087656743, 'Aadhar': 897654638965, 'account_number': 175779084752, 'balance': 500}, {'Holder_name': 'Maha Farjana', 'mobile': 7098656748, 'Aadhar': 890765235689, 'account_number': 414863694113, 'balance': 500}]

# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   4

#  ******** You can check your details by entring your ACCOUNT HOLDER NAME and ACCOUNT NUMBER ********

# Enter holder name to check the details : Mounik
# Enter account number : 651407053810

# Invaild ACCOUNT NUMBER or HOLDER NAME
# Enter holder name to check the details : Mounika
# Enter account number : 651407053810

# Holder_name  =====>  Mounika
# mobile  =====>  789045673
# Aadhar  =====>  7056784356278
# account_number  =====>  651407053810
# balance  =====>  50000

# 1) Create new account
# 2) Deposite
# 3) WithDraw
# 4) Check Details
# 5) Check Balance
# 6) Break
# Please enter a number between 1 to 6 :   5

#  ******** You can check your BALANCE by entring your ACCOUNT HOLDER NAME and ACCOUNT NUMBER ********

# Enter holder name to check the BALANCE : Mouniks
# Enter account number : 651407053810
# Invaild ACCOUNT NUMBER or HOLDER NAME 
# Enter holder name to check the BALANCE : Mounika
# Enter account number : 651407053810

# Total balance of Mounika is 50000
