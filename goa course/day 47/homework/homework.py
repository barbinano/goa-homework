# def get_middle(s):
#     if len(s) % 2 == 0:
#         return s[ len(s) // 2 - 1] + s[ len(s) // 2 ]
    
#     else:
#         return s[ len(s) // 2 ]
    
    




# def is_anagram(test, original):
#     if sorted(original.lower()) == sorted(test.lower()):
        
#         return  True
#     else: return False








# def maskify(cc):
#     return "#" * (len(cc) - 4) + cc[-4:]
        

#     pass




# def check_exam(arr1,arr2):
#     score = 0

#     for i in range(len(arr1)):
#         if arr2[i] == "":
#             score += 0
#         elif arr2[i] == arr1[i]:
#             score += 4
#         else:
#             score -= 1

#     if score < 0:
#         return 0
#     return score
    
#     pass



# def create_phone_number(n):
#     phone_number = "("
    
#     for i in range(3):
#         phone_number += str(n[i])
    
#     phone_number += ") "
    
#     for i in range(3, 6):
#         phone_number += str(n[i])
    
#     phone_number += "-"
    
#     for i in range(6, 10):
#         phone_number += str(n[i])
    
#     return phone_number



# def get_count(sentence):
#     count = 0
#     for i in sentence:
#         if i in "aeiou":
#             count += 1
#     return count
#     pass