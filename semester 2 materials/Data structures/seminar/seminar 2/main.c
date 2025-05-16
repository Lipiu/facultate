/*
allocation to stack -> from high memory address to low memory address (right to left)
allocation: LMA:  <-  z  <-  y  <-  x   <- HMA
*/

#include <stdio.h>

int main(){
    char x = 62;
    char y = -2;
    float z = 65.64;

    char* p = &x; //allocated on stack
    printf("Stack memory address where p is allocated: %p\n", &p);
    printf("Content of p: %p\n", p);
    printf("Content pointed by p: %d", *p);

    return 0;
}