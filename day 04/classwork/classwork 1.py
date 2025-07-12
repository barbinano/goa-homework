#1) მომხმარებელს შემოატანინეთ input-ის მეშვეობით სახელი და თქვენი დავალებაა შეინახოთ იგი ცვლადში და დაპრინტოთ ეს მნიშვნელობა.

name=input("what is your name?")
print("your name is " + name)

#2) მომხარებელს შემოატანინეთ 2 ცალი რიცხვი სხვადასხვა დამოუკიდებელი input-ის მეშვეობით, ამის შემდეგ კი უბრალოდ დაბეჭდეთ ამ შემოყვანილი რიცხვების ჯამი. (დაგჭირდებათ int() ფუნქცია)

num_1=input("what is your age?")
num_2=input("what year were you born in?")
print(int(num_1) + int(num_2))



#3) მომხმარებელს შემოატანინეთ თავისი ასაკი, თქვენი დავალებაა დაბეჭდოთ ამ მომხმარებლის მიერ შემოყვანილი მნიშვნელობის მონაცემთა ტიპი.
age=input("what is your age?")
print(type(age))



#4) შექმენით 4 ცვლადი, თითოულ ცვლადში შეინახეთ 1 მონაცემთა ტიპის მნიშვნელობა, თქვენი დავალებაა კი საბოლოოდ დაბეჭდოთ ამ ცვლადების მონაცემტა ტიპები


variable_1=("saba")
variable_2=16
variable_3=1.87
variable_4= True

print(type(variable_1))
print(type(variable_2))
print(type(variable_3))
print(type(variable_4))
