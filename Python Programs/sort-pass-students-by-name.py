Sort Pass Students by Name
Sort Pass Students by Name: A list of N students name and their marks in three subjects are passed as the input. The average of the 3 subjects must be greater than or equal to 40 and also the total marks must be greater than or equal to 150 for the student to pass. Print the names of the students who have passed, with the names sorted in ascending order.
Input Format:
The first line contains N, the number of students.
The following N lines contains Name and marks of each student in three subjects separated by space.
Output Format:
Print the names of the students who passed (with the names sorted in ascending order).
Example Input/Output 1:
Input:
3
Ram 45 65 45
Geetha 60 30 50
Soundarya 80 90 80
Output:
Ram
Soundarya
n=int(input())
l=[]
for i in range(n):
    a,b,c,d=map(str,input().split())
    if (int(b)+int(c)+int(d)//3)>=40 and int(d)+int(b)+int(c)>=150:
        l.append(a)
for i in sorted(l):
    print(i)
#include<stdio.h>
#include <stdlib.h>
struct Student{
    char name[20];
    int a,b,c;
};
int fun(const void* a,const void* b){
    struct Student* obj1= (struct Student*)a;
    struct Student* obj2= (struct Student*)b;
    return strcmp(obj1->name,obj2->name);
}
double avg(int totaly){
    return totaly/3.0;
}
int total(struct Student* obj){
    return obj->a+obj->b+obj->c;
}
int main()
{
    int n;
    scanf("%d",&n);
    
    struct Student students[n];
    for(int i=0;i<n;++i){
        struct Student* obj=(struct Student*)
        malloc(sizeof(struct Student));
        scanf("%s %d %d %d\n",obj->name,&obj->a,&obj->b,&obj->c);
        students[i]=*obj;
    }
    qsort(students,n,sizeof(struct Student),fun);
    for(int i=0;i<n;++i){
        int totaly=total(&students[i]);
        double avgy=avg(totaly);
        if(avgy>=40 && totaly>=150){
            printf("%s\n",students[i].name);
        }
    }
    return 0;
}
