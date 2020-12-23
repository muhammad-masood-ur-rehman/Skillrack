Chess, Carrom and Scrabble Players
Each student in a class of ‘n’ plays at least one indoor game chess, carrom and scrabble. Given three list of names of students who play chess, scrabble and carrom, develop an algorithm and write a C++ code to find the students who can
(i) Play chess and carrom
(ii) Chess, carrom but not scrabble
Understand the template code and implement the member functions of the class
Input Format
Number of students who play chess
Name of student1 who plays chess
Name of student2 who plays chess
…
Name of student-n who plays scrabble
Number of students who play scrabble
Name of student1 who plays scrabble
Name of student2 who plays scrabble
…
Name of student-n who plays scrabble
Number of students who play carrom
Name of student1 who plays carrom
Name of student2 who plays carrom
…
Name of student-n who plays carrom
Output Format
Name of students who play chess and carrom. order the names as given in the chess input list . separate names by a comma Name of students who play chess and carrom but not scrabble. Order the names as given in the chess input list. separate names by a comma
Boundary Conditions
Number of students in class will not be more than 30
Length of name of students in class will not be more than 20
Assume that none of the set will become empty
#include<iostream>
#include<cstring>
using namespace std;
class set
{
    int num_Of_Ele;
    char names[30][20];
public:
    void get();
    void print()const;
    set intersection(set&);
    set difference(set&);
};
 
void set::get() {
    int i;
    cin>>num_Of_Ele;
    for(i=0; i<num_Of_Ele; i++)
        cin>>names[i];
}
void set::print()const {
    int i;
    if(num_Of_Ele>0) {
        cout<<names[0];
        for(i=1; i<num_Of_Ele; i++)
            cout<<","<<names[i];
        cout<<endl;
    }
}
set set::intersection(set &a) {
    int i, j;
    set b;
    b.num_Of_Ele=0;
    for(i=0; i<num_Of_Ele; i++)
        for(j=0; j<a.num_Of_Ele; j++)
            if(!(strcmp(names[i],a.names[j]))) {
                strcpy(b.names[b.num_Of_Ele++],names[i]);
                break;
            }
    return b;
}
set set::difference(set &a) {
    int i, n, j;
    set b;
    b.num_Of_Ele=0;
    for(i=0; i<num_Of_Ele; i++) {
        n=0;
        for(j=0; j<a.num_Of_Ele; j++)
            if(!(strcmp(names[i],a.names[j]))) {
                n++;
                break;
            }
        if(!n)
            strcpy(b.names[b.num_Of_Ele++],names[i]);
    }
    return b;
}
 
 
int main()
{
    set chess, carrom,scrabble;
    chess.get();
    carrom.get();
    scrabble.get();
    set inter = chess.intersection(carrom);
    inter.print();
    set diff = inter.difference(scrabble);
    diff.print();
    return 0;
}
