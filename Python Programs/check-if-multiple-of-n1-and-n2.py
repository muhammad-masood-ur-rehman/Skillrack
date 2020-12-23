Check if Multiple of N1 and N2
The program must accept three integers N1, N2 and N3 as the input. The program must print yes if N2 is a multiple of N1 and N3 is a multiple of N2. Else the program must print no as the output.
Example Input/Output:
Input:
8 32 64
Output:
yes
 
b,n,m = map(int, input().split()) 
if(n%b==0 and m%n==0): print("yes") 
else: print("no")
