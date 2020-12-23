Red Green Blue
Red Green Blue: Given a character ch and the program must print as per the following conditions.
If ch is R, the program must print RED
If ch is G, the program must print GREEN
If ch is B, the program must print BLUE
For any other input, the program must print UNDEFINED.
Input Format:
The first line contains the character ch.
Output Format:
The first line contains the string.
Example Input/Output 1:
Input:
R
Output:
RED
Example Input/Output 2:
Input:
J
Output:
UNDEFINED
s=input.strip()
print('RED') if s=='R' else print ('GREEN') if s=='G' else print('BLUE') if s=='B' else print ('UNDEFINED')
