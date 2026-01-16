#2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.



words=["saba" , "giga" , "NATIA"  , " KOBAXIDZE" , "gIORGI"]
words_2=[]

for i in words:
    if i==i.lower() and i[0] == "g":
        words_2.append("goga")

    elif i==i.upper() or i[0] == "N":
        words_2.append("Nika")
        
    else: words_2.append("ლიდერი")

print(words_2)




# 3)  შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი.


numbers = [1, 2, 3, 4, 5, 6]
numbers_2 = []

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0 or i % 2 == 0:
        numbers_2 .append(numbers[i] ** 2)   
    else:
        numbers_2 .append(numbers[i] * 2)   
    i += 1

print(numbers_2 )


#4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.
words_3 = ["HELLO", "Python", "PROGRAMMING", "Nika", "CODE"]
words_4 = []

i = 0
while i < len(words_3):
    if len(words_3[i]) > 6 or words_3[i].isupper():
        words_4.append(words_3[i].lower())
    else:
        words_4.append(words_3[i] * 2)
    i += 1

print(words_4)


#5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.


numbers_3 = "0123456789"
numbers_4 = []

for i in range(len(numbers_3 )):
    
    if i % 2 == 0 or int(numbers_3 [i]) > 7:
        numbers_4.append(numbers_3 [i])

print(numbers_4)




numbers_3 = "0123456789"
numbers_4  = []

i = 0
while i < len(numbers_3):
    if i % 2 == 0 or int(numbers_3[i]) > 7:
        numbers_4 .append(int(numbers_3[i]))
    i += 1

print(numbers_4 )   
