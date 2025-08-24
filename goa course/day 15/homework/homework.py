#1)შექმენით ცვლადი სადაც შეინახავთ ინტეჯერ ტიპის მონაცემს,
#შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია 10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"
number_1=8

if number_1>10:
    print("more than 10")
    
else: print("less than 10")



#2)მომხმარებელს შემოაყვანინეთ რიცხვი,შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში დაუპრინტეთ "not equal to 15"
number_2=int(input("enter random number:"))

if number_2==15:
    print("equal to 15")

else: print("not equal to 15")




#3)მომხმარებელს შემოატანეთ სტრინგი შენი დავალებაა შეამოწმო,
#თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის giorgi დაუპრინტეთ 'you are correct" სხვა შემთხვევაში დაუპრინტეთ "you are wrong"

name=input("enter name? ")

if name==("giorgi"):
    print("you are correct")

else: print("you are wrong")


#4)დაატრიალეთ ფორ ციკლი 50 დან 100 მდე 5 ის გამოტოვებით

for i in range(50,100,5):
    print(i)




#5)ფორ ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი

for i in range(3):
    print("saba saghliani")



#6)while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე
i=20

while i<50:
    print(i)

    i=i+1
