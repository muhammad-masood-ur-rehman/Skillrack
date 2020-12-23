Milk Man and His Bottles
A milkman serves milk in packaged bottles of varied sizes. The possible size of the bottles are {1, 5, 7 and 10} litres. He wants to supply desired quantity using as less bottles as possible irrespective of the size. Your objective is to help him find the minimum number of bottles required to supply the given demand of milk.
Input Format:
The first line contains the number of test cases N.
Next N lines, each contain a positive integer L which corresponds to the demand of milk.
Output Format:
N lines containing the minimum number of required bottles for each L.
Boundary Conditions:
1 <= N <= 100
0 < L <= 9999

Example Input/Output 1:
Input:
3
17
65
12

Output:
2
7
2
Explanation:
The first line in the input contains 3 which indicates the number of test cases.
For 17, the answer is 2 as it can be supplied using 10+7 litres bottles.
For 65 it is 6*10 litre bottles + one 5 litre bottle.
For 12, it is one 7 litre + one 5 litre bottle.
def b10(litres):
    if(litres%10==0):
        print((litres//10))
    else:
        print(((litres//10)+b751(litres%10)))
def b751(litres):
    if(litres==1 or 5 or 7):
        return(1)
    elif(litres==2 or 6 or 8):
        return(2)
    elif(litres==3 or 9):
        return(3)
    elif(litres==4):
        reurn(4)
    else:
        return(0)
testcase=int(input())
if(testcase<=1000 and testcase>0):
    for i in range(testcase):
        litres=int(input())
        if(litres>10):
            b10(litres)
        elif(litres>0):
            print(b751(litres))
else:
    print("Wrongly Entered ")
