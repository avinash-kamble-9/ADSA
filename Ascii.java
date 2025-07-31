import java.util.Scanner;

public class Ascii {
    public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name:");

        String username =sc.nextLine(); 

        System.out.println("ASCII values of the username:");
        
        for (int i = 0; i < username.length(); i++) {
            char character = username.charAt(i);
            int asciiValue = (int) character; // Convert character to ASCII value
            System.out.println(character + " -> " + asciiValue);
        }
    }
}
