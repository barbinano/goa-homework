#1)შექმენით სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიის ბოლოში დაამატე სიტყვა --> "ianvari" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

list_1=[980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]
list_1.append("ianvari")

print(list_1)

#2)შექმენი სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიაში მეორე ინდექსზე დაამატე სიტყვა ---> "bati" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა


list_2=[980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

list_2.insert( 2 , "bati")

print(list_2)


#3)შექმენი სია ---->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე მე 5 ინდექსზე მდგომი ელემენტი და დაპრინტე საბოლოო სია ნახე ამოიშალა თუ არა


list_3=[980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

list_3.pop(5)

print(list_3)
#4)შექმენი სია --->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე True და ასევე ამოშალე "kote" და დაპრინტე საბოლოო სია და ნახე ამოიშალა თუ არა



list_4=[980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5]

list_4.remove( "kote")
list_4.remove( True )



print(list_4)