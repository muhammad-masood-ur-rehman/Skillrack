Word histogram
Histogram is a graphical representation drawn based on the frequency of occurrence of things. Histogram for a word is drawn based on the number of occurrences of each character in the word. An inverted dictionary is used to maintain the list of characters that has same frequency. Write an algorithm and the subsequent Python code to compute and print the frequency of occurrence of character as a dictionary (ch:count). Make the entire process to be case insensitive. For example, if the input word is ‘parrot’, then the dictionary with characters and frequency of occurrence is

{'a': 1, 'o': 1, 'p': 1, 'r': 2, 't': 1}
and the inverted dictionary is
{1: ['a', 'o', 'p', 't'], 2: ['r']}
Print dictionary in sorted order by key. Sort the values of each key in the inverted dictionary.
[Hint: use pprint function for printing dictionary in sorted order.
Syntax for pprint is
pprint(dictionary name)
Include the line “from pprint import pprint” in the top of your program
Check for boundary conditions and print 'Invalid input' if conditions are not met.
Input Format:
First line contains the input word
Output Format:
Dictionary of characters in the word as keys and count as values in sorted order by key.
Inverted dictionary in sorted order by key.
word=input().rstrip().lower()
if(any(c.isnumeric() for c in word)==True):
    print('Invalid input')
    exit()
dic={}
for letter in word:
    if(letter not in dic):
        freq=word.count(letter)
        dic[letter]=freq

import pprint
#Finding the inverse dictionary:
inv_dic={}
for k,v in dic.items():
    inv_dic[v]=inv_dic.get(v,[])
    inv_dic[v].append(k)
    inv_dic[v]=sorted(inv_dic[v])

pprint.pprint(dic)
pprint.pprint(inv_dic)
