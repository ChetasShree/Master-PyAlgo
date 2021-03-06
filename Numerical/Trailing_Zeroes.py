# Function to get trailing zeroes
def trailingZeroes(number):
    rem = 0
    while number > 0:
        number //= 5
        rem += number
    return rem

number = int(input('Enter Number for calculating trailing Zeroes : '))    
solution = trailingZeroes(number)
print(solution)

'''Input: number = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Input: number = 5
Output: 1
Explanation: 5! = 120'''
