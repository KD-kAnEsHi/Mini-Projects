import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;
import java.io.*;


public class Main
{
    public static void main(String[] args) {
        if (args.length != 2) // Check if the number of arguments is correct, if not print error message
        {
            System.out.println("Error, Please Input Valid Arguments in Command Line\n"); 
            return; 
        }

        String inputFile = args[0]; // Get the input file name from the command line
        String outputFile = args[1]; // Get the output file name from the command line

        LazyBinarySearchTree tree = new LazyBinarySearchTree(); // Create a new LazyBinarySearchTree object, tree used to store the values

        try (BufferedReader fileReader = new BufferedReader(new FileReader(inputFile)); 
             BufferedWriter fileWriter = new BufferedWriter(new FileWriter(outputFile))) // Try to open the input and output files
        {
            
            String line; // Create a string to store the current line
            while ((line = fileReader.readLine()) != null) // Read the input file line by line
            {
                String[] command = new String[line.length()];

                if(line.contains(":")) // Check if the line contains a colon if it does split the line into the command and the argument
                {
                    command = line.split(":");
                }
                else // If the line does not contain a colon Split the line into the command and the argument
                {
                    command[0] = line; 
                }
                String commandName = command[0]; // Get the command name
                String commandArgs = (command.length > 1) ? command[1].trim() : null; // Get the command argument

                switch (commandName) // Check the command name
                {
                    case "Insert":  // If the command is insert
                        if (commandArgs == null) // Check if the input is valid
                        {
                            fileWriter.write("Error in insert: Invalid input\n"); // If the input is invalid, print an error message
                        }
                        else 
                        {
                            try 
                            {
                                boolean inserted = tree.Insert(Integer.parseInt(commandArgs)); // Insert the value into the tree
                                fileWriter.write(Boolean.toString(inserted) + "\n"); // Print whether the value was inserted
                            } 
                            catch (IllegalArgumentException ex) // Catch any exceptions that occur when parsing the input
                            {
                                fileWriter.write("Error in insert: IllegalArgumentException raised\n"); // If the input is invalid, print an error message
                            }
                        }
                        break;

                    case "Delete":
                        try 
                        {
                            boolean deleted = tree.delete(Integer.parseInt(commandArgs)); // Delete the value from the tree
                            fileWriter.write(Boolean.toString(deleted) + "\n"); // Print whether the value was deleted
                        } 
                        catch (IllegalArgumentException ex) // Catch any exceptions that occur when parsing the input
                        {
                            fileWriter.write("Error in delete: IllegalArgumentException raised\n"); // If the input is invalid, print an error message
                        }
                        break;

                    
                    case "Contains": // If the command is contains
                        try 
                        {
                            boolean contains = tree.contains(Integer.parseInt(commandArgs)); // Check if the value is in the tree
                            fileWriter.write(Boolean.toString(contains) + "\n"); // Print whether the value is in the tree
                        } 
                        catch (IllegalArgumentException ex) // Catch any exceptions that occur when parsing the input
                        {
                            fileWriter.write("Invalid input\n"); // If the input is invalid, print an error message
                        }
                        break;


                    case "FindMax": // If the command is find max
                        int max = tree.findMax(); // Get the maximum value in the tree
                        fileWriter.write(Integer.toString(max) + "\n"); // Print the maximum value in the tree
                        break;

                    case "FindMin": // If the command is find min
                        int min = tree.findMin(); // Get the minimum value in the tree
                        fileWriter.write(Integer.toString(min) + "\n"); // Print the minimum value in the tree
                        break;

                    case "PrintTree": // If the command is print tree
                        String str = tree.toString(); // Get the tree as a string
                        fileWriter.write(str + "\n"); // Print the tree
                        break;

                    case "Height": // If the command is height
                        int height = tree.height(); // Get the height of the tree
                        fileWriter.write(Integer.toString(height) + "\n"); // Print the height of the tree
                        break;

                    case "":
                        // Ignore empty lines
                        break;

                    default:
                        fileWriter.write("Error in Line: " + commandName + "\n"); // If the command is not recognized, print an error message
                        break;
                }
            }
        } 
        catch (IOException e) // Catch any exceptions that occur when opening the files
        {
            System.out.println("Error opening Read and Write File");
            return;
        }
    }
}

