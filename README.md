In the above programs, the decimal_to_gray function takes a decimal number n as input and returns the corresponding Gray code.

The function works by performing a bitwise XOR operation between the decimal number and the number obtained by shifting the decimal number one bit to the right (i.e., dividing it by 2 and discarding the remainder). 

The resulting number is the Gray code. The ^ operator is the bitwise XOR operator.
