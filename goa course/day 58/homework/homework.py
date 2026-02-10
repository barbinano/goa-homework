# 1) შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.



numbers = [5, 12, 3, 21, 9, 18]

biggest = 0
second_biggest = 0

for i in numbers:
    if i > biggest:
        second_biggest = biggest
        biggest = i
    elif i > second_biggest and i != biggest:
        second_biggest = i

print("მეორე ყველაზე დიდი რიცხვია:", second_biggest)








# 2) მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, დაპრინტეთ ასეთი სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.



sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()

count = 0
i = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print( count)




# 3) მომხმარებელს შემოატანინეთ სიტყვა და გაიგეთ ეს სიტყვა არის თუ არა პალინდრომი - ანუ ეს სიტყვა წინიდანაც და უკნიდანაც თუ ზუსტად იგივენაირად იკითხება. თუ კი მაშინ დაპრინტეთ True, თუ არა დაპრინტეთ False, გამოიყენეთ for ციკლი, არ გამოიყენოთ slicing - [::-1].



word = input("შეიყვანეთ სიტყვა: ")
length = len(word)












# 4) შექმენით არეული რიცხვებით სავსე გრძელი სია და 2 ცარიელი სია, ერთ სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, ხოლო მეორე სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, გამოიყენეთ for ციკლი.



numbers = [13, 8, 21, 4, 6, 15, 10, 7, 18, 9, 2, 11]

index_1 = []
index_2 = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        if i % 2 == 1:
            index_1.append(numbers[i])
        else:
            index_2 .append(numbers[i])

print("ლუწი რიცხვები კენტ ინდექსზე:", index_1)
print("ლუწი რიცხვები ლუწ ინდექსზე:", index_2        )




# 5) შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები - ყველაფერი რაც მეორდება 2-ზე მეტჯერ, გამოიყენეთ remove() ფუნქცია და while ციკლი.

data = [1, "apple", 2, "apple", 3, 1, 1, True, False, True, "banana", "banana", "banana"]

i = 0
while i < len(data):
    if data.count(data[i]) > 1:
        data.remove(data[i])
    else:
        i += 1

print(data) 







# 6)  მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი ყველაზე გრძელი სიტყვა, გამოიყენეთ while ციკლი, არ გამოიყენოთ max() ფუნქცია.

sentence = input("შეიყვანეთ წინადადება: ")
words = sentence.split()

longest_word = ""
i = 0

while i < len(words):
    if len(words[i]) > len(longest_word):
        longest_word = words[i]
    i += 1

print("ყველაზე გრძელი სიტყვაა:", longest_word)
