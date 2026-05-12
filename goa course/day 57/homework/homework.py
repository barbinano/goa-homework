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


# def to_float_array(arr):
#     result = []
    
#     for i in arr:
#         if "." in i:
#             result.append(float(i))
#         else:
#             result.append(int(i))
    
#     return result


# def capitalize(s):
#     even = ""
#     odd = ""
    
#     for i in range(len(s)):
#         if i % 2 == 0:  # even index
#             even += s[i].upper()
#             odd += s[i]
#         else:           # odd index
#             even += s[i]
#             odd += s[i].upper()
    
#     return [even, odd]


# def adjacent_element_product(array):
#     max_product = array[0] * array[1]
    
#     for i in range(len(array) - 1):
#         product = array[i] * array[i + 1]
        
#         if product > max_product:
#             max_product = product
    
#     return max_product

# def show_sequence(n):
#     if n == 0:
#         return str(n) + "=0"
#     if n < 0:
#         return str(n) + "<0"
    
#     total = 0
#     result = ""
    
#     for i in range(n + 1):
#         total += i
#         result += str(i)
        
#         if i != n:
#             result += "+"
    
#     return result + " = " + str(total)


# def solution(digits):
#     max_val = 0
    
#     for i in range(len(digits) - 4):
#         num = 0
        
#         for b in range(5):
#             digit = int(digits[i + b])
#             num = num * 10 + digit
        
#         if num > max_val:
#             max_val = num
    
#     return max_val

# def factorial(n):
#     result = 1
    
#     for i in range(1, n + 1):
#         result = result * i
    
#     return result


# def nb_dig(n, d):
#     count = 0
    
#     for i in range(n + 1):
#         square = i * i
#         b = str(square)
        
#         for ch in b:
#             if ch == str(d):
#                 count += 1
    
#     return count


