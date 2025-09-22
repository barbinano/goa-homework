#1)შექმენი სია 7 რიცხვით. დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო. დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით). 2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange". დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.



numbers = [1, 2, 3, 4, 5, 6, 7]
total = numbers[-7] * numbers[-1]
print(total)
third_from_left = numbers[-5]
third_from_right = numbers[-3]
print( third_from_left)
print( third_from_right)




fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]

print( fruits[2:3])
print( fruits[-4:-3])


#3)
#შექმენი [3,4,5,6,7,1,2,9,8,11]

#მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.

#თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი

#თუ უარყოფით რიცხვი ან  10 ზე მეტი მაღალირიცხვი შემოიყვანა დაბეჭდეთ --> "you entered negative or more than 10  number "




list_1 = [3, 4, 5, 6, 7, 1, 2, 9, 8, 11]
index = int(input("Enter number: "))
if 0 <= index < 10:
    print(str(index) + " " + "is" + " " + str(list_1[index]))
else:
    print("you entered negative or 10 and above")


#4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]


#--- მინუს ინდექსების გამოყენებით შეადგინეთ შემდეგი წინადადება და დაბეჭდეთ --> "dog is running in forest very fast"

#--- აასწყვეთ ზემოთ მოცემული წინადადება ოღონდ დადებითი ინდექსებით

#--- დადებით ინდექსების გამოყენებით ააწყვეთ შემდეგი წინადადება ---> "cat is very angry"

words = ["dog", "most", "is", "angry", "running", "forest", "fast", "in", "cat", "human", "very"]
sentence1 = words[-11] + " " + words[-9] + " "+ words[-7] + " " + words[-4] + " " + words[-6] + " " + words[-1] + " " + words[-5] + " " 
print( sentence1)
sentence2 = words[0] + " " + words[2] + " " + words[4] + " " + words[7] + " " + words[5] + " " + words[10] + " " + words[6]
print( sentence2)
sentence3 = words[8] + " " + words[2] + " " + words[10] + " " + words[3]
print( sentence3)


#5)
#შექმენი სია ცხოველებით: ["dog", "cat", "horse", "cow", "sheep", "goat"].
#მომხმარებელს შემოიტანინე ინდექსი(რიცხვი)

#თუ მომხმარებლის მიერ შემოყვანილ ინდექსზე მდგომი ელემენტი არის  "cat", დაბეჭდე "შენ აირჩიე კატა".

#თუ არის "goat", დაბეჭდე "შენ აირჩიე თხა".

#სხვა შემთხვევაში დაბეჭდე "სხვა ცხოველი აირჩიე".



animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]
index_2 = int(input("Enter a number: "))
if 0 <= index_2 <= 5:  
    if animals[index_2] == "cat":
        print("შენ აირჩიე კატა")
    elif animals[index_2] == "goat":
        print("შენ აირჩიე თხა")
    else:
        print("სხვა ცხოველი აირჩიე")
else:
    print("არასწორი ინდექსია")

#6)
#შექმენი სია 6 ქალაქით.
#მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს).

#თუ პირველი ინდექსი ნაკლებია მეორეზე → დაბეჭდე ამ ინდექსებზე მდგომი ორივე ელემენტი.

#თუ მეორე ნაკლებია პირველზე → დაბეჭდე "შეცვალე ინდექსები ადგილებით"--->ზემოთ თუ დაპრინტე a და b ამ შემთხვევაში დაპრინტე b და a.

#თუ ინდექსები ერთნაირია → დაბეჭდე "ორივე ერთია" და გამოიტანე ამ ინდექსზე მდგომი ელემენტი ვთქვათ თუ შემოიყვანა მომხმარებელმა 5 #და 5 დაუბეჭდე მე 5 ინდექსზე მდგომი ელემენტი.

cities = ["თბილისი", "ბათუმი", "ქუთაისი", "რუსთავი", "გორი", "ზუგდიდი"]

index_3 = int(input("შეიყვანე პირველი ინდექსი: "))
index_4 = int(input("შეიყვანე მეორე ინდექსი: "))

if 0 <= index_3 <= 5 and 0 <= index_4 <= 5:
    if index_3 < index_4:
        print( cities[index_3], "და", cities[index_4])
    elif index_4 < index_3:
        print("შეცვალე ინდექსები ადგილებით")
        print( cities[index_4], "და", cities[index_3])
    else:
        print("ორივე ერთია")
        print( index_3 + " " + cities[index_3])
else:
    print("არასწორი ინდექსი")









#7)მომხმარებელი შემოიტანს სიტყვას.

#თუ პირველი ასო "a"-ა → დაბეჭდე "სიტყვა იწყება a-თი".

#თუ ბოლო ასო "z"-ია → დაბეჭდე "სიტყვა მთავრდება z-ით".

#სხვაგვარად → დაბეჭდე "სიტყვა არც a-თი იწყება და არც z-ით მთავრდება".

word = input("შეიყვანე სიტყვა: ")

if word[0] == "a":
    print("სიტყვა იწყება a-თი")
elif word[-1] == "z":
    print("სიტყვა მთავრდება z-ით")
else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")




#8)დავალება 4

#მომხმარებელი შემოიტანს სიტყვას.

#თუ პირველი და ბოლო ასო ერთმანეთს ემთხვევა → დაბეჭდე "პირველი და ბოლო ერთნაირია".

#თუ განსხვავდება → "პირველი და ბოლო განსხვავებულია".


word = input("შეიყვანე სიტყვა: ")

if word[0] == word[-1]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")




#9)შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr"
 

#----ამ სიიდან შეადგინე სიტყვა "goga, 

#----ამ სიტყვიდან შეადგინე სიტყვა "saba"

#----ამ სიტყვიდან შეადგინე სიტყვა "bativar"



letters = ("agivorsbgitr")

goga = letters[1] + letters[4] + letters[1] + letters[0]
print("goga:", goga)

saba = letters[6] + letters[0] + letters[7] + letters[0]
print("saba:", saba)

bativar = letters[7] + letters[0] + letters[10] + letters[2] + letters[3] + letters[0] + letters[5]
print("bativar:", bativar)



#10)შექმენი შემდეგი სტრინგი --> 'giorgi'

#შენი დავალებააა რომ for დდა while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე


string_1=("giorgi")


for i in range(6):
    print(string_1[i])

string_1=("giorgi")


i=0
while i<6:
    print(string_1[i])

    i=i+1