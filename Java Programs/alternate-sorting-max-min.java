Alternate Sorting - Max Min
Given an array of N integers, rearrange the array in such a way that the first element is first maximum, second element is first minimum, third element is second maximum, fourth element is second minimum and so on. Complete the method alternateSort to achieve the desired output.
Input Format:
The first line contains N.
The second line contains the value of the N integers separated by one or more spaces.
Output Format:
The N numbers alternately sorted as per the given instructions.
Boundary Conditions:
4 <= N <= 100
Example Input/Output 1:
Input:
7
1 2 3 4 5 6 7
Output:
7 1 6 2 5 3 4
Example Input/Output 2:
Input:
6
10 99 44 22 56 63
Output:
99 10 63 22 56 44
Example Input/Output 3:
Input:
7
9 5 6 9 3 2 5
Output:
9 2 9 3 6 5 5
private static void alternateSort(int arr[], int LENGTH) {
    Arrays.sort(arr);
    
    int ans[]=new int[arr.length];
    
    int i=0;
    int end=arr.length-1;
    while(i<arr.length){
        ans[i]=arr[end--];
        i+=2;
    }
    end=0;i=1;
    while(i<arr.length){
        ans[i]=arr[end++];
        i+=2;
    }
    i=0;
    while(i<arr.length){
        arr[i]=ans[i++];
    }
}
