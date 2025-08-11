def age_authenticator(age, salary):
    if salary < 2000:
        print("You do not meet the salary requirement to access this content.")
    elif salary >=2000 :
       print("You meet the salary requirement to access this content.")
    
    if age < 15:
        print("You are too young to access this content.")
    elif age < 18:
        print("You are allowed to access this content with parental guidance.")
    elif age < 21:
        print("You are allowed to access this content with adult supervision.")
    elif age >= 21 :
        print("You are allowed to access this content without any restrictions.")
   

age_authenticator(18, 1200)