
while True:
    print("for ADDITION enter 1")
    print("for SUBSTRACTION enter 2")
    print("for MULTIPLICATION enter 3")
    print("for DIVISION enter 4")
    print("for MODULUS enter 5")

    n=int(input("ENTER THE NUMBER GIVEN TO PERFORM YOUR OPERATION:-"))
    
    if(n==1):
        sum=0
        print("performing ADDITION")
        a=int(input("for how many no. do you want to do addtion?:-"))
        for i in range(0,a):
            a=int(input(f"Enter your no. {i}:-"))
            sum=sum+a                  
        
        print(f"your answer is={sum}")

    elif(n==2):
        print("performing SUBSTRACTION")
        a=int(input("Enter first no.:-"))
        b=int(input("Enter second no.:-"))
        ans=a-b
        print(f"your answer is={ans}")

    elif(n==3):
        sum=1
        print("performing MULTIPLICATION")
        a=int(input("for how many no. do you want to do addtion?:-"))
        for i in range(0,a):
            a=int(input(f"Enter your no. {i}:-"))
            sum=sum*a                  
        
        print(f"your answer is={sum}")

    elif(n==4):
        print("performing DIVISION")
        a=int(input("Enter first no.:-"))
        b=int(input("Enter second no.:-"))
        ans=a/b
        print(f"your answer is={ans}")

    elif(n==5):
        print("performing MODULUS")
        a=int(input("Enter first no.:-"))
        b=int(input("Enter second no.:-"))
        ans=a%b
        print(f"your answer is={ans}")

    else:
        print("enter valid no.")