#include <stdio.h>
#include "complex.h"
#include "quaternion.h"
#include "vector.h"

int main() {
    Complex c1 = { 1, 2 };
    Complex c2 = { 3, 4 };
    Complex result = exp_complex(&c1);

    printf("%.15lf + %.15lfi", result.real, result.imag);

    return 0;
}
