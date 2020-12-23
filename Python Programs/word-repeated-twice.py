Word Repeated Twice
The program must accept a string S containing multiple words as the input. The program must print the word which is repeated twice in the string S as the output. If more than one such words are present in S, the program must print the first occurring one as the output. If there is no such word, the program must print -1 as the output.
Input Format:
The first line contains S.
Output Format:
The first line contains the word which is repeated twice in the string S or -1.
Example Input/Output 1:
Input:
apple banana cherry banana dates apple apple
Output:
banana
Explanation:
The word repeated twice in the string "apple banana cherry banana dates apple apple" is banana.
Hence the output is banana
Example Input/Output 2:
Input:
one two three two two three four three
Output:
-1
Example Input/Output 3:
Input:
dec jan feb mar jan feb mar
Output:
jan
Python:
lis=list(map(str,input().split()))
ctr=0
wr=""
for ele in lis:
    if lis.count(ele)==2:
        ctr=ctr+1
        wr=ele
        break
if ctr==0:
    print("-1")
else:
    print(wr)
inputstring=list(map(str,input().split()))
counts=[inputstring.count(ele) for ele in inputstring]
if 2 not in counts:
    print(-1)
else:
    print(inputstring[counts.index(2)])
C:
#include<stdio.h>
#include <stdlib.h>
int main()
{    
    char string[1001];
    scanf("%[^\n]",string);
    char words[100][100];  
    int i = 0, j = 0, k, length, count,no=0;  
      
    //Split the string into words such that each row of array words represents a word  
    for(k=0; string[k]!='\0'; k++){  
          
        //Here, i represents row and j represents column of two-dimensional array words  
        if(string[k] != ' ' && string[k] != '\0'){  
            //Converts the string into lowercase and add it to array words  
            words[i][j++] = tolower(string[k]);  
        }  
        else{  
            words[i][j] = '\0';  
            //Increment row count to store new word  
            i++;  
            //Set column count to 0  
            j = 0;  
        }  
    } 
    length = i+1;  
      
    
    for(i = 0; i < length; i++){  
        count = 1;  
        for(j = i+1; j < length; j++){  
           if(strcmp(words[i], words[j]) == 0 && (strcmp(words[j],"0") != 0)){  
               count++;  
               //Set words[j] to 0 to avoid printing visited word  
               strcpy(words[j],"0");  
           }   
        }  
        //Displays the duplicate word if count is greater than 1  
        if(count ==2 ) 
        {
            printf("%s\n", words[i]); 
            no++;
            break;
        }
    }  
    if(no==0)
    {
        printf("-1");
    }
    return 0;
}
