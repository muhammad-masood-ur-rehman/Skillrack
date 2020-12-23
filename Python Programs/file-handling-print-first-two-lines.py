File Handling - Print First Two Lines
The program must accept a string S denoting the filename as the input. The program must read the content from the file and print the first two lines of the content as the output.
Note:
There is always at least two line content in the file S.
The file S will be in the same folder where the program executes.
Boundary Condition(s):
5 <= Length of S <= 100
Input Format:
The first line contains S.
File Content Format:
The lines contain the string values.
Output Format:
The first two lines each contain a string value as per the given condition.
Example Input/Output 1:
Input:
string.txt
Content of string.txt:
Hi
Hello
Welcome
Output:
Hi
Hello
Example Input/Output 2:
Input:
input.txt
Content of input.txt:
Apple
Mango
Output:
Apple
Mango
fileName = input().strip()
inpFile = open (fileName, "r")
line1 = inpFile.readline()
line2 = inpFile.readline()
print(line1, line2, sep = "")
inpFile.close()
