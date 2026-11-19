print("It is s Simple Console Level Calculator.\n")
i = 0;
while i>=0 :
    print("\nSelect the operation.\n")
    print("1 = Addition","2 = Subtraction","3 = Multiplication","4 = Division",sep="\n")
    n = int(input("\nEnter the Numerical Value of the operations : "))
# code for Addition
    if(n==1):
        print("Addition of two numbers.")
        a = int(input("1st Number :"))
        b = int(input("2nd Number :"))
        print("The Sum of the numbers is",a+b)
# code for Subtraction
    elif(n==2):
        print("Subtraction of two numbers.")
        a = int(input("1st Number :"))
        b = int(input("2nd Number :"))
        print("The difference of the numbers is",a-b)
# code for Multiplication
    elif(n==3):
        print("Multiplication of two numbers.")
        a = int(input("1st Number :"))
        b = int(input("2nd Number :"))
        print("The product of the numbers is",a*b)
# code for Division
    elif(n==4):
        print("Division of two numbers.")
        a = int(input("1st Number :"))
        b = int(input("2nd Number :"))
        print("The Quotient of the numbers is",a/b)
    i = i+1
