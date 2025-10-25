import java.util.Scanner;
public class calcu {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("=== CALCULATOR ===");
            int UserInput = - 1;
            try {
                System.out.println("Enter a chocies: ");
                UserInput = scanner.nextInt();
            }
            catch (Exception e) {
                System.out.println("System: Invalid input. Please enter a number.");
                scanner.next(); // Clear the invalid input
                continue;
            }
            if (UserInput == 1) {
                System.out.println("Enter first number: ");
                int number_1 = scanner.nextInt();
                System.out.println("Enter second number: ");
                int number_2 = scanner.nextInt();
                System.out.println("Answer: " + (number_1 + number_2));
            }
            else if (UserInput == 2) {
                System.out.println("Enter first number: ");
                int number_1 = scanner.nextInt();
                System.out.println("Enter second number: ");
                int number_2 = scanner.nextInt();
                System.out.println("Answer: " + (number_1 - number_2));
            }
            else if (UserInput == 3) {
                System.out.println("Enter first number: ");
                int number_1 = scanner.nextInt();
                System.out.println("Enter second number: ");
                int number_2 = scanner.nextInt();
                System.out.println("Answer: " + (number_1 * number_2));
            }
            else if (UserInput == 4) {
                System.out.println("Enter first number: ");
                int number_1 = scanner.nextInt();
                System.out.println("Enter second number: ");
                int number_2 = scanner.nextInt();
                if (number_2 == 0) {
                    System.out.println("Error: Division by zero is not allowed.");
                } else {
                    System.out.println("Answer: " + (number_1 / number_2));
                }
            }
            else if (UserInput == 5) {
                System.out.println("Exiting the calculator. Goodbye!");
                break;
            }
            else {
                System.out.println("Invalid input. Please try again.");
            }
        }
        scanner.close();
    }
}