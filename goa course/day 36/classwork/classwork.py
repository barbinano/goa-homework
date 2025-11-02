#1) შემოაყვანიეთ მომხმარებელს რაღაცა სიტყვა:
#-> შეამოწმეთ არის თუ არა 'a' ან 'A' ამ სიტყვაში/ტექსტში
#> შეამოწმეთ თუ არ არის სიტყვა 'car' ამ სიტყვაში/ტექსტში

word_1=input("write a word")
letter = "a" or "A"
if letter in word_1:
    print("letter is in word")

else:
    print("not in the word")

if word_1 != "car":
    print("word is not car car")

else:
    print("car isnt the word")




word_1=input("write a word")

a_asoiani=("a" in word_1) or ("A" in word_1)

if a_asoiani == True:
   print("letter is in word")

else:
    print("not in the word")



no_car = 'car' not in word_1

if no_car == True:
        print("word is not car car")

else:
    print("car isnt the word")




    #2) მომხმარებელს შემოატანინეთ ტექსტი.
#-> დაუარეთ ამ ტექტის ასოებს for ლუპით
#-> თუ ასო არის 'a' ან 'A' დასკიპეთ, სხვა შემთხვევაში დაპრინტეთ ასო


text_2 = input("შეიყვანე ტექსტი: ")

length=len(text_2)


for i in range(length):
    if i == 'a' or i == 'A':
        continue
    print(text_2[i])







    



