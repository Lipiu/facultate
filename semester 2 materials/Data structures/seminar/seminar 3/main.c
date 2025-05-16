#include <stdio.h>
#include <malloc.h>

#define BYTEARRAY_SIZE 10
#define LINE_SIZE 8
#define COLUMN_SIZE 10


int main()
{
	char x = 65;
	char y = -2;

	float z = 65.64;

	char* p = NULL;
	printf("Stack memory address where p is allocated = %p\n", &p);
	printf("Content of p = %p\n", p);
	//printf("Content pointed by p = %d\n", *p);

	p = &x;
	printf("Stack memory address where p is allocated = %p\n", &p);
	printf("Content of p = %p\n", p);
	printf("Content pointed by p = %d\n", *p);

	p = (char*)malloc(1 * sizeof(char));
	printf("Stack memory address where p is allocated = %p\n", &p);
	printf("Content of p = %p\n", p);
	printf("Content pointed by p = %d\n", *p);

	*p = x;
	printf("Stack memory address where p is allocated = %p\n", &p);
	printf("Content of p = %p\n", p);
	printf("Content pointed by p = %d\n", *p);

	free(p);

    p = (char*)malloc((BYTEARRAY_SIZE + 1)* sizeof(char)); // +1 for null byte
    
    for(unsigned char i = 0; i < BYTEARRAY_SIZE; i++){
        p[i] = x + i;
    }
    p[BYTEARRAY_SIZE] = 0; //store the null terminator byte at the last allocated byte in the byte array

    for(unsigned char i = 0; i < BYTEARRAY_SIZE; i++){
        printf("%d --> %c\n", p[i], p[i]);
    }

    printf("%s", p);
    
    free(p);

    char v[BYTEARRAY_SIZE + 1]; //for null byte terminator
    for(unsigned char i = 0; i < BYTEARRAY_SIZE; i++){
        p[i] = x + i;
    }
    v[BYTEARRAY_SIZE] = 0;

    p = v;
    printf("%s\n", p);

    char M[10][9];
    char** pM = NULL;

    // step 1: allocate the intermediary array of heap addresses of the lines
    pM = (char**)malloc(LINE_SIZE * sizeof(char*));
	
    // step 2: allocate heap memory for the lines
    for(unsigned char i = 0; i < LINE_SIZE; i++){
        pM[i] = (char*)malloc(COLUMN_SIZE * sizeof(char)); // starting heap address of line i
    }

    // store actual values over the items pM[i][j]


    // deallocate the matrix in heap memory
    // step 1: deallocate the farthest heap locations (the lines with actual values)
    for(unsigned char i = 0; i < LINE_SIZE; i++){
        free(pM[i]); // deallocate the line i
    }
    // step 2: deallocate the nearest location
    free(pM); // intermediary arrays of pointers to lines is deallocated

    return 0; 
}