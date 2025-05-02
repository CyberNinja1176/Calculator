print("1-ADD")
print("2-SUB")
print("3-DIV")
print("4-MULTIPLY")

option = float(input("Choose an Option (1,2,3,4):- "))
result=0

if(option in [1,2,3,4]):
    num1=float(input("Enter 1st number:- "))
    num2=float(input("Enter 2nd number:- "))

    if(option == 1):
        res= num1+ num2
    elif(option ==2):
        res=num1-num2
    elif(option ==3):
        res=num1/num2
    elif(option ==4):
        res=num1*num2


else:
    print("Invilid Operaion entered")
print("The Result of The Operation is {}".format(res))