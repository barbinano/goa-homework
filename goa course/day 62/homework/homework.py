# def reverse_number(n):

#     if n < 0:
#         negative = True
#         n = -n   
#     else:
#         negative = False

#     reversed_num = int(str(n)[::-1])

#     if negative:
#         return -reversed_num
#     else:
#         return reversed_num



# def create_phone_number(n):
#     result = "("
    
#     for i in range(3):
#         result += str(n[i])
    
#     result += ") "
    
#     for i in range(3, 6):
#         result += str(n[i])
    
#     result += "-"
    
#     for i in range(6, 10):
#         result += str(n[i])
    
#     return result


# def create_phone_number