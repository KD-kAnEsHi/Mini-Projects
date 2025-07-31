
public class LazyBinarySearchTree
{
    /**
    * Inner Class TreeNode represents a node in the Lazy Binary Search Tree.
    */    
    private class TreeNode// implements Comparable<TreeNode>
    {
        private int value;
        private TreeNode left;
        private TreeNode right;
        private boolean isDeleted;
        
        TreeNode(int value) // This is the Tree's Node Constructor, it is responsible for creating a new Node
        {
            this.value = value; // This is get the Node's Value
            this.left = null; // This is sed to move to the Node's Left Child
            this.right = null; // This is used to move to the Node's Right Child
            this.isDeleted = false; // This is the Node's Deleted Status
        }
    }

    private TreeNode root; 

    /**
     * Constructs an empty LazyBinarySearchTree.
     */
    public LazyBinarySearchTree() 
    {
        root = null;// Tree's Root Node, used to get the root from anyhere in the program
    }






//------------------------ Delete Function:
    /**
     *Delete should not physically remove an element from the tree.  Rather, it should mark the specified element as logically deleted.  
     *If the specified element is not in the tree or is already marked as deleted, then delete should do nothing.  The return value of 
     *delete should indicate whether delete logically deleted an element.

     * Marks the specified element as logically deleted without physically removing it from the tree.
     * If the element is not in the tree or is already marked as deleted, does nothing.
     * @param deletedValue The value to be marked as deleted.
     * @return true if an element was logically deleted, false otherwise.
     * @throws IllegalArgumentException if deletedValue is not in the range [1,99].
     */
    public boolean delete (int deletedValue ) throws IllegalArgumentException // This is the Tree's Delete Function
    {
        if (deletedValue < 1 || deletedValue > 99) // This is to check if the input value is within the range of 1 to 99
        {
            throw new IllegalArgumentException("Error Deletion: Please Input a Valid Integer in the Range [1,99]\n"); // This is to throw an exception if the input value is not within the range of 1 to 99
        }

        if(root == null) // This is to check if the tree is empty
        {
            System.out.println("Error Tree is Empty, There is Nothing to Delete\n");
            return false;
        }
        return deleteHelperFunction(deletedValue, this.root); // Call's the helper function to delete the value
    }

    
    private boolean deleteHelperFunction(int deletedValue, TreeNode node) // This is the Tree's Delete Helper Function
    {
        if (deletedValue == node.value) // Checks if the value to be deleted is the same as the current node's value
        {
            if (node.isDeleted) // This loop checks if the node is already deleted
            {
                return false;
            } 
            else
            {
                node.isDeleted = true;
                return true;
            }
        }
        else if (deletedValue < node.value) // This is to check if the value to be deleted is less than the current node's value
        {
            return deleteHelperFunction(deletedValue, node.left); // This is to recursively call the helper function to delete the value
        } 
        else if (deletedValue > node.value) // Checks if the value to be deleted is greater than the current node's value
        {
            return deleteHelperFunction(deletedValue, node.right); // This is to recursively call the helper function to delete the value
        } 
        else
        {
            System.out.println("Error: Deleted Value Not Found in Tree\n"); // This is to print an error message if the value to be deleted is not found in the tree
            return false;  // This is to return false if the value to be deleted is not found in the tree
        }
    }
    






    //------------------------ Insert Functions:
    /**
     * Insert should insert a new element to a leaf node.  The valid set of keys is all integers in the range [1,99]. If the new element 
     * would be a duplicate of a non-deleted element already in the tree, then insert should do nothing.  However, if the new element is 
     * not a duplicate of a non-deleted element, but is a duplicate of a deleted element, then insert should “undelete” the deleted element 
     * in-place rather than physically inserting a new copy of the element.  The return value of insert should indicate whether insert 
     * logically (as opposed to physically) inserted a new element.
     * 
     * Inserts a new element into the tree or undeletes a deleted element if it is a duplicate.
     * @param insertedValue The value to be inserted.
     * @return true if a new element was logically inserted, false otherwise.
     * @throws IllegalArgumentException if insertedValue is not in the range [1,99].
     */
    public boolean Insert(int insertedValue) throws IllegalArgumentException
    {
        if (insertedValue < 1 || insertedValue > 99)
        {
            throw new IllegalArgumentException("Error Insertion: Please Input a Valid Integer in the Range [1,99]\n"); // Throws an exception if the input value is not within the range of 1 to 99
        }

        if(contains(insertedValue) == true) // check if the tree has duplicate values
        {
            return false;
        }

        if(root == null) // check if the tree is empty
        {
            root = new TreeNode(insertedValue); // insert the value into the tree
            return true;
        }
        return insertHelperFunction(insertedValue, this.root); // Call's the helper function to insert the value
    }

