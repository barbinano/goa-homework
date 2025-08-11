



def age_authenticator(age):
    if age < 15:
        print("You are too young to access this content.")
    elif age < 18:
        print("You are allowed to access this content with parental guidance.")
    elif age < 21:
        print("You are allowed to access this content with adult supervision.")
    elif age >= 21 :
        print("You are allowed to access this content without any restrictions.")
    else : print("error")
   

age=int(input("your age:"))

age_authenticator(age)
