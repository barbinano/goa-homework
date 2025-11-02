text_2 = input("შეიყვანე ტექსტი: ")

length=len(text_2)


for i in range(length):
    if text_2[i] == 'a' or text_2[i] == 'A':
        continue
    print(text_2[i])
