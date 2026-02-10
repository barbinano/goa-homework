word = input("შეიყვანეთ სიტყვა: ")

for i in word:
    if word.count(i) == 1:
        print(i)
        break
