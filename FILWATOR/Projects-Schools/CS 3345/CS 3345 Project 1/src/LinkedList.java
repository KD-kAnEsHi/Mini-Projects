/**
 * LinkedList class represents a linked list structure for storing objects of generic type AnyType,
 * where AnyType extends the IDedObject interface. This class provides various methods for manipulating
 * and managing the linked list, such as inserting, deleting, and searching for objects based on their ID.
 */

public class LinkedList<AnyType extends IDedObject> {
    private Node<AnyType> head; // Head of the linked list

    // Getter method to retrieve the head of the linked list
    public Node<AnyType> getHead() {
        return head;
    }

    // Setter method to set the head of the linked list
    public void setHead(Node<AnyType> head) {
        this.head = head;
    }

    // Constructor to initialize an empty linked list
    public LinkedList() {
        this.head = null;
    }

    /**
     * makeEmpty method sets the head of the linked list to null,
     * effectively making the list empty.
     */
    public void makeEmpty() {
        setHead(null);
    }

    /**
     * findID method searches for an object with the given ID in the linked list.
     * If found, it returns the object; otherwise, it returns null.
     */
    public AnyType findID(int ID) {
        if (getHead() == null) {
            return null;
        } else {
            Node<AnyType> listPasser = getHead();
            while (listPasser != null) {
                if (listPasser.getData().getID() == ID) {
                    return listPasser.getData();
                }
                listPasser = listPasser.getNext();
            }
        }
        return null;
    }

    /**
     * insertAtFront method inserts a new object at the front of the linked list.
     * It returns true if the insertion is successful, and false if an object with the same ID already exists.
     */
    public boolean insertAtFront(AnyType x) {
        if (findID(x.getID()) == null) {
            Node<AnyType> newNode = new Node<>(x);
            newNode.setNext(getHead());
            setHead(newNode);
            return true;
        }
        return false;
    }

    /**
     * deleteFromFront method removes and returns the object at the front of the linked list.
     * If the list is empty, it returns null.
     */
    public AnyType deleteFromFront() {
        if (getHead() != null) {
            Node<AnyType> tempFrontNode = getHead();
            setHead(getHead().getNext());
            tempFrontNode.setNext(null);
            return tempFrontNode.getData();
        }
        return null;
    }

    /**
     * deleteIDNode method removes and returns the object with the specified ID from the linked list.
     * If the list is empty or the ID is not found, it returns null.
     */
    public AnyType deleteIDNode(int ID) {
        if (getHead() == null) //If the LinkedList is empty the program is going to return the NULL
        {
            return null;
        }

        if (getHead().getData().getID() == ID) //If the ID at the LinkedList Head is equal to the ID inputted by the user the Program is going to call the function deleteFront
        {
            return deleteFromFront();
        }
        else
        {
            //If the ID entered by the user is not equal to the ID in head, the program is going to loop through every LinkedList until it find the first Node that had that ID
            //and returns it, if there is no such ID, the program will return false.
            Node<AnyType> frontNode = getHead().getNext();
            Node<AnyType> backNode = getHead();

            while (frontNode != null) {
                if (frontNode.getData().getID() == ID)
                {
                    backNode.setNext(frontNode.getNext());
                    frontNode.setNext(null);
                    return frontNode.getData();
                }
                backNode = frontNode;
                frontNode = frontNode.getNext();
            }
        }
        return null;
    }

    /**
     * printAllRecords method prints the details of all objects in the linked list.
     * If the list is empty, it prints a corresponding message.
     */
    void printAllRecords() {
        if (getHead() == null)// If the list is empty, the program will display a message on the screen letting the user know
        {
            System.out.println("Linked List is empty!");
        }
        else
        {
            // Else if the LinkedList is not empty, the program is going to parse through the LinkedList until it reaches NULL, and outputs every data stored in each Node
            Node<AnyType> parsingNode = getHead();
            while (parsingNode != null) {
                parsingNode.getData().printID();
                System.out.println();
                parsingNode = parsingNode.getNext();
            }
        }
    }
}
