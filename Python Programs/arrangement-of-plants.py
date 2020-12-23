Arrangement of Plants
A gardener has the practice of assigning ID to the plants during plantation. One day, he makes a note of the heights of plants in his garden. He writes the height of the plant against the ID of the plant. He then instructs his employee to keep the plants, in ascending order of its height. Design an algorithm and write the Python code to display the list of ID numbers of plants in ascending order of their height. IDs are also numbers. Check for boundary conditions and print 'Invalid input' for wrong input. For example, if there are three trees with IDs as 175, 160, 120 and height as 47, 73 and 23 then the output should be [120, 175, 160].
n=int(input())
ids=[]
heights=[]
for i in range(n):
 ids.append(int(input()))
 heights.append(int(input()))
sorted_ids=[x for (y,x) in sorted(zip(heights,ids))]
#The zip() function returns an iterator of tuples based on the iterable object.
for i in sorted_ids:
 print(i)
