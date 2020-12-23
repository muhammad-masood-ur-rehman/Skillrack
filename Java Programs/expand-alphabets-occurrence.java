Expand alphabets occurrence
A string consisting of short hand form of occurrence of alphabets will be passed as input. The program must expand the code and print the alphabets.
Input Format:
The first line will contain the short hand form of the code of length L.
Boundary Conditions:
2 <= L <= 20
Output Format:
The alphabets occurrence based on the short hand code.

Example Input/Output 1:
Input:
a3b5a2
Output:
aaabbbbbaa
Explanation:
a3 implies a has to occur 3 times and hence a is printed thrice.
b5 implies b has to be occur five times and hence b is printed five times.
a2 again implies a has to occur 2 times and hence a is printed thrice.

Example Input/Output 2:
Input:
z2m6c4
Output:
zzmmmmmmcccc
Example Input/Output 3:
Input:
abc5
Output:
aaaaabbbbbccccc
Explanation:
Here there is no number after a and b. This implies the next immediate number of occurrence is applicable to both a and b.
Hence 5 which occurs after c is applicable to a and b too. So all the three alphabets a,b,c are printed five times.
import java.util.*;

 class Hello {


    public static void main(String[] args) {

     Scanner sc=new Scanner(System.in);

    String str=sc.nextLine();

    char[] ch=str.toCharArray();

    int i,n=ch.length,num,j,l,k;

    String st="";

    for(i=0;i<n;i++)

        {

            if(ch[i]>='a'&&ch[i]<='z')

                st+=ch[i];

            else   

                {

                    num=Character.getNumericValue(ch[i]);

                    l=st.length();

                char[] c=st.toCharArray();

                st="";

                for(k=0;k<l;k++)

                {

                    for(j=0;j<num;j++)

                        {

                            st+=c[k];

                        }

                }

                System.out.print(st);

                    st="";

                }
              
        }

 }
}
