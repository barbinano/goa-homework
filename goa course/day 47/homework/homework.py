# 1) შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი რომელიც იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები.

names = ["Giorgi", "nino", "Ana", "luka", "Dato"]

Upper_name = []


for i in names:
    if i[0] == i[0].upper():
        Upper_name.append(i)

print(Upper_name)



# 2) შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ დიდი, ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის სიასთან და დაპრინტეთ მიღებული შედეგი.



names = ["Giorgi", "Nino", "Ana"]
surnames = ["BERIDZE", "gelashvili", "KAPANADZE"]




for i in range(len(names)):
    names[i] = names[i].upper()

for i in range(len(surnames)):
    surnames[i] = surnames[i].lower()

name_surname = names + surnames
print(name_surname)


# 3) შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, ან რომელიც მთავრდება დიდი ასოთი.



words = ["HELLO", "Python", "CODEX", "programming", "DataA", "LIST"]

words_1=[]


for i in range(len(words)):
    if len(words[i]) < 6 or words[i][-1] == words[i][-1].upper():
        continue
    else: words_1.append(i)




# 4) შექმენით float მონაცემთა ტიპის ელემენტებით სავსე სია რომელშიც იქნება 10 float ელემენტი და ამ სიიდან ახალ ცარიელ სიაში ჩაამატეთ ის რიცხვები რომლებიც არიან 10-ზე მეტი და 100-ზე ნაკლები.


floats = [5.5, 12.3, 99.9, 150.0, 45.6, 9.8, 100.1, 67.4, 10.5, 200.2]
new_list = []

for i in floats:
    if i > 10 and i < 100:
        new_list.append(i)

print(new_list)


# 5) შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი დავალებაა რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. გამოიყენეთ for ციკლი და შესაბამისი ფუნქციები.


cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Zugdidi"]
countries = ["Georgia", "France", "Italy", "Spain", "Germany",
             "Japan", "China", "Brazil", "Canada", "Australia"]



for i in range(len(cities)):
    countries.insert(i, cities[i])



print(countries)
