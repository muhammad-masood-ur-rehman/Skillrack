Creating Unique List and Searching
A login register is maintained in the library of VITCC in which, the register number of students are recorded when they enter the library. Sometimes it happens that the students visit the library more than once in a day and hence duplicate entries occur so frequently in the register. The librarian wants to have a report of all students who have visited on a particular day, ‘x’. Given the list  of students who visited the library on the day ‘x’, write an algorithm and the subsequent Python program to prepare a report with unique register number of students. Also read a register number ‘r’ and search for it in the list. Print ‘Found’ if ‘r’ is in the list and print ‘Not found’ otherwise.
n=int(input())
p=[]
for i in range(n):
    reg=input().rstrip().upper()
    if(reg not in p):
        p.append(reg)
r=input().rstrip().upper()
print(p)
if(r in p):
 print('Found')
else:
 print('Not found')
