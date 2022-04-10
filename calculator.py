import math
print("\t\t\tCALCULATOR\n\n")
print("1.Addition(+) \t 2.Subtraction(-) \t 3.Multiplication(*) \n\n4.Division(/) \t 5.Floor Division(//)\t 6.Modulus(%) \n\n7.Exponent(^) \t 8.Square root \t\t 9.Sine \n\n10.Cosine \t 11.Tangent \t\t 12.Exit\n\n")

while(True):
    choice=int(input("\nEnter Your Choice: "))
    if(choice==1):
        print("\t\tADDITION")
        n1=int(input("\nEnter the number 1:"))
        n2=int(input("\nEnter the number 2:"))
        print("Result of ",n1,"+",n2,"=",n1+n2)
    elif(choice==2):
        print("\n\t\tSUBTRACTION")
        n1=int(input("\nEnter the number 1:"))
        n2=int(input("\nEnter the number 2:"))
        print("Result of ",n1,"-",n2,"=",n1-n2)
    elif(choice==3):
        print("\n\t\tMULTIPLICATION")
        n1=int(input("\nEnter the number 1:"))
        n2=int(input("\nEnter the number 2:"))
        print("Result of ",n1,"*",n2,"=",n1*n2)
    elif(choice==4):
        print("\n\t\tDIVISION")
        n1=int(input("\nEnter the divisor:"))
        n2=int(input("\nEnter the dividend:"))
        print("Result of ",n2,"/",n1,"=",n2/n1)
    elif(choice==5):
        print("\n\t\tFLOOR DIVISION")
        n1=int(input("\nEnter the divisor:"))
        n2=int(input("\nEnter the dividend:"))
        print("Result of ",n2,"/",n1,"=",n2//n1)
    elif(choice==6):
        print("\n\t\tMODULUS")
        n1=int(input("\nEnter the divisor:"))
        n2=int(input("\nEnter the dividend:"))
        print("Result of ",n2,"%",n1,"=",n2%n1)
    elif(choice==7):
        print("\n\t\tEXPONENT")
        n1=int(input("\nEnter the base:"))
        n2=int(input("\nEnter the power:"))
        print("Result of ",n1,"^",n2,"=",n1**n2)
    elif(choice==8):
        print("\n\t\tSQUARE ROOT")
        n1=int(input("\nEnter a number:"))
        print("Result = ",math.sqrt(n1))
    elif(choice==9):
        print("\n\t\tSINE")
        n1=int(input("\nEnter Radiant:"))
        print("Result of sin(",n1,") = ",math.sin(n1))
    elif(choice==10):
        print("\n\t\tCOSINE")
        n1=int(input("\nEnter Radiant:"))
        print("Result of sin(",n1,") = ",math.cos(n1))
    elif(choice==11):
        print("\n\t\tTANGENT")
        n1=int(input("\nEnter Radiant:"))
        print("Result of sin(",n1,") = ",math.tan(n1))
    elif(choice==12):
        print("\n\t\tTHANK YOU!")
        break
    else:
        print("Invalid choice")
        
            
