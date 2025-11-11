from ATMmenu import menu
from ATMoperation import deposit,withdraw,balenq
from ATMexcept import DepositError,WithDrawError,InSufficientFundError
while True:
    try:
        menu()
        ch=int(input("Enter your choice:"))
        match ch:
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDON'T ENTER ZERO OR -VE VALUES FOR DEPOSITS.")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOL FOR DEPOS ITS.")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDON'T ENTER ZERO OR -VE VALUES FOR WITHDRAWING.")
                except ValueError:
                    print("\tDON'T ENTER ALNUMS,STRS AND SYMBOL FOR WITHDRAWING.")
                except InSufficientFundError:
                    print("\tYOUR ACCOUNT DOESN'T HAVE SUFFICIENT FUND")
            case 3:
                balenq()
            case 4:
                print("\tThank you, visit again.")
                break
            case _:
                print("\tYour choice of selection is wrong-try again.")
    except ValueError:
        print("\tDon't Enter alnums,str and symbols for choice-try again.")