#include <stdio.h>
#include <stdlib.h>

#define SIZE 100000000  // Large array size

int main() {
    int *array = (int*)malloc(SIZE * sizeof(int));
    
    // Sequential memory access
    for (int i = 0; i < SIZE; i++) {
        array[i] = i;
    }

    // Random memory access (reverse order)
    for (int i = SIZE - 1; i >= 0; i--) {
        array[i] += i;
    }

    printf("Memory-bound benchmark completed.\n");
    free(array);
    return 0;
}