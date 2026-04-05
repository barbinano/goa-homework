# def solution(number):
#     if number < 0:
#         return 0
    
#     total = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total



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


# def high_and_low(numbers):
#     nums = numbers.split()
    
#     high = low = int(nums[0])
    
#     for i in nums:
#         i = int(i)
#         if i > high:
#             high = i
#         if i < low:
#             low = i
    
#     return f"{high} {low}"



# def find_short(s):
#     words = s.split()
#     shortest = len(words[0])
    
#     for word in words:
#         if len(word) < shortest:
#             shortest = len(word)

#     return shortest 



# def points(games):
#     total = 0
    
#     for each_game in games:
#         x, y = each_game.split(":")
#         x, y = int(x), int(y)
        
#         if x > y:
#             total += 3
#         elif x == y:
#             total += 1
    
#     return total


# def calculator(equation):
#     a, op, b = equation.split()
    
#     x = len(a)  # count dots
#     y = len(b)
        
    
#     if op == "+":
#         result = x + y
#     elif op == "-":
#         result = x - y
#     elif op == "*":
#         result = x * y
#     elif op == "//":
#         result = x // y
    
#     return "." * result
    