    private boolean insertHelperFunction(int insertedValue, TreeNode node) // Insert Helper Function
    {
        // check if the tree has duplicate values
        if(insertedValue == node.value) // Check if the value to be inserted is the same as the current node's value
        {
            if (node.isDeleted) // Check if the node is already deleted
            {
                node.isDeleted = false; // Set the node's deleted status to false
                return true;
            } 
            else // Check if the node is not deleted
            {
                return false;
            }
        }
        else if (insertedValue < node.value) // Check if the value to be inserted is less than the current node's value
        {
            if (node.left == null) 
            {
                node.left = new TreeNode(insertedValue); // Insert the value into the left child of the current node and return true if tha value is inserted
                return true; //
            } 
            else 
            {
                return insertHelperFunction(insertedValue, node.left); // Recursively call the helper function to insert the value
            }
        } 
        else // Check if the value to be inserted is greater than the current node's value
        {
            if (node.right == null) // Check if the value to be inserted is greater than the current node's value
            {
                node.right = new TreeNode(insertedValue); // Insert the value into the right child of the current node and return true if tha value is inserted
                return true; 
            } 
            else // Check if the value to be inserted is greater than the current node's value
            {
                return insertHelperFunction(insertedValue, node.right); // Recursively call the helper function to insert the value
            }
        }
    }




    //------------------------ findMin Functions: NOT FINISHED
    /**
     * FindMin should return the value of the minimum non-deleted element, or -1 if none exists.
     * Inserts a new element into the tree or undeletes a deleted element if it is a duplicate.
     * Finds the minimum non-deleted element in the tree.
     * @return The value of the minimum non-deleted element, or -1 if none exists.
     */
    public int findMin() // This is the Tree's FindMin Function
    {
        if (root == null) // Checks if the tree is empty
        {
            System.err.println("Tree is Empty, There is No Minimum Value to Find\n"); // Prints an error message if the tree is empty and returns -1 if the tree is empty
            return -1; 
        }
        return findMinNode(root).value; // Calls the helper function to find the minimum value in the tree
    }
    
    private TreeNode findMinNode(TreeNode node) // This is the Tree's FindMin Helper Function
    {
        if (node.left == null) // Checks if the left child of the current node is null
        {
            if (node.isDeleted) // Checks if the current node is deleted
            {
                return findMinNode(node.right); // Recursively call the helper function to find the minimum value in the right child of the current node
            } 
            else // Checks if the current node is not deleted
            {
                return node; // Returns the current node
            }
        } 
        else // Checks if the left child of the current node is not null
         {
            TreeNode leftMin = findMinNode(node.left); // Recursively call the helper function to find the minimum value in the left child of the current node
            if (leftMin != null && !leftMin.isDeleted) // Checks if the minimum value in the left child of the current node is not deleted
            {
                return leftMin; // Returns the minimum value in the left child of the current node
            } 
            else 
            {
                return findMinNode(node.right); // Recursively call the helper function to find the minimum value in the right child of the current node
            }
        }
    }
    






    //------------------------ findMax Functions: NOT FINISHED
    /**
    * FindMax should return the value of the maximum non-deleted element, or -1 if none exists.
    * Finds the maximum non-deleted element in the tree.
    * @return The value of the maximum non-deleted element, or -1 if none exists.
    */
    public int findMax() // This is the Tree's FindMax Function
    {
        if (root == null) // Checks if the tree is empty
        {
            System.err.println("Tree is Empty, There is No Maximum Value to Find\n"); // Prints an error message if the tree is empty and returns -1 if the tree is empty returns -1 if the tree is empty
            return -1; 
        }
        return findMaxNode(root).value; // Calls the helper function to find the maximum value in the tree
    }
    
    private TreeNode findMaxNode(TreeNode node) // This is the Tree's FindMax Helper Function
    {
        if (node.right == null) // Checks if the right child of the current node is null
        {
            if (node.isDeleted) // Checks if the current node is deleted
            {
                return findMaxNode(node.left); // Recursively call the helper function to find the maximum value in the left child of the current node
            } 
            else // Checks if the current node is not deleted
            {
                return node; // Returns the current node
            }
        } 
        else // Checks if the right child of the current node is not null
        {
            TreeNode rightMax = findMaxNode(node.right); // Recursively call the helper function to find the maximum value in the right child of the current node
            if (rightMax != null && !rightMax.isDeleted) // Checks if the maximum value in the right child of the current node is not deleted
            {
                return rightMax; // Returns the maximum value in the right child of the current node
            } 
            else 
            {
                return findMaxNode(node.left); // Recursively call the helper function to find the maximum value in the left child of the current node
            }
        }
    }





