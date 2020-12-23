Sort Books - Price Rating Year Title
The title, ISBN, rating, price and publication year of N books are passed as the input. Then a year Y is passed as the input. The program must print the books published in the year Y based on the conditions given below.
- If two or more books have same price, then they must be sorted based on rating (the higher rating book must be displayed first)
- If two or more books have same price and rating, then they must be sorted based on year of publication (the recently published book must be displayed first)
- If two or more books have same price, rating and year of publication, then they must be sorted based on their title in ascending order. It is assured that no two books will have same title.
Please fill in the code in Hello.java for the method getYearwiseBooks and also the code for Book.java based on the above conditions so that the program executes successfully.
Hello.java
import java.util.*;

public class Hello {
private static Map<Integer, List<Book>> getYearwiseBooks(List<Book> books) {
    Map<Integer,List<Book>> map=new HashMap<>();

    for(int i=0;i<books.size();++i){
        if(!map.containsKey(books.get(i).pub_yr))
        map.put(books.get(i).getYear(),new ArrayList<>());

        map.get(books.get(i).getYear()).add(books.get(i));
    }
    for(int yr: map.keySet()){
        List<Book> list= map.get(yr);
        list.sort((Book a,Book b)->{
            int aPrice=a.getPrice(),bPrice=b.getPrice(),aRating=a.getRating(),bRating=b.getRating(),aYr=a.getYear(),bYr=b.getYear();
            if(aPrice==bPrice){
                if(aRating == bRating){
                    if(aYr == bYr){
                        return a.getTitle().compareTo(b.getTitle());
                    }
                    else{
                        return aYr - bYr;
                    }
                }
                else{
                    return bRating-aRating;
                }
            }
            else{
                return aPrice - bPrice;
            }
        });
    }
    return map;

}
public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        List<Book> books = new ArrayList<>();
        for (int ctr = 1; ctr <= N; ctr++) {
            Book book = new Book();
            book.setTitle(sc.next());
            book.setISBN(sc.next());
            book.setPrice(sc.nextInt());
            book.setRating(sc.nextInt());
            book.setYear(sc.nextInt());
            books.add(book);
            sc.nextLine();
        }
        Map<Integer, List<Book>> yearWiseBooks = getYearwiseBooks(books);
        int year = sc.nextInt();
        for (Book book : yearWiseBooks.get(year)) {
            StringBuilder sb = new StringBuilder();
            sb.append(book.getTitle()).append(" ");
            sb.append(book.getISBN()).append(" ");
            sb.append(book.getPrice()).append(" ");
            sb.append(book.getYear()).append(" ");
            sb.append(book.getRating());
            System.out.println(sb.toString());
        }
    }//end of main

}//end of class Hello
Book.java
public class Book{
    String title, ISBN;
    int rating, price, pub_yr;
    
    public void setTitle(String S){
        title = s;
    }
    public void setISBN(String S){
        ISBN =s;
    }
    public void setPrice(int n){
        price =n;
    }
    public void setRating(int n){
        rating = n;
    }
    public void setYear(int n){
        pub_yr = n;
    }
    
    public String getTitle(){
        return title;
    }
    public String getISBN(){
        return ISBN;
    }
    public int getPrice(){
        return price;
    }
    public int getYear(){
        return pub_yr;
    }
    public int getRating(){
        return rating;
    }
}
