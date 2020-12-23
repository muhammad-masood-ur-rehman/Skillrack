Letter Identification
Given three words, write an algorithm and the subsequent Python code to identify the following letters:
1. Letters common to all the three words
2. Letters in first two words but not in third word
3. Letters in first word but not in second and third word
4. Letters in all the three words
For example, if the words are apple, camel, element then letters in common to all the three words -  i, eLetters in first two words but not in third word – aLetters in first word but not in second and third word  - pLetters in all the three words – a, p, p, l, e, c, m, n, t
Hint: Use sets in Python. While reading input, use rstrip() function to remove extra spaces 
Input Format: First line contains word1Second line contains word2Third line contains word3
Output Format: List of letters common to all the three words in lexicographical orderList of letters common to first two words but not in third word in lexicographical orderList of letters in first word but not in second or third word in lexicographical orderList of all letters in the three words in lexicographical order.
word1=input().rstrip().lower()
word2=input().rstrip().lower()
word3=input().rstrip().lower()
s1=set(word1)
s2=set(word2)
s3=set(word3)
L1=[]
L2=[]
L3=[]
L4=[]
for i in s1:
    if(i in s2 and i in s3):
        L1.append(i)
for i in s1:
    if(i in s2 and i not in s3):
        L2.append(i)
for i in s1:
    if(i not in s2 and i not in s3):
        L3.append(i)
s4=s1.union(s2).union(s3)
L4=list(s4)
print(sorted(L1))
print(sorted(L2))
print(sorted(L3))
print(sorted(L4))
