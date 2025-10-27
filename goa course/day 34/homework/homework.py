#1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
 #  for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.
countrys=["georgia" , "USA" , "russia" , "india"]

length=len(countrys)

for i in range(length):
    if len(countrys[i]) > 6:
        print(countrys[i])

    else:
        print("not more then 6")



#2) შექმენით სია სხვადასხვა სიტყვებით.  
#-> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.

random_words=["supermasiveblac" , "ukwhatelseismassive?" , "mein kampf"]

length_2=len(random_words)

for i in range(length_2):
    if len(random_words[i]) % 15 == 0 :
        print (random_words[i])

    else:
        print("not devided by 15")



#3) შექმენით სია რიცხვებით.  
#-> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
#-> არ გამოიყენოთ len() — დაითვალეთ ხელით.
list_2=[10, 13, 12, 17, 18 , 90, 1]

length_3=0

for i in range(7):
    length_3+=1


print (length_3)



#4) შექმენით სია სხვადასხვა სიტყვებით.  
#-> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.

list_3=["georgia" , "USA" , "russia" , "india" , "pakistan", "beard"]

length_4=len(list_3)

for i in range(length_4):
    if len(list_3[i]) == 5:
        print(list_3[i])

    else:
        print("not equal to 5")


#5) მომხმარებელს შემოატანინე წინადადება.  
#-> გაიგე რამდენი სიმბოლოა წინადადებაში.  
#-> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

text = input("შეიყვანეთ სიტყვა ან ტექსტი: ")

length_5 = len(text)

counting_a=0

for i in range(length_5):
    if text[i]=="a" or text[i] == "A": 
        counting_a+=1

print(counting_a)



#6) <= Boss Level =>
#შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
#--> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი

list_4=["georgia" , "USA" , "russia" , "india" , "pakistan", "beard" , "crest"]


length_6=len(list_4)

longest=list_4[0]

for i in range(length_6):
    if len(list_4[i]) > len(longest):
        longest=(list_4[i])

print(longest)

