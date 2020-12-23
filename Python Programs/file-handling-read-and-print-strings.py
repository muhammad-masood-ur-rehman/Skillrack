File Handling - Read and Print Strings
The program must accept a string S denoting the filename as the input. The program must read all the content from the file S and print them as the output.
Note: The file S will be in the same folder where the program executes.
Boundary Condition(s):
5 <= Length of S <= 100
Input Format:
The first line contains S.
File Content Format:
The lines contain the string values.
Output Format:
The lines contain the string values.
Example Input/Output 1:
Input:
input.txt
Content of input.txt:
hi
hello
welcome
Output:
hi
hello
welcome
Example Input/Output 2:
Input:
sample.txt
Content of sample.txt:
Letuscrack
Python Code
Output:
Letuscrack
Python Code
fileName = input().strip()
inputFile = open(fileName, 'r')
fileContent = inputFile.read()
print(fileContent)
inputFile.close()
