/**
 * The Node class represents a node in a linked list and is parameterized with AnyType, which must extend IDedObject.
 * This is essentially were the getter and setters utilized when moving and adding Nodes to the LinedList will be stored.
 */
public class Node<AnyType extends IDedObject> {

        private Node<AnyType> next;// Reference to the next node in the linked list
        private AnyType data;// Data stored in the current node

        /**
         * Constructor for the Node class, initializing the node with the provided data.
         * @param data The data to be stored in the node.
         */
        public Node(AnyType data) {
                this.data = data;
                this.next = null;
        }

        /**
         * Setter method to set the reference to the next node in the linked list.
         * @param next The next node in the linked list.
         */
        public void setNext(Node<AnyType> next) {
                this.next = next;
        }

        /**
         * Getter method to retrieve the reference to the next node in the linked list.
         * @return The next node in the linked list.
         */
        public Node<AnyType> getNext() {
                return next;
        }

        /**
         * Getter method to retrieve the data stored in the current node.
         * @return The data stored in the current node.
         */
        public AnyType getData() {
                return data;
        }
}
