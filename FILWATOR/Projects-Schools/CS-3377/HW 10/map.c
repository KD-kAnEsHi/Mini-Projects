#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <errno.h>                                                    // for EINTR
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>                                                  // for mmap


// Print out the usage of the program and exit.
void Usage(char*);

// Block size in bytes
#define BSIZE 4096

int main(int argc, char** argv)
{
        int32_t fd;                                                     // Variable to store the file descriptor
        struct stat fileStat;                                           // Structure to store the file status      
        uint8_t* arr;                                                   // Pointer to store the mapped memory          
        int block_num;                                                  // Variable to store the block number           
        uint8_t min_val;                                                // Variable to store the minimum value in the block   

        // input checking 
        if (argc != 3)
                Usage(argv[0]);

        // open input file
        fd = open(argv[1], O_RDWR);
        if (fd == -1) {
                perror("open failed");
                exit(EXIT_FAILURE);
        }


        //use fstat to get file size
        if(fstat(fd, &fileStat) == -1){                                 // Get the file status and store it in 'fileStat' structure, then check if it failed      
                perror("stat failed");                                  // print an error message
                exit(EXIT_FAILURE);                                     // Exit the program with EXIT_FAILURE status
        }
        off_t file_size = fileStat.st_size;                             // Get the file sie from the fileStat structure
        //printf("File size: %jd bytes\n", (intmax_t)file_size);



        //-----------------------------------------------------------------------------------------------------------------------------------------------------------// 
        // Call mmap to map the file to memory
        // Include the sys/mman.h header file]
         arr = mmap(NULL, file_size, PROT_READ, MAP_PRIVATE, fd, 0);     // Map the file to memory and store the pointer to the mapped memory in 'arr'
         if (arr == MAP_FAILED) {                                        // Check if the mapping failed      
                perror("mmap failed");                                   // Print an error message            
                exit(EXIT_FAILURE);                                      // Exit the program with EXIT_FAILURE status         
         }


        // parse block_num
        block_num = atoi(argv[2]);                                        // Convert the block number from string to integer            
        // find the smallest element in the specified block
        off_t block_start = block_num * BSIZE;                            // Calculate the start of the block       
        off_t block_end = block_start + BSIZE;                            // Calculate the end of the block     

        if (block_end > file_size)                                         // Check if the end of the block is greater than the file size        
        {
                block_end = file_size;                                     // Set the end of the block to the file size          
        }

        min_val = UINT8_MAX;                                               // Set the minimum value to the maximum value of uint8_t            

        off_t i;
        for (i = block_start; i < block_end; i++) {                        // Loop through the block to find the minimum value
                if (arr[i] < min_val)                                      // Check if the current value is less than the minimum value
                {
                        min_val = arr[i];                                  // Set the minimum value to the current value  
                }
        }
        printf("minimum value in block %d is %d\n", block_num, min_val);    // Print the minimum value in the block

  // use fstat to get file size

  // call mmap to map the file to memory. See man page for mmap
  // suggested usage: mmap(NULL, file_size, PROT_READ, MAP_PRIVATE, fd, 0)
  // assign the return value of mmap to  pointer variable arr 
  // arr[i] is the ith byte of the file
  // Assume the file to consists of sequence of unsigned 8 bit integer (uint8_t)

  // ................ 
  // The size of each block is BSIZE (defined above)
  // find the smallest element in the block # specified by argv[2]
  // print the result

        munmap(arr, file_size);                                             // Unmap the file from memory
        close(fd);                                                          // Close the file         
        return EXIT_SUCCESS;
}


void Usage(char* s)                                                          // Function to print the usage of the program and exit
{
        fprintf(stderr, "Usage: %s filename block_num \n", s);               // Print the usage of the program//
        exit(EXIT_FAILURE);
}
             