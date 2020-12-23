Only Alphabets and Space
Only Alphabets and Space: Given a String S, remove all the special characters and numbers from S and print.
Input Format:
The first line contains the string S
Output Format:
The first line contains the string with only alphabets and spaces.
Boundary Conditions:
1 < Length of S < 1000
Example Input/Output 1:
Input:
Hello #$ World!
Output:
Hello  World
Example Input/Output 2:
Input:
Grand2017
Output:
Grand
import re
print("".join(re.findall('[a-zA-Z]+|\s',input())))
