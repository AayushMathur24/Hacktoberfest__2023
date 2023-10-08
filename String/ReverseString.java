import java.util.*;
class ReverseString {
    public static void main(String[] args) {
        //Original String
        String a="Hacktoberfest";
        //Variable to store the Reversed String
        String res="";
        //Iterating from end of the String to starting
        for(int i=a.length()-1;i>=0;i--)
        {
            res+=a.charAt(i);
        }
        //Printing the Reversed String
        System.out.println("Reversed String= "+res);
    }
}
