#1) მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
#--> თუ დადებითია დაპრინტეთ 'ეს რიცხვი დადებითი რიცხვია'
#--> თუ უარყოფითია დაპრინტეთ 'ეს რიცხვი უარყოფითი რიცხვია'
#--> თუ ნულია დაპრინტეთ 'ეს რიცხვი ნულია'

number_1=int(input("input random number:"))

if number_1>0:
    print('ეს რიცხვი დადებითი რიცხვია')

elif number_1 < 0:
    print('ეს რიცხვი უარყოფითი რიცხვია')

else: print('ეს რიცხვი ნულია')






#2) მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
#0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
#13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
#20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
#65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
#120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
#თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'



number_2=int(input("your age:"))

if number_2 > 0 and number_2 < 13:
    print('ბავშვი ხარ')

elif number_2 > 13 and number_2 < 20:
    print('მოზარდი/თინეიჯერი ხარ')

elif number_2 > 20 and number_2 < 65:
    print('ზრდასრული ხართ')

elif number_2 > 65 and number_2 < 120:
    print('ხანში შესული ხართ')

elif number_2 > 120:
    print('გურუ ან ჯადოქარი ხარ')

elif number_2 < 0:
    print('არასწორი ინფო')





#3) დაწერეთ "password guesser" პროგრამა, შექმენით რაიმე ცვლადი და მასში შეინახეთ ის პაროლი რომელსაც ყველგან იყენებთ ;)
#მომხმარებელს მოთხოვეთ გამოიცნოს თქვენი პაროლი
#აღნიშნეთ ცდების რაოდენობა
#გამოიყენეთ while loop, მანამ ატრიალეთ სანამ მომხმარებელი პაროლს არ გამოიცნობს ან დაწერს --> 'nah strong password'
#ბოლოს აჩვენეთ(დაუპრინტეთ) რამდენი ცდა დაჭირდა პაროლის გამოსაცნობად


password = "fake password"   
attempts = 0                 

guess = ""                   
while guess != password:    
    guess = input("Guess the password or type nah strong password to give up: ")
    attempts += 1

    if guess == "nah strong password":  
        print("giving up alredy?")
        break
    elif guess != password:
        print("wrong password, please try again!")


if guess == password:
    print(f"password is correct. {attempts} attempts were needed.")



#4) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი
number_3=int(input("input random number:"))
number_4=int(input("input random number:"))
number_5=int(input("input random number:"))

if number_3> number_4 and number_3 > number_5:
    print(number_3)

elif number_4 > number_3 and number_4 > number_5:
    print(number_4)

elif number_5 > number_3 and number_5> number_4:
    print(number_5)






#5) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
#თუ 1 --> დაპრინტეთ 'ორშაბათი'
#თუ 2 --> დაპრინტეთ 'სამშაბათი'
#თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
#თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
#თუ 5 --> დაპრინტეთ 'პარასკევი' 
#თუ 6 --> დაპრინტეთ 'შაბათი'
#თუ 7 --> დაპრინტეთ 'კვირა' 
#სხვა დანარჩენი --> 'არ ვიცი ეგ რა დღეა'



number_6=int(input("input  number 1-7:"))

if number_6==1:
    print('ორშაბათი')

elif number_6==2:
    print("სამშაბათი")

elif number_6==3:
    print('ოთხშაბათი')

elif number_6==4:
    print('ხუთშაბათი')

elif number_6==5:
    print('პარასკევი')


elif number_6==6:
    print('შაბათი')


elif number_6==7:
    print('კვირა' )

else: print('არ ვიცი ეგ რა დღეა')



