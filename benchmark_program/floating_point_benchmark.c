#include <stdio.h>

#define SIZE 100000000  // Large number of iterations for a floating-point task

int main() {
    double result = 0.0;

    // Perform many floating-point operations
    for (int i = 0; i < SIZE; i++) {
        result += 1.0 / (i + 1.0);
        result *= 1.001;
        result /= 1.0001;
    }

    printf("Floating-point benchmark completed. Result: %f\n", result);
    return 0;
}
