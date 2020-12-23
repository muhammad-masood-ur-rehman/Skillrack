Intelligent Chef
There are N persons in a hotel. Each person has their own preferences for food.
The hotel chef wants to prepare the food items as minimum as possible.
The program must accept the food preferences of each person as the input.
The program must print the minimum number of food items that must be prepared to serve everyone in the hotel.
Note: Each person eats only one food item but has many options.
Example
Input/Output 1:
Input:
5
Dosa Poori
Idli Poori
Idli Poori
Idli Dosa
Poori
Output:
2
Explanation:
Here N = 5 representing the 5 persons in the hotel.
At least 2 food items (Idli & Poori) must be prepared to serve everyone in the hotel.
import java.util.*;

class FoodItem implements Comparable<FoodItem>{
    String name;
    List<Integer> customers;
    
    public int compareTo(FoodItem item){
        return customers.size()-item.customers.size();
    }
}
public class Main {

    public static void main(String[] args) {
		//Your Code Here
        Scanner scan=new Scanner(System.in);
        int n=scan.nextInt();
        scan.nextLine();
        Map<String,FoodItem> map=new HashMap<>();
        
        List<Integer> remainingCustomers=new ArrayList<>();
        
        for(int i=1;i<=n;++i){
            String items[]=scan.nextLine().split("\\s+");
            for(String item:items){
                if(!map.containsKey(item)){
                    FoodItem foodItem=new FoodItem();
                    foodItem.name=item;
                    foodItem.customers=new ArrayList<>();
                    map.put(item,foodItem);
                }
                map.get(item).customers.add(i);
            }
            remainingCustomers.add(i);
        }
        int count=0;
        // for(FoodItem obj:map.values()){
        //     System.out.println(obj.name+" "+obj.customers);
        // }
        while(!remainingCustomers.isEmpty()){
            List<FoodItem> objects=new ArrayList<>(map.values());
            Collections.sort(objects,Collections.reverseOrder());
            FoodItem mostPreffered=objects.get(0);
            
            count++;
            
            map.remove(mostPreffered.name);
            
            remainingCustomers.removeAll(mostPreffered.customers);
            
            for(String str:map.keySet()){
                map.get(str).customers.removeAll(mostPreffered.customers);
            }
        }
        System.out.print(count);
	}
}
