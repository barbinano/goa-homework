#1)მოცემულია სტრინგი "PythonProgramming".
#ამოიღე პირველი 6 სიმბოლო და დაბეჭდე გამოიყენეთ slicing



string_1="PythonProgramming"
print(string_1[:6])




#2)მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
#ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე გამოიყენეთ slicing (მინუს ინდექსებითაც)

numbers_1 = [10, 20, 30, 40, 50, 60, 70]
print(numbers_1[2:5])
print(numbers_1[-5:-2])




#3)მოცემულია სტრინგი "HelloWorld".
#დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)

string_2="HelloWorld"

print(string_2[:5])
print(string_2[-10:-5])


#3)მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
#დაბეჭდე ყოველ პირველი მესამე მეხუთე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)

letters_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters_1[0])
print(letters_1[2])
print(letters_1[4])


print(letters_1[-7])
print(letters_1[-5])
print(letters_1[-3])

#4)მოცემულია სტრინგი "Information".
#ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)


string_3="Information"
print(string_3[2:7])
print(string_3[-9:-4])




#5)
#მოცემულია სტრინგი "abcdefghijklmno".
#შექმენი სამი სხვადასხვა სლაისი:

#პირველი შეიცავდეს მხოლოდ a დან d მდე ასოებს

#მეორე – შეიცავდეს j დან o მდე ასოებს

#მესამე – შეიცავდეს f დან j მდე ასოებს

string_4 = "abcdefghijklmno"

print(string_4[0:3])   
print(string_4[9:14] ) 
print(string_4[5:9])  

            