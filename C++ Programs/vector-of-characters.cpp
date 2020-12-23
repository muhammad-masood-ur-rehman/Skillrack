Vector of Characters
Design a class charVector that has a character vector as datamember. Provide member functions in the class to createVector, duplicateVector, duplicateRevVector and print. Functions shall be defined as follows: initializeVector – read a string and create a vector of characters duplicateVector – Add the content of the vector once at the end. For example if the content of charVector is “bat” then after the function is called the content must “batbat” duplicateRevVector – Add the content of the vector in reverse at the end. For example if the content of charVector is “bat” then after the function is called the content must “battab” print – Print content of vector, use iterators for traversal Use the vector class defined in STL for the implementation. Use [] operator in functions duplicateVector, duplicateRevVector and use iterator in print and initializeVector functions.
#include <iostream>
#include <string>
#include <vector>
 
using namespace std;
 
class charVector{
    vector<char> cv;
public:
    void initializeVector(string);
    void dupVector();
    void dupRevVector();
    void print();
};
 
 
void charVector::initializeVector(string s) {
    int i=0, l=s.length();
    for(; i<l; i++)
        cv.push_back(s[i]);
}
void charVector::dupVector() {
    int i=0, l=cv.size();
    for(; i<l; i++)
        cv.push_back(cv[i]);
}
void charVector::dupRevVector() {
    int i, l=cv.size();
    for(i=l-1; i>=0; i--)
        cv.push_back(cv[i]);
}
void charVector::print() {
    for(vector<char>::iterator i=cv.begin(); i!=cv.end(); i++)
        cout<<*i;
}
 
 
int main()
{
    charVector ch1,ch2;
    string s1,s2;
    cin>>s1>>s2;
    ch1.initializeVector(s1);
    ch2.initializeVector(s2);
    ch1.dupVector();
    ch2.dupRevVector();
    ch1.print();
    cout<<endl;
    ch2.print();
    cout<<endl;
}
