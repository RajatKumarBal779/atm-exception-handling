from ATMexcept import DepositError,WithDrawError,InSufficientFundError
bal=500.00 #min amount in the account
def deposit():
    global bal
    damt=float(input("Enter the deposit amount:"))
    if damt<=0:
        raise DepositError
    else:
        bal+=damt
        print(f"\tYour account xxxxxx4296 credited with INR:{damt}")
        print("\tNow your account xxxxxx4296 balance after deposit:{}".format(bal))
def withdraw():
    global bal
    wamt=float(input("Enter the withdrawal amount:"))
    if wamt<=0:
        raise WithDrawError
    else:
        if (wamt+500)>bal:#min bal must be 500 and that 500 can't be withdrawal
            raise InSufficientFundError
        else:
            bal-=wamt
            print(f"\tYour account xxxxxx4296 debited with INR:{wamt}")
            print("\tNow your account xxxxxx4296 balance after withdraw:{}".format(bal))
def balenq():
    print("\tyour account xxxxxx4296 balance is:{}".format(bal))