    //------------------------ Contains Functions:
    /**
     * Contains should return whether the given element both exists in the tree and is non-deleted.
     * Checks if the given element exists in the tree and is non-deleted.
     * @param value The value to check.
     * @return true if the value exists and is non-deleted, false otherwise.
     * @throws IllegalArgumentException if value is not in the range [1,99].
     */
    public boolean contains(int value) throws IllegalArgumentException // This is the Tree's Contains Function
    {
        if (value < 1 || value > 99) // Checks if the input value is within the range of 1 to 99
        {
            throw new IllegalArgumentException("Error Contains: Please Input a Valid Integer in the Range [1,99]\n"); // Throws an exception if the input value is not within the range of 1 to 99
        }

        if (root == null) // Checks if the tree is empty
        {
            System.out.println("Error Tree is Empty and does not contain any values\n"); // Prints an error message if the tree is empty and returns false if the tree is empty returns false if the tree is empty
            return false; 
        }

        TreeNode node = root; // Sets the current node to the root of the tree
        while( node !=  null) // Loops through the tree to find the value
        {
            if(value == node.value) // Checks if the value is the same as the current node's value
            {
                if(node.isDeleted == false) // Checks if the current node is not deleted
                { 
                    return true; // Returns true if the value is found in the tree and is not deleted
                }
                else // Checks if the current node is deleted
                {
                    return false; // Returns false if the value is found in the tree and is deleted
                }
            }
            if(value > node.value) // Checks if the value is greater than the current node's value
            {
                node = node.right; // Moves to the right child of the current node
            }
            else if(value < node.value) // Checks if the value is less than the current node's value
            {
                node = node.left; // Moves to the left child of the current node
            }
        }
        return false; // Returns false if the value is not found in the tree
    }









    //------------------------ Contains Functions:
    /**
    * ToString should perform an pre-order traversal of the tree and print the value of each element, including elements marked as deleted.  
    * However, elements that are marked as deleted should be preceded by a single asterisk.  Every pair of adjacent elements should be 
    * separated by whitespace in the printing, but no whitespace should occur between an asterisk and the element with which it is associated.
    * Leading and trailing whitespace is tolerable, but it will be ignored.  (no additional messages should be printed, either)  An example 
    * of the output is as follows:
    
    * Performs a pre-order traversal of the tree and constructs a string representation.
    * Deleted elements are preceded by an asterisk '*' in the string.
    * @return A string representation of the tree's elements.
    */
    public String toString() { // This is the Tree's ToString Function
        if(root == null) // Checks if the tree is empty
        {
            System.out.println("Error Tree is Empty, There is Nothing to Print\n"); // Prints an error message if the tree is empty and returns an empty string if the tree is empty
            return ""; // Returns an empty string if the tree is empty
        }

        StringBuilder sb = new StringBuilder(); // Creates a new StringBuilder object
        toStringConcatenation(root, sb); // Calls the helper function to concatenate the values in the tree
        return sb.toString(); // Returns the concatenated values in the tree
    }

    private void toStringConcatenation(TreeNode node, StringBuilder sb) 
    {
        if (node == null) // Checks if the current node is null
        { 
            return;
        }

        if (node.isDeleted) // Checks if the current node is deleted
        {
            sb.append("*").append(node.value).append(" "); // Appends an asterisk to the current node's value
        } 
        else // Checks if the current node is not deleted
        {
            sb.append(node.value).append(" "); // Appends the current node's value
        }
        toStringConcatenation(node.left, sb); // Recursively calls the helper function to concatenate the values in the left child of the current node
        toStringConcatenation(node.right, sb); // Recursively calls the helper function to concatenate the values in the right child of the current node
    }








    //------------------------ Height Functions:
    /**
    * Height should return the height of the tree, including “deleted” elements
    * Calculates the height of the tree, including "deleted" elements.
    * @return The height of the tree.
    */
    public int height() 
    {
        if(root == null) // Checks if the tree is empty
        {
            System.out.println("Error Tree is Empty, Program Cannot Count Height\n"); // Prints an error message if the tree is empty and returns -1 if the tree is empty
            return -1;
        }
        return heightCounter(root); // Calls the helper function to count the height of the tree
    }

    private int heightCounter(TreeNode node)  // This is the Tree's Height Helper Function
    {
        if (node == null) // Checks if the current node is null returns -1 if the current node is null
        {
            return -1; 
        }

        int leftHeight = heightCounter(node.left); // Recursively calls the helper function to count the height of the left child of the current node
        int rightHeight = heightCounter(node.right); // Recursively calls the helper function to count the height of the right child of the current node
        return 1 + Math.max(leftHeight, rightHeight); // Returns the maximum height of the left and right children of the current node
    }






    //------------------------ Size Function:
    /**
     * size should return the count of elements in the tree, including “deleted” ones.
     * Counts the number of elements in the tree, including "deleted" ones.
     * @return The count of elements in the tree.
     */
    public int size() // This is the Tree's Size Function
    {
        if(root == null) // Checks if the tree is empty
        {
            System.out.println("Error Tree is Empty, Program Cannot Count Size\n"); // Prints an error message if the tree is empty and returns -1 if the tree is empty
            return -1;
        }
        return sizeCounter(root); // Calls the helper function to count the size of the tree
    }

    private int sizeCounter(TreeNode node) // This is the Tree's Size Helper Function
    {
        if (node == null) // Checks if the current node is null
        {
            return 0;
        }
        return 1 + sizeCounter(node.right) + sizeCounter(node.left); // Recursively calls the helper function to count the size of the right and left children of the current node
    }

}





