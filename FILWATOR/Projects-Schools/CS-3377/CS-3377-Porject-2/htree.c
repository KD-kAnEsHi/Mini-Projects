/*
 * Pratyush Niraula, pxn210033
 * Karl Azangue,  kka210001
*/

/*
 * Pratyush Niraula,  pxn210033
 * Karl Azangue,  kka210001
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <errno.h>     // for EINTR
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>

// Print out the usage of the program and exit.
void Usage(char*);
uint32_t jenkins_one_at_a_time_hash(const uint8_t* , uint64_t );


typedef struct threader{
  uint32_t threadNumber;
  uint8_t *arr;
  uint32_t start;
  uint32_t end;
  uint32_t hash;
};



// block size
#define BSIZE 4096

int main(int argc, char** argv)
{
  int32_t fd;
  uint32_t nblocks;

  // input checking 
  if (argc != 3)
    Usage(argv[0]);

  // open input file
  fd = open(argv[1], O_RDWR);
  if (fd == -1) {
    perror("open failed");
    exit(EXIT_FAILURE);
  }

  struct stat statStruct;
  if(fstat(fd, &statStruct) == -1)
  {
    perror("fstat failed");
    exit(EXIT_FAILURE);
  }    

  // use fstat to get file size
  // calculate nblocks 
  uint8_t *mapper = mmap(NULL, statStruct.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
  if(mapper == MAP_FAILED){
    perror("mmap failure");
    exit(EXIT_FAILURE);
  }




  printf(" no. of blocks = %u \n", nblocks);
  double start = GetTime();

  // calculate hash value of the input file
  double end = GetTime();
  printf("hash value = %u \n", hash);
  printf("time taken = %f \n", (end - start));
  close(fd);
  return EXIT_SUCCESS;
}



uint32_t jenkins_one_at_a_time_hash(const uint8_t* key, uint64_t length)
{
  unint64_t i = 0;
  uint32_t hash = 0;

  while (i != length) {
    hash += key[i++];
    hash += hash << 10;
    hash ^= hash >> 6;
  }
  hash += hash << 3;
  hash ^= hash >> 11;
  hash += hash << 15;
  return hash;
}


void Usage(char* s)
{
  fprintf(stderr, "Usage: %s filename num_threads \n", s);
  exit(EXIT_FAILURE);
}




















/*
#include <stdio.h>     
#include <stdlib.h>   
#include <stdint.h>  
#include <inttypes.h>  
#include <errno.h>     // for EINTR
#include <fcntl.h>     
#include <unistd.h>    
#include <sys/types.h>
#include <sys/stat.h>

#include <pthread.h>
#include <sys/mman.h>
#include <assert.h>


// Print out the usage of the program and exit.
void Usage(char*);
uint32_t jenkins_one_at_a_time_hash(const uint8_t* , uint64_t );

// function to calculate time
typedef struct threader{
  uint32_t threadNumber;
  uint8_t *arr;
  uint32_t start;
  uint32_t end;
  uint32_t hash;
  };


// block size
#define BSIZE 4096

int main(int argc, char** argv) 
{
  int32_t fd;
  uint32_t nblocks;

  // input checking 
  if (argc != 3)
    Usage(argv[0]);



  // open input file
  fd = open(argv[1], O_RDWR);
  if (fd == -1) {
    perror("open failed");
    exit(EXIT_FAILURE);
  }



  // use fstat to get file size
  struct stat statStruct;
  if(fstat(fd, &statStruct) == -1){
    perror("fstat failure");
    exit(EXIT_FAILURE);
  }



  uint8_t *mapper = mmap(NULL, statStruct.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
  if(mapper == MAP_FAILED){
    perror("mmap failure");
    exit(EXIT_FAILURE);
  }



  int32_t numThreads = atoi(argv[2]);
  if(numThreads < 1){
    perror("Invalid number of threads");
    exit(EXIT_FAILURE);
  }



  // calculate nblocks 
  nblocks = statStruct.st_size / BSIZE;
  printf(" no. of blocks = %u \n", nblocks);












  double start = GetTime();
  
  threadData *data[numThreads];

  for(int i = 0l i < numThreads; i++){
    data[i] = (threadData *)malloc(sizeof(threadData));
    data[i]->mapper = mapper;
    data[i]->threadID = i;
    data[i]->start = i * blockperThread;
    data[i]->end = hashValue = 0;
    pthread_create(&threads[i], NULL, threadFunction, (void *)data);  
  }
  

  double end = GetTime();
  //printf("hash value = %u \n", hash);
  printf("time taken = %f \n", (end - start));
  close(fd);
  return EXIT_SUCCESS;
}



// function to calculate hash value of the input file
uint32_t jenkins_one_at_a_time_hash(const uint8_t* key, uint64_t length) 
{
  uint64_t i = 0;
  uint32_t hash = 0;
  
  while (i != length) {
    hash += key[i++];
    hash += hash << 10;
    hash ^= hash >> 6;
  }
  hash += hash << 3;
  hash ^= hash >> 11;
  hash += hash << 15;
  return hash;
}


void Usage(char* s) 
{
  fprintf(stderr, "Usage: %s filename num_threads \n", s);
  exit(EXIT_FAILURE);
}



*/