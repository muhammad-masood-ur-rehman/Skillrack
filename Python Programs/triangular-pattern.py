Triangular Pattern
A triangular pattern with ‘n’ rows is formed with ‘i’ numbers in the i - th row, starting from the first row.  In a triangular pattern, The number of elements in the first row will be 1; the number of elemnts in the second row will be 2 ; and so on.
For example, if the value of ‘n’ is 3 and if the elements in each row are : First row has only one element , namely,  1 ; second  row has two elements, namely,  2, 1 ; The third rwo has three elements, namely, 1, 2, 3.
1
2 1
1 2 3
Path in a triangular pattern is described as the sequence of numbers, with one number taken from each row, starting from the first row till the last row.   For example, the paths in the pattern above are
1 – 2 – 1
1 – 2 – 2
1 – 2 – 3
1 – 1 - 1
1 – 1 – 2
1 – 1 - 3
Value of a Path is the sum of the numbers in that path. In the above illustration, Maximum value of  the paths in the  is ‘6’. Write an algorithm and the subsequent Python program to compute the maximum value among the paths in the triangular pattern.
Input Format
First line contains an integer ‘n’ which indicates the number of rows in the triangular patters
Next few lines contains the input for the triangular pattern
Output Format
Print the maximum value of the path in a triangular pattern
n = int(input())
maxi = []
pattern = []
for i in range(1,n+1):
    temp = []
    for j in range(1,i+1):
        temp.append(int(input()))
    pattern.append(temp)
for i in pattern:
    maxi.append(max(i))

print(sum(maxi))
