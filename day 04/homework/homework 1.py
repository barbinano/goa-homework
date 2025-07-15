#2) კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

#input არის ინფორმაცია რომელსაც მომხმარებელი აძლევს პროგრამას, და output არის შედეგი რომელსაც პროგრამა უბრუნებს მომხმარებელს.
#მაგალითად input:
name = input("what is yout name? ")

print(name)  #ეს არის output






#3) შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ.

age = input("what is your age? ")

print(type(age))






#4) თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

str_1="you"    #string
str_2="are"    #string
str_3="gonna"  #string
str_4="kick"   #string
str_5="meowt"  #string


int_1=10       #integer
int_2=11       #integer
int_3=12       #integer
int_4=13       #integer
int_5=14       #integer


float_1=3.2    #float
float_2=3.3    #float
float_3=4.3    #float
float_4=5.2    #float
float_5=6.1    #float







#5) აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.


str_6="goga"
int_6=12
float_6=2.1

print(type(str_6))
print(type(int_6))
print(type(float_6))





#6) მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.


name_1=input("write your name:")
last_name=input("what is your last name? ")
print(name_1 + " " + last_name)






#7) მომხმარებელს შემოატანინეთ 5 რიცხვი სხვადასხვა დამოუკიდებელი input-ების სახით, თქვენი დავალებაა დაბეჭდოთ მათი საშუალო არითმეტიკული.



number_1=input("your age: ")
number_2=input("your birth year: ")
number_3=input("current year: ")
number_4=input("your hight: ")
number_5=input("your weight: ")

total=(int(number_1) + int(number_2) + int(number_3) + int(number_4) + int(number_5) )
answer=(total / 5)
print(answer)




#8) მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი, სიმაღლე, წონა და ამ მონაცემების გამოყენებით დაბეჭდეთ ერთი დიდი წინადადება.

your_name=input("what is your name? ")
surname=input("what is your surname? ")
your_age=input("how old are you? ")
your_height=input("how tall are you? ")
your_weight=input("what is your weight? ")


print("მონაცემები: " + your_name + " " + surname + " " + your_age + " " + your_height + " " + your_weight)
