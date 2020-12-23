Amicable Numbers
Two numbers are said to be amicable if the sum of proper divisors of one number plus 1, is equal to the other number. All divisors of a number other than 1 and itself, are called proper divisors. For example, the numbers 220 and 284 are amicable as the sum of proper divisors of 220 (i.e.) 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110 is equal to 284 and sum of proper divisors of 284 (i.e.) 1, 2, 4, 71 and 142 is 220. Given two numbers, write an algorithm and the subsequent Python code to Print Yes if the given two numbers are amicable. Print ‘No’ if the given numbers are not amicable. Check for boundary conditions and print 'Invalid input' for wrong input. Write appropriate functions for accomplishing the task.
Input Format
First line contains the first number
Next line contains the second number
Output Format
Print either Yes or No
Input:
First line contains the first number
Next line contains the second number
Output:
Print either Yes or No
def prop_div_sum(n):
    total = 0
    for i in range(2,n):
        if n%i==0:
            total += i
    return total

n = int(input())
m = int(input())
if (prop_div_sum(n)+1) == m or (prop_div_sum(m)+1) == n:
    print('Yes')
else:
    print('No')
