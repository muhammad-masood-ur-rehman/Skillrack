Sparse Matrix
Write an algorithm and the subsequent Python program to check whether the given matrix is sparse or not. A matrix is said to be a “Sparse” if the number  of zero entries  in the matrix,  is greater than or equal to the number  of non-zero entries. Otherwise it is  “Not sparse”. Check for boundary conditions and print 'Invalid input' when not satisfied.
r=int(input())  #number of rows in matrix
c=int(input())  #number of columns in matrix
if(r<=0 or c<=0):
 print('Invalid input')
 exit
else:
 vals=[]
 flag=0
 for i in range(r*c):
  vals.append(int(input()))
  zero_entries=vals.count(0)
 if(zero_entries>=r*c-zero_entries):
  print('Sparse')
 else:
  print('Not sparse')
