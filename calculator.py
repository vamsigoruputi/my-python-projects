while True:
    num1=float(input("enter first number: "))
    opr=input("enter operator(+ - * /): ")
    num2=float(input("enter second number: "))
    if opr=="+":
        print("result:",num1+num2)
    elif opr=="-":
        print("result:",num1-num2)
    elif opr=="*":
        print("result:",num1*num2)
    elif opr=="/":
        print("result:",num1/num2)
    else:
        print("invalid operator")
    again=input("do you want to continue?(yes/no): ")
    if again !="yes":
        break

    