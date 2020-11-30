#ifndef QUATERNION_MATRIX_H
#define QUATERNION_MATRIX_H


#include "quaternion.h"

typedef struct quaternion_matrix_t {
    Quaternion** values;
    int rows;
    int cols;
} QuaternionMatrix;


#endif
