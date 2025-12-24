# 1) შექმენით რიცხვებით სავსე სია და ახალ სიაში ჩააგდეთ ყველა რიცხვი გამრავლებული 2-ზე. დაპრინტეთ ახალი სია.

nums = [1, 2, 3, 4, 5]
nums_2 = []
for i in nums:
    nums_2.append(i * 2)
print(nums_2)

# 2) შექმენით სახელებით სავსე სია, მომხმარებელს შემოატანინეთ რაიმე რიცხვი, და ამ რიცხვის ინდექსზე ჩაამატეთ სახელი "ნიკა" თქვენს სიაში.

names = ["ანა", "ლუკა", "მარი"]
index = int(input("შეიყვანე რიცხვი: "))
names.insert(index, "ნიკა")
print(names)

# 3) შექმენით string წინადადების ცვლადი, ამ წინადადებიდან დაპრინტეთ მხოლოდ ხმოვანი ასოები.

sentence = "wrelo pepela gafrindi nela"
xmovani = "aeiouAEIOU"
for i in sentence:
    if i in xmovani:
        print(i, " ")

# 4) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 4-ზე მეტი სიგრძეში ან დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.

words = ["cat", "house", "dog", "python", "hi"]



for i in words:
    if len(i) > 4 or words.index(i) % 2 == 1:
        words.remove(i)


print(words)



#5) შექმენით რიცხვებით სავსე სია, გამოითვალეთ რიცხვების საშუალო არითმეტიკული - რიცხვების ჯამი გაყოფილი რიცხვების რაოდენობაზე.


nums = [1, 2, 3, 4, 5]

total=0


for i in nums:
    total += i 


avarage = total / len(nums)

print(avarage)

