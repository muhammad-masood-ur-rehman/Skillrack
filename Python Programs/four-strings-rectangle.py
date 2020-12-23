Four Strings Rectangle
Four strings out of which two have the same length L1 and the remaining two have the same length L2 are passed as the input to the program. The four strings must be printed in a L1*L2 rectangular matrix shape as shown in the example input/output.
L1 >= L2 and a string with L1 must appear on the top of the rectangle. The string which is on the top with length L1 will always be the first string in the input. Other three strings can occur in a random order in the input. The sequence of the string can be identified by the fact that the last letter of a string will be the first letter of another string (and you can safely assume the last letter will not occur more than once).
Input Format:
The first line contains the string which represents the top of the rectangular matrix.
The next three lines will contain the remaining the three string values which can represent the right, left and bottom side of the rectangle, but not necessarily in the same order.
Output Format:
The L1*L2 rectangular matrix with these four strings as it's sides as described in the Example Input/Output.
Boundary Conditions:
3 <=  L1, L2 <= 100
L1 >= L2
Example Input/Output 1:
Input:
MANAGE
SUM
TAURUS
EAT
Output:
MANAGE
U****A
SURUAT
List = []
for i in range(4):
    List.append(input().strip());
Len = []
for i in List:
    if not (len(i) in Len):
        Len.append(len(i))
 
Matrix = [["*" for i in range(max(Len))] for j in range(min(Len))]
for i in range(len(List[0])):
    Matrix[0][i] = List[0][i]
List[1:] = sorted(List[1:],key = lambda x: len(x))
    
for i in range(1,4):
    if List[i][-1] == Matrix[0][0]:
        for j in range(len(Matrix)):
            Matrix[j][0] = List[i][::-1][j]
    elif List[i][0] == Matrix[0][0]:
        for j in range(len(Matrix)):
            Matrix[j][0] = List[i][j]
    elif List[i][-1] == Matrix[0][-1]:
        for j in range(len(Matrix)):
            Matrix[j][-1] = List[i][::-1][j]
    elif List[i][0] == Matrix[0][-1]:
        for j in range(len(Matrix)):
            Matrix[j][-1] = List[i][j]
    elif List[i][-1] == Matrix[-1][0]:
        for j in range(len(Matrix[0])):
            Matrix[-1][j] = List[i][::-1][j]
    elif List[i][0] == Matrix[-1][0]:
        for j in range(len(Matrix[0])):
            Matrix[-1][j] = List[i][j];
 
 
for i in range(len(Matrix)):
    print("".join(Matrix[i]))
