def decimal_to_gray(n):
    
    return n ^ (n >> 1)



decimal_num = 10
gray_code = decimal_to_gray(decimal_num)
print(f"The Gray code for decimal {decimal_num} is {gray_code}")
