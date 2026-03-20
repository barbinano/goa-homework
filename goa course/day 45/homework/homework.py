# def accum(s):
#     result = ""
    
#     for i in range(len(s)):
#         part = ""
        
#         for b in range(i + 1):
#             if b == 0:
#                 part += s[i].upper()
#             else:
#                 part += s[i].lower()
        
#         if i > 0:
#             result += "-"
#         result += part
    
#     return result


# def litres(time):
#     return int(time * 0.5)


# def lovefunc(flower1, flower2):
#     return (flower1 % 2) != (flower2 % 2)


# def maps(arr):
#     result = []
    
#     for i in arr:
#         result.append(i * 2)
    
#     return result


# def solution(string, ending):
#     if len(ending) > len(string):
#         return False

#     string = string[::-1]
#     ending = ending[::-1]

#     for i in range(len(ending)):
#         if string[i] != ending[i]:
#             return False

#     return True