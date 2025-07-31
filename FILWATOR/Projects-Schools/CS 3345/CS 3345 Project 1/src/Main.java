import java.util.Scanner;

// The main class that contains the program's entry point
public class Main {
    public static void main(String[] args) {

        // Create a Scanner object to take user input
        Scanner scanner = new Scanner(System.in);

        // Create a LinkedList to store Product objects
        LinkedList<Product> productInfo = new LinkedList<>();
        int enteredChoice;

        // Display the main menu for the program
        System.out.println("*********************** Program Menu ***********************");
        System.out.println("Enter a value between a number (1 - 7) for each of the following.");
        System.out.println("1 - Make Empty: Clears the list of every product info on file");
        System.out.println("2 - Find ID: Outputs the details/info of the searched ID. If not found you will receive an error message");
        System.out.println("3 - Insert At Front: Get the product magazine details from the user and add it to the front of the list");
        System.out.println("4 - Delete From Front: Print the first item on the list and deletes it");
        System.out.println("5 - Delete ID: Print particular IDed item in the list and then delete it.");
        System.out.println("6 - Print All Records:  Print all the records in the list");
        System.out.println("7 - Quit: Quit the program.");
        System.out.println();
        System.out.print("Please Enter your choice: ");
        enteredChoice = scanner.nextInt();

        // Main loop to process user choices until they choose to quit (option 7)
        while(enteredChoice != 7)
        {
            // Validate user input to ensure it is within the valid range (1 - 7), if is not withing this range the user will be prompted to enter another value
            if(enteredChoice > 7 || enteredChoice <= 0)
            {
                System.out.print("Invalid Choice, Enter a number between 1 - 7: ");
                enteredChoice = scanner.nextInt();
            }

            // Process user choice based on the entered number:

            /**
             * If the user ENTERS 1, the LinkedList will be cleared, and message will be displayed on the screen letting
             * the user know that they List is now empty.
             */
            if(enteredChoice == 1)
            {
                // Clear the list of product information
                System.out.println("Your Choice: 1");// Tells user which choice the choosed
                productInfo.makeEmpty();
                System.out.println("The list is now empty.");//Lets the user know that the list is now empty
            }
            /**
             * If the user ENTERS 2, the user will then be prompted to enter the ID of the value they are search for once they user enters a value, if the ID is not in
            * they list a message will be displayed on the screen stating that they ID could not be found, else they ID and every detials (productName, supplierName, and
            * productID) will be displayed on the screen
             */
            else if(enteredChoice == 2)
            {
                System.out.println("Your Choice: 2");// Tells user which choice the choosed
                // Search for a product by ID and display its details
                int iD;
                System.out.print("Enter ID that is to be found: "); //Prompts the user to enter the ID they are searching for
                iD = scanner.nextInt();
                Product foundID = productInfo.findID(iD);//Searches the ID in the LinkedList and stores the returned generic values in 'foundID'
                if(foundID != null)//If the ID was found in the LinedList the program is going to output the ID, and its details (productName, supplierName, and productID)
                {                  //if not found the program will output a message stating that the ID could not be found
                    System.out.println("ID Found, here are the ID details:");
                    foundID.printID();
                }
                else
                {
                    System.out.println("ID not found in the list");
                }
            }
            /** If they user ENTERS 3, the user will be prompted to enter the details for the new product the would like to add to the LinkedList, in this order ProductID,
            ProductName, and SupplierName, once that is done the program will output a message confirming that a new product was added.
             */
            else if(enteredChoice == 3)
            {
                System.out.println("Your Choice: 3");// Tells user which choice the choosed
                // Get details for a new product from the user and insert it at the front of the list
                System.out.println("Enter details for the new Product");
                System.out.print("Enter Product ID: ");//Prompts the user to enter the details regarding the newProduct
                int productID = scanner.nextInt();
                scanner.nextLine(); // Consume the newline character left in the buffer

                System.out.print("Enter Product Name: ");
                String productName = scanner.nextLine();

                System.out.print("Enter Supplier Name: ");
                String supplierName = scanner.nextLine();

                Product newProduct = new Product(productID, productName, supplierName);//Creates a node using all the details (productName, supplierName, and productID) inputed by the user
                productInfo.insertAtFront(newProduct);//Adds the created Node/new product to the front of the list
                System.out.println("Product inserted at the front of the list.");//lets the user know that a new the prodyct was succefully added to the front
            }
            /**If the user ENTERS 4, the program is going to delete the firs NODE in the program, and output a confirmation message stating that the first not was deleted and
            *and the details (productName, supplierName, and productID) associated with the deleted product.
             */
            else if(enteredChoice == 4)
            {
                System.out.println("Your Choice: 4");// Tells user which choice the choosed
                Product deletedFront = productInfo.deleteFromFront();// Delete the first item from the list and display its details

                if(deletedFront != null)//If the list is not empty the program, delete first node, and outputs its details
                {
                    System.out.println("Deleted from the front of the list:");
                    deletedFront.printID();
                }
                else
                {
                    System.out.println("List is empty, there is nothing to delete."); //If the list is empty the program tells the user that the list was empty
                }
            }
            /**If the user ENTERS 5, then they will be prompted to enter the value the would like to delete, once that is the program will check if the ID exist, if it does
            the program will delete Node, else it will output a message letting the user know that the ID couldn't be found
             */
            else if(enteredChoice == 5)
            {
                System.out.println("Your Choice: 5");// Tells user which choice the choosed
                // Delete a product by ID and display its details
                System.out.print("Enter ID to be deleted: ");
                int deleteID = scanner.nextInt();
                System.out.println();

                Product deletedProductID = productInfo.deleteIDNode(deleteID);//Removed the generic Node associeted with the ID entered by the user and returns it
                if (deletedProductID != null) //If they ID was found in the LinkedList the program is going to output all of its details, before deleting
                {
                    System.out.print("Deleted product with ID " + deleteID + ": ");
                    System.out.println();
                    deletedProductID.printID();
                }
                else
                {
                    System.out.println("Product with ID " + deleteID + " not found.");//If the ID was not found in the list, the program is going state so on the screen
                    System.out.println();
                }
            }
            //If the user ENTERS 6, the program is going to go through every Node/Product in the LinkedList and output their details (productName, supplierName, and productID)
            else if(enteredChoice == 6)
            {
                System.out.println("Your Choice: 6");// Tells user which choice the choosed
                // Display details of all products in the list
                System.out.println("Here is the output of every product in the list.");
                productInfo.printAllRecords();//Goes through every Node in the LinkedList and outputs what is inside
            }

            System.out.println();
            System.out.print("Please Enter new MENU choice: "); //This prompts the user to choose another value from the MENU, this will keep going unless the user enters 7
            enteredChoice = scanner.nextInt();
        }
        // Display a goodbye message when the program exits
        System.out.println("Your Choice: 7");
        System.out.println("Program is done running, Goodbye");
        System.exit(0);
    }
}
