# 1)შექმენი ფუნქცია, რომელსაც აქვს ერთი პარამეტრი —name.
# ფუნქციამ უნდა დააბრუნოს ტექსტი:
# გამარჯობა, [სახელი]!

# ფუნქცია გამოიძახე სხვადასხვა არგუმენტით მინიმუმ 3-ჯერ.



def greet(name):
    return "გამარჯობა, " + [name]

print(greet("გიორგი"))
print(greet("ანა"))
print(greet("ნიკა"))




# 2)შექმენი ფუნქცია, რომელსაც აქვს ორი პარამეტრი — num1 და num2.
# ფუნქციამ უნდა დააბრუნოს მათი ჯამი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით


def sum_numbers(num1, num2):
    return num1 + num2

print(sum_numbers(5, 3))
print(sum_numbers(10, 20))
print(sum_numbers(-2, 7))



# 3)შექმენი ფუნქცია ერთი პარამეტრით num.

# ფუნქციამ უნდა დააბრუნოს (return) გადაცემული რიცხვის კვადრატი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით



def square(num):
    return num ** 2

print(square(4))
print(square(7))
print(square(10))



# 4)შექმენი ფუნქცია ერთი პარამეტრით — age.

# თუ ასაკი არის 18 ან მეტი, დააბრუნოს:
# სრულწლოვანი ხარ

# სხვა შემთხვევაში:
# არ ხარ სრულწლოვანი




def check_age(age):
    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"

print(check_age(20))
print(check_age(17))
print(check_age(18))






# 5)შექმენი ფუნქცია ერთი პარამეტრით — (string).

# ფუნქციამ უნდა დაბეჭდოს ტექსტის სიმბოლოების რაოდენობა.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით




def string_length(text):
    print(len(text))

string_length("Hello")
string_length("გამარჯობა")
string_length("Python")





# 6)შექმენი ფუნქცია ორი პარამეტრით num1 და nuk2.

# ფუნქციამ უნდა დააბრუნოს მათი ნამრავლი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით





def multiply(num1, num2):
    return num1 * num2

print(multiply(3, 4))
print(multiply(5, 6))
print(multiply(10, 0))






# 7)შექმენი ფუნქცია ერთი პარამეტრით — score.

# თუ ქულა ≥ 90 → დააბრუნოს "შესანიშნავი ქულა"

# თუ ქულა >= 70 და ნაკლებია ან <=89 → დააბრუნოს "კარგი ქულა"

# თუ ქულა >= 50 და <= 69 → დააბრუნოს "დამაკმაყოფილებელი ქულა"

# სხვა შემთხვევაში დააბრუნოს "ჩაჭრილი"

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით




def check_score(score):
    if int(score) >= 90:
        return "შესანიშნავი ქულა"
    elif int(score) >= 70 or int(score)<=89:
        return "კარგი ქულა"
    elif int(score) >= 50  and int(score)<= 69:
        return "დამაკმაყოფილებელი ქულა"
    else:
        return "ჩაჭრილი"


print(check_score(26))
print(check_score(86))
print(check_score(96))


# 8)შექმენი ფუნქცია ერთი პარამეტრით — number.

# ფუნქციამ უნდა დააბრუნოს, ლუწია თუ კენტი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით



def even_or_odd(number):
    if number % 2 == 0:
        return "ლუწია"
    else:
        return "კენტია"

print(even_or_odd(4))
print(even_or_odd(7))
print(even_or_odd(10))





# 9)შექმენი ფუნქცია ერთი პარამეტრით — name

# ფუნქციამ უნდა დააბრუნოს მხოლოდ პირველი ასო.

# მაგალითად:
# „Giorgi“ → G

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით





def first_letter(name):
    return name[0]

print(first_letter("Giorgi"))
print(first_letter("saba"))
print(first_letter("Luka"))




# 10)შექმენი ფუნქცია სამი num1 num2 num3.

# ფუნქციამ უნდა დააბრუნოს ამ სამი რიცხვის საშუალო არითმეტიკული.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით







def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(3, 6, 9))
print(average(10, 20, 30))
print(average(5, 5, 5))






# 11)შექმენი ფუნქცია ერთი პარამეტრით —password.

# თუ პაროლი უდრის "python123" → დააბრუნოს  "წვდომა დაშვებულია"

# სხვა შემთხვევაში → "არასწორი პაროლი"

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით



def check_password(password):
    if password == "python123":
        return "წვდომა დაშვებულია"
    else:
        return "არასწორი პაროლი"



print(check_password("python123"))
print(check_password("123python"))
print(check_password("kirky"))





# 12)შექმენი ფუნქცია ერთი პარამეტრით — text.

# ფუნქციამ უნდა დააბრუნოს ეს ტექსტი მთლიანად დიდი ასოებით.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით


def to_uppercase(text):
    return text.upper()
 

print(to_uppercase("python"))
print(to_uppercase("Hello World"))
print(to_uppercase("privet"))
