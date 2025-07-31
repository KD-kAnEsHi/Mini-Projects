/**
 * The Product class represents an entity with product information and implements the IDedObject interface.
 * It includes variables for productID, productName, and supplierName. Additionally, it provides a constructor
 * to initialize these variables and implements the required methods from the IDedObject interface.
 */
public class Product implements IDedObject {

        private int productID;// Variable for productID
        private String productName;// Variable for productName
        private String supplierName;// Variable for supplierName

        /**
         * Constructor for the Product class, initializing productID, productName, and supplierName.
         * @param productID      The unique identifier for the product.
         * @param productName    The name of the product.
         * @param supplierName   The name of the supplier for the product.
         */
        public Product(int productID, String productName, String supplierName) {
                this.productID = productID;
                this.productName = productName;
                this.supplierName = supplierName;
        }


        /**
         * Implementation of the getID() method from the IDedObject interface.
         * Getter function that returns the productID.
         * @return The productID of the product.
         */
        @Override
        public int getID() {
                return productID;
        }

        /**
         * Implementation of the printID() method from the IDedObject interface.
         * Prints the details of the product including productID, productName, and supplierName.
         */
        @Override
        public void printID() {
                System.out.println("ProductID: " + productID);
                System.out.println("ProductName: " + productName);
                System.out.println("SupplierName: " + supplierName);
        }
}
