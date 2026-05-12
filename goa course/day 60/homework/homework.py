# codewars 1

# def is_valid_walk(walk):
#     if len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("w") == walk.count("e"):
#         return True
#     else:
#         return False

# codewars 2

# def compute_sum(n):
#     sum1 = 0
#     for i in range(1, n + 1):
#         for ii in str(i):
#             sum1 += int(ii)
#     return sum1

# codewars 3

# def delete_nth(order,max_e):
#     filltered = []
#     for i in order:
#         if filltered.count(i) < max_e:
#             filltered.append(i)
#     return filltered

# codewars 4
# def digital_root(n):
#     while n >= 10:  
#         digit_total = 0
        
#         for digit in str(n): 
#             digit_total+= int(digit)  
        
#         n = digit_total  
    
#     return n



# codewars 5

# def clean_string(s):
#     result = []

#     for character in s:
#         if character == "#":
#             if result:  
#                 result.pop()
#         else:
#             result.append(character)

#     return "".join(result)
