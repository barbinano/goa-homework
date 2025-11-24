# 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.

fruits = ["apple", "banana", "orange"]
fruits_2=["kiwi", "mango"]
fruits.extend(fruits_2)
print(fruits)

# 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.

numbers = [10, 20, 30]
numbers_2=  [40, 50]
numbers.extend(numbers_2)
print(numbers)

# 3) შექმენი სია names და შეაბრუნე reverse()-ით.

names = ["ana", "luka", "mari"]
names.reverse()
print(names)

# 4) შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.

numbers_3 = [5, 2, 5, 7, 5, 9]
print(numbers_3.count(5))

# 5) შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.

letters = ["a", "b", "a", "c"]
print(letters.count("a"))

# 6) შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.

names_2 = ["dato", "saba", "nini"]
print(names_2.index("saba"))

# 7) შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.

colors = ["red", "green", "blue"]
print(colors.index("blue"))


# 8) შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].

numbers_4 = [1, 2, 3]
numbers_5 = [7, 8, 9]
numbers_4.extend(numbers_5)
print(numbers_4)


# 9) შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.

foods = ["bread", "milk", "cheese"]
foods.reverse()
print(foods)


# 10) შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".

cities = ["batumi", "tbilisi", "kutaisi"]
print(cities.index("tbilisi"))


# 11) შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.

animals = ["cat", "dog", "cat", "cow"]
print(animals.count("cat"))


# 12)შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.

fruits = ["apple", "banana"]
fruits.append("grape")
print(fruits)


# 13)შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.

numbers_6 = [1, 2, 3]
numbers_7 = [4, 5]

numbers_6.extend(numbers_7)

print(numbers_6)

# 14)შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.

names_2 = ["goga", "saba"]
names_2.insert(1, "luka")   
print(names_2)


# 15)შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.

items = ["pen", "pencil", "eraser"]
items.pop()
print(items)


# 16)შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.

colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)


# 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.


foods = ["bread", "milk"]
element_count=len(foods)
if  element_count == 2:
    foods.append("cheese")
else:
    foods.append("meat")

print(foods)


# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

nums = [10, 20, 30]
input_number = int(input("Enter integer: "))

if input_number in nums:
    print("Already in list")
else:
    nums.append(40)
    print(nums)


# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.

letters = ["a", "b", "c"]
input_letter = input("Enter a letter: ")


letters.insert(1, input_letter)

print(letters)


# 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.

values = [1, 2, 3, 4]
index = int(input("Enter index: "))

if  index < len(values):
    values.pop(index)
else:
    print("Index out of range")

print(values)


# 21)შექმენი სია pets = ["cat", "dog", "hamster"].  მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.

pets = ["cat", "dog", "hamster"]
pet_name = input("Enter pet name: ")

if pet_name in pets:
    pets.remove(pet_name)
    print("Removed")
else:
    print("Not found")

print(pets)



# 22)შექმენი სია a = [5, 5, 7]. მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი არის სიის ელემენტი, დაბეჭდე რამდენჯერ არის სიაში - count() ფუნქციის გამოყენებით. სხვა შემთხვევაში append()-ით ჩასვი ის სიაში და დაბეჭდე სია.

a = [5, 5, 7]
input_number_2 = int(input("Enter number: "))

if input_number_2 in a:
    print(a.count(input_number_2))
else:
    a.append(input_number_2)
    print(a)



# 23)შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. შემდეგ if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, თუ არ არის 5-ზე მეტი დაბეჭდე შებრუნებული სია.

queue = ["first", "second"]
new_element = input("Enter new item: ")

queue.insert(0, new_element)

if len(queue) > 5:
    queue.pop()       
    print(queue)
else:
     print(queue.reverse)   


# 24)შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; თუ 0-ია ან ნაკლებია ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.


nums = [2, 4, 6]
input_number_3 = int(input("Enter number: "))

if input_number_3 > 0:
    nums.append(input_number_3)
else:
    print("Only positive allowed")

print(nums)



# 25) შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.

mix = ["x", "y", "z"]
mix_2 = [1, 2, 3]
mix.extend(mix_2)

user_input = input("Enter a letter: ")

if user_input in mix:
    mix.remove(user_input)
    print("Removed")

else:
    print("No such element")

    

print(mix)

