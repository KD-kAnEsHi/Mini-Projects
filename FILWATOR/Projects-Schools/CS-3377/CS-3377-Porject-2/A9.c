#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/syscall.h>

#include "common_threads.h"

void *tree(void *arg);
int gettid();

int main(int argc, char *argv[])
{
    int ht;
    if (argc != 2) {
        fprintf(stderr, "usage: htree height \n");
        exit(1);
    }

    ht = atoi(argv[1]);
    pthread_t p1;
    Pthread_create(&p1, NULL, tree, &ht);
    Pthread_join(p1, NULL);
    return 0;
}

// It is easier to write a recursive function than an iterative one.
// Remember arg is an address in the stack of the caller.
// I wouldnt modify the value at that location.
void* tree(void* arg)
{
    int height = *((int *) arg);                                         // Deference the passed argument and store the tree's height as an integer

    if(height > 0)                                                       // If statement, check whethe the current node is a leaf of internal node, (leaf is height is 0).
    {
        pthread_t left, right;
        int leftHeight = height - 1;                                     // Calculate the heights for left and right children
        int rightHeight = height - 1;

        printf("Int. Thread (id: %d) at height %d\n", gettid(), height); // Print information about the internal thread

        Pthread_create(&left, NULL, tree, &leftHeight);                  // Program Create threads for left and right children
        Pthread_create(&right, NULL, tree, &rightHeight);

        Pthread_join(left, NULL);                                        // Program wait for left and right children to complete
        Pthread_join(right, NULL);
    }
    else
    {
        printf("Leaf Thread (id: %d) at height %d\n", gettid(), height); // Print information about the leaf thread
    }
    return NULL;
}

int gettid()
{
    return (syscall(SYS_gettid));
}

