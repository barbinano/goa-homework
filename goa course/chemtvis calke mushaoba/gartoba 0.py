import time

password = "12342"

print("Cracking Password....")

for i in range(100000000):
    guess = str(i).zfill(5)

   

    if guess == password:

        print("Password Found")

        print("Password is:", guess)
        
        break



