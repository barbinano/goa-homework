#6) <= Boss Level =>
#შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
#--> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი


list_4=["georgia" , "USA" , "russia" , "india" , "pakistan", "beard" , "crest"]

length_6=len(list_4)


longest=list_4[0]


for i in range(length_6):
    if len(list_4[i]) > len(longest):
        longest=(list_4[i])

print(longest)
    