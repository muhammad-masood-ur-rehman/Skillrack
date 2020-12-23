Toggle Case
Simon wishes to convert lower case alphabets to upper case and vice versa. Help Simon by writing a program which will accept a string value S as input and toggle the case of the alphabets. Numbers and special characters remain unchanged. 
Input Format: First line will contain the string value S 
Output Format: First line will contain the string value with the case of the alphabets toggled. 
Constraints: Length of S is from 2 to 100 
SampleInput/Output:
Example 1:
Input: GooD mORniNg12_3
 Output: gOOd MorNInG12_3 
Example 2:
Input:R@1nBow 
Output:r@1NbOW
n=input()
print(n.swapcase())
