# # return masked string
# def maskify(cc):
#     return "#" * (len(cc) - 4) + cc[-4:]
        

#     pass





# def no_boring_zeros(n):
     

# if n != 0:
#     return int(str(n).rstrip('0'))
# else:
#     return 0


# def warn_the_sheep(queue):
#     wolf_index = queue.index("wolf")
    
    
#     number = len(queue) - wolf_index - 1
    
#     if number == 0:
#         return "Pls go away and stop eating my sheep"
#     else:
#         return "Oi! Sheep number " +  str(number) + "! You are about to be eaten by a wolf!"


# def number(lines):
#     result = []
     
#     for i in range(len(lines)):
#         number= i+1
#         letter=lines[i]
#         result.append(str(number) + ": " + str(letter) )
    
#     return result


# def distinct(arr):
#     numbers = []
    
#     for i in arr:
#         if i not in numbers:
#             numbers.append(i)
    
#     return numbers




# def human_years_cat_years_dog_years(humanYears):
#     if humanYears == 1:
#         cat = 15
#         dog = 15
#     elif humanYears == 2:
#         cat = 15 + 9
#         dog = 15 + 9
#     else:
#         cat = 15 + 9 + (humanYears - 2) * 4
#         dog = 15 + 9 + (humanYears - 2) * 5
    
#     return [humanYears, cat, dog]

















w