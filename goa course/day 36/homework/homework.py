#1) მომხმარებელს შემოატანინეთ სიტყვა.  
#-> იტერაციით გაიარეთ თითო ასო  
#-> თუ შეხვდებით ასო 'e'-ს ან 'E'-ს გაჩერდით (break)  
#-> დაბეჭდეთ მხოლოდ ის ასოები, რაც მანამდე იყო  

word_1=input("write a word")

length_1=len(word_1)

for i in range(length_1):
    if word_1[i] == "e"  or word_1[i] == "E":
        break

    else: print (word_1[i])

#2) მომხმარებელს შემოატანინეთ წინადადება.  
#-> შეამოწმეთ არის თუ არა ტექსტში სიტყვა 'bad'  
#-> თუ არის, დაპრინტეთ "აკრძალული სიტყვა!"  
#-> თუ არაა, დაპრინტეთ "ყველაფერი რიგზეა"  


sentence_1 = input("write a sentence: ")


if "bad" in sentence_1:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")



#3) მომხმარებელს შემოატანინეთ წინადადება.  
#-> დაუარეთ ტექსტს for ციკლით  
#-> გამოტოვეთ ყველა space => ' '
#-> დაბეჭდეთ ყველა დანარჩენი სიმბოლო  

sentence_2 = input("write a sentence: ")

length_2=len(sentence_2)

for i in range(length_2):
    if sentence_2[i] == " ":
        continue
    else:
        print(sentence_2[i])






#4) მომხმარებელს შემოატანინეთ წინადადება.  
#-> დაუარეთ მას for ლუპით  
#-> გამოტოვეთ ხმოვნები (a, e, i, o, u)  
#-> დაბეჭდეთ მხოლოდ თანხმოვნები და თავისთავათ ყველა სხვა სიმბოლო 

sentence_3 = input("write a sentence: ")

length_3=len(sentence_3)

for i in range(length_3):
    if sentence_3[i] == "a" or sentence_3[i]== "e"  or sentence_3[i] == "i"  or sentence_3[i] == "o" or sentence_3[i] == "u":
        continue

    else: print(sentence_3[i])





 


#5) მომხმარებელს შემოაყვანით ორი რიცხვი
#--> დაუარეთ ყველა რიცვს ამ დიაპაზონში
#--> დაბეჭდეთ მხოლოდ რიგით პირველი რიცხვი ამ შუალედში რომელიც იყოფა 15-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)

number_1=int(input("write a number"))

number_2=int(input("write a number"))

for i in range(number_1, number_2 + 1 ):
    if i % 15 == 0:
        print(i)
        break




#6) შექმენით უსასრულო while loop:
#--> სანამ მომხმარებელი არ შემოიყვანს 'python is best', მანამდე დაპრინტეთ 'you should learn python'


while True:
    text = input("write a sentence: ")
    if text == "python is best":
        break
    print("you should learn python")



#7) \<.BOSS.>/ 
#მომხმარებელს შემოაყვანით ორი რიცხვი
#--> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით მესამე რიცხვი ამ შუალედში რომელიც იყოფა 3-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)


number_3=int(input("write a number"))

number_4=int(input("write a number"))

for i in range(number_3, number_4 + 1, 3 ):
     if i % 3 == 0:
        print(i)
        break

