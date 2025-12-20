words = ["GameAB", "hello", "good", "pythON", "GoLD", "code"]


for i in words :
     if i[0]==("G") and i[-2:]==i[-2:].upper():
        words.remove(i)
     elif words[words.index(i)] == words[words.index(i)].lower():
          words[words.index(i)] =  words[words.index(i)].upper()
    

print(words)
