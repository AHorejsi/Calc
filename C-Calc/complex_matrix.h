#ifndef COMPLEX_MATRIX_H
#define COMPLEX_MATRIX_H


#include "complex.h"

typedef struct complex_matrix_t {
    Complex** values;
    int rows;
    int cols;
} ComplexMatrix;


#endif
