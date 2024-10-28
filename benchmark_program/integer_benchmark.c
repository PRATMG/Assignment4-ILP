#include <stdio.h>

#define SIZE 100000000  // Large number of iterations for a CPU-intensive task

int main() {
    int result = 0;
    
    // Perform many integer operations
    for (int i = 0; i < SIZE; i++) {
        result += i;
        result *= 2;
        result /= 2;
    }

    printf("Integer-bound benchmark completed. Result: %d\n", result);
    return 0;
}
