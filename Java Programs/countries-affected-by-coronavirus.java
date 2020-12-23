Countries Affected by Coronavirus
The program must accept the names of N persons affected by the coronavirus and their country names as the input. The program must print the names of the countries with the number of persons affected by the coronavirus. The countries must be sorted in descending order based on the number of persons affected by the coronavirus. If more than one countries have the same number of corona affected persons, then those countries must be sorted in the order of their occurrences.
Boundary Condition(s):
2 <= N <= 50
1 <= Length of each person's name <= 50
1 <= Length of each country's name <= 20
Input Format:
The first line contains N.
The next N lines, each contains two string values representing the name and the country of a person.
Output Format:
The lines containing the names of the countries and the number of persons affected by the coronavirus.
Example Input/Output 1:
Input:
6
Mr.Ahbain USA
Mr.Lee Ming China
Ms.Maa Long China
Mr.Verana Latta India
Ms.Jwlin Rij China
Ms.Abc USA
Output:
China 3
USA 2
India 1
Explanation:
In USA, 2 persons affected by the coronavirus(Mr.Ahbain and Ms.Abc). So the count is 2.
In China, 3 persons affected by the coronavirus(Mr.Lee Ming, Ms.Maa Long and Ms.Jwlin Rij). So the count is 3.
In India, 1 person affected by the coronavirus(Mr.Verana Latta). So the count is 1.
So the names of countries with the number of corona affected persons are printed based on the given conditions.
China 3
USA 2
India 1
Example Input/Output 2:
Input:
4
Ms.Juro Japan
Mr.cling Mon China
Ms.Kyo Kirou Canada
Ms.Aki Hiroshi Japan
Output:
Japan 2
China 1
Canada 1
import operator
a=[str(input()) for i in range (int(input()))]
h=[]
dict={}
for i in a:
    words = i.split()
    words=(words[-1])
    h.append(words)
for i in h:
    dict[i] = h.count(i)
country=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)
for ele in country:
    print(ele[0],ele[1],sep=" ")
import java.util.*;
public class Hello {
    static class Country{
        String name;
        int count;
        Country(String name,int count){
            this.name=name;
            this.count=count;
        }
    }
    public static class Sorting implements Comparator<Country>{
        @Override
        public int compare(Country c1,Country c2){
            if(c1.count>c2.count){
                return -1;
            }
            else if(c1.count<c2.count){
                return 1;
            }
            return 0;
        }
    }
    public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		sc.nextLine();
		Map<String,Integer> map=new LinkedHashMap<>();
	    for(int ctr=1;ctr<=N;ctr++){
	        String[] str=sc.nextLine().split(" ");
	        String s=str[str.length-1];
	        map.put(s,map.getOrDefault(s,0)+1);
	    }
	    List<Country> list=new ArrayList<>();
	    for(Map.Entry<String,Integer> entry:map.entrySet()){
	        Country c=new Country(entry.getKey(),entry.getValue());
	        list.add(c);
	    }
	    Collections.sort(list,new Sorting());
	    for(Country c:list){
	        System.out.println(c.name+" "+c.count);
	    }
	}
}
