JAVA - File Handling - Sort Students
Java Program to sort the students using file Handling
JAVA - File Handling - Sort Students: A list of name and marks for N students is given in a file. The program must print the names sorted by marks in descending order.
Boundary Condition(s):
1 <= N <= 1000
Input File Format:
The first line contains N.
The next N lines contain name and marks each separated by space(s).
Output Format:
The first line contains an integer.
Example Input/Output 1:
Input:
3
Ram 85
Jeya 92
Sathya 89
Output:
Jeya
Sathya
Ram
Example Input/Output 2:
Input:
4
Yamini 76
Ragu 67
Yeshwant 89
Philips 70
Output:
Yeshwant
Yamini
Philips
Ragu
import java.io.;
import java.util.;
 public class Hello {
         public static void main(String args[]){
         Scanner sc=new Scanner(System.in); 
         try{
             BufferedReader br=new BufferedReader(new FileReader(sc.nextLine()));
             String l=br.readLine(); 
             int count=0; 
             int total=0;
             if(count==0){
                 total=Integer.parseInt(l); 
                 count++;
             }    
             String arr[][]=new String[total][2];
             l=br.readLine();
             while(l!=null){   
                 String s[]=l.split(" "); 
                 arr[count-1][0]=s[0]; 
                 arr[count-1][1]=s[1];
                 count+=1; 
                 l=br.readLine();
             } 
             String first[]=new String[total];
             int sec[]=new int[total];
             for(int i=0;i<total;i++){
                 first[i]=arr[i][0];
                 sec[i]=Integer.parseInt(arr[i][1]);
             }  
             for(int i=0;i<total;i++){
                 for(int j=i+1;j<total;j++){
                     if(sec[i]<sec[j]){
                         String t=first[i];
                         first[i]=first[j];
                         first[j]=t; 
                         int tt=sec[i];
                         sec[i]=sec[j];
                         sec[j]=tt;
                     }
                 }
             } 
             for(int i=0;i<total;i++){
                 System.out.println(first[i]);
             }
         }
         catch(Exception e){
         }
     }
 }
