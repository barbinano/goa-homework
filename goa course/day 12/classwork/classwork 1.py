#1) for ციკლის მეშვეობით გამოიტანეთ რიცხვები 10-ის ჩათვლით
for i in range(11):
    print(i)

#2) while ციკლის მეშვეობით გამოიტანეთ რიცხვები 5-დან 20-მდე.
i=5
while i<20:
    print(i)
    i=i+1

#3) კომენტარების სახით ახსენით რა არის conditional statement, რა დანიშნლება გააჩნიათ და როგორი სახის განცხადებები გვაქვს.
#conditional statement არის კოდი რომელიც ასრულებს დავალებას იმის მიხედვით თუ მოცემყლი პირობა სიცრუეა თუ სიმართლე. 
#if ასრულებს კოდს, თუ პირობა მართალია.

#elif – ამატებს დამატებით პირობას.

#else – ასრულებს კოდს, თუ ყველა წინა პირობა მცდარი იყო.

#4) მომხმარებელს შემოატანინეთ თავისი ასაკი, შეინახეთ იგი ცვლადში და შეამოწმეთ თუ ასაკი იქნება მეტი ან ტოლი 18-ის 
#მაშინ გამოუტანოს რომ იგი ზრდასრულია, ხოლო თუ იქნება 18-ზე ნაკლები საბოლოო გზის მეშვეობით გამოუტანეთ რომ ის მოზარდია.


#ეს კოდი ადრე დავწერე, სწორია?.
#start
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
#finish


#ეს კი დავალებაა

age=int(input("what is your age?"))
if age>=18:
    print("you are old")
else: print ('you are too young' )







