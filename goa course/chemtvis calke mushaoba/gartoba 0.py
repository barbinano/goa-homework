password = "114324356"

print("Cracking Password....")

for i in range(1000000000000):
    guess = str(i).zfill(len(password))

   

    if guess == password:

        print("Password Found")

        print("Password is:", guess)
        
        break



