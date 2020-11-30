#define _USE_MATH_DEFINES

#include <math.h>
#include <stdio.h>
#include "complex.h"

Complex IMAG = { 0, 1 };

Complex complex_plus_number(Complex* left, double right) {
    Complex result = { left->real + right, left->imag };
    
    return result;
}

Complex complex_plus_complex(Complex* left, Complex* right) {
    Complex result = { left->real + right->real, left->imag + right->imag };
    
    return result;
}

Complex number_minus_complex(double left, Complex* right) {
    Complex result = { left - right->real, -right->imag };

    return result;
}

Complex complex_minus_number(Complex* left, double right) {
    Complex result = { left->real - right, left->imag };

    return result;
}

Complex complex_minus_complex(Complex* left, Complex* right) {
    Complex result = { left->real - right->real, left->imag - right->imag };

    return result;
}

Complex complex_times_number(Complex* left, double right) {
    Complex result = { left->real * right, left->imag * right };

    return result;
}

Complex complex_times_complex(Complex* left, Complex* right) {
    Complex result = {
        left->real * right->real - left->imag * right->imag,
        left->real * right->imag + left->imag * right->real
    };

    return result;
}

Complex number_divided_by_complex(double left, Complex* right) {
    Complex leftAsComplex = { left, 0 };

    return complex_divided_by_complex(&leftAsComplex, right);;
}

Complex complex_divided_by_number(Complex* left, double right) {
    Complex result = { left->real / right, left->imag / right };
    
    return result;
}

Complex complex_divided_by_complex(Complex* left, Complex* right) {
    Complex conj = conjugate_complex(right);

    Complex numerator = complex_times_complex(left, &conj);
    Complex denominator = complex_times_complex(right, &conj);

    return complex_divided_by_number(&numerator, denominator.real);;
}

Complex number_to_power_of_complex(double left, Complex* right) {
    Complex leftAsComplex = { left, 0 };

    return complex_to_power_of_complex(&leftAsComplex, right);
}

Complex complex_to_power_of_number(Complex* left, double right) {
    Complex rightAsComplex = { right, 0 };

    return complex_to_power_of_complex(left, &rightAsComplex);
}

Complex complex_to_power_of_complex(Complex* left, Complex* right) {
    double a = arg_complex(left);
    double b = left->real * left->real + left->imag * left->imag;
    double c = right->real * a + 0.5 * right->imag * log(b);
    Complex d = { cos(c), sin(c) };

    return complex_times_number(&d, pow(b, right->real / 2) * pow(M_E, -right->imag * a));
}

Complex conjugate_complex(Complex* com) {
    Complex result = { com->real, -com->imag };

    return result;
}

Complex negate_complex(Complex* com) {
    Complex result = { -com->real, -com->imag };

    return result;
}

double abs_complex(Complex* com) {
    return sqrt(com->real * com->real + com->imag * com->imag);
}

Complex normalize_complex(Complex* com) {
    return complex_divided_by_number(com, abs_complex(com));
}

int complex_equals_number(Complex* left, double right) {
    return left->real == right && 0 == left->imag;
}

int complex_equals_complex(Complex* left, Complex* right) {
    return left->real == right->real && left->imag == right->imag;
}

Complex sin_complex(Complex* com) {
    Complex result = {
        sin(com->real) * cosh(com->imag),
        cos(com->real) * sinh(com->imag)
    };

    return result;
}

Complex cos_complex(Complex* com) {
    Complex result = {
        cos(com->real) * cosh(com->imag),
        sin(com->real) * sinh(com->imag)
    };

    return result;
}

Complex tan_complex(Complex* com) {
    Complex sinValue = sin_complex(com);
    Complex cosValue = cos_complex(com);

    return complex_divided_by_complex(&sinValue, &cosValue);
}

Complex sec_complex(Complex* com) {
    Complex cosValue = cos_complex(com);

    return number_divided_by_complex(1, &cosValue);
}

Complex csc_complex(Complex* com) {
    Complex sinValue = sin_complex(com);

    return number_divided_by_complex(1, &sinValue);
}

Complex cot_complex(Complex* com) {
    Complex tanValue = tan_complex(com);

    return number_divided_by_complex(1, &tanValue);
}

Complex sinh_complex(Complex* com) {
    Complex result = {
        sinh(com->real) * cos(com->imag),
        cosh(com->real) * sin(com->imag)
    };

    return result;
}

Complex cosh_complex(Complex* com) {
    Complex result = {
        cosh(com->real) * cos(com->imag),
        sinh(com->real) * sin(com->imag)  
    };

    return result;
}

Complex tanh_complex(Complex* com) {
    Complex sinhValue = sinh_complex(com);
    Complex coshValue = cosh_complex(com);

    return complex_divided_by_complex(&sinhValue, &coshValue);
}

Complex sech_complex(Complex* com) {
    Complex coshValue = cosh_complex(com);

    return number_divided_by_complex(1, &coshValue);
}

Complex csch_complex(Complex* com) {
    Complex sinhValue = sinh_complex(com);

    return number_divided_by_complex(1, &sinhValue);
}

Complex coth_complex(Complex* com) {
    Complex tanhValue = tanh_complex(com);

    return number_divided_by_complex(1, &tanhValue);
}

Complex asin_complex(Complex* com) {
    Complex a = complex_times_complex(&IMAG, com);
    Complex b = complex_times_complex(com, com);
    Complex c = number_minus_complex(1, &b);
    Complex d = sqrt_complex(&c);
    Complex e = complex_plus_complex(&a, &e);
    Complex f = negate_complex(&IMAG);

    return complex_times_complex(&f, &e);
}

Complex acos_complex(Complex* com) {
    Complex a = negate_complex(&IMAG);
    Complex b = complex_times_complex(com, com);
    Complex c = complex_minus_number(&b, 1);
    Complex d = sqrt_complex(&c);
    Complex e = complex_plus_complex(com, &d);
    Complex f = log_complex(&e);

    return complex_times_complex(&a, &f);
}

Complex atan_complex(Complex* com) {
    Complex a = complex_divided_by_number(&IMAG, 2);
    Complex b = complex_times_complex(&IMAG, com);
    Complex c = complex_plus_number(&b, 1);
    Complex d = number_minus_complex(1, &b);
    Complex e = log_complex(&c);
    Complex f = log_complex(&d);
    Complex g = complex_minus_complex(&e, &f);

    return complex_times_complex(&a, &g);
}

Complex asec_complex(Complex* com) {
    Complex acosValue = acos_complex(com);

    return number_divided_by_complex(1, &acosValue);
}

Complex acsc_complex(Complex* com) {
    Complex asinValue = asin_complex(com);

    return number_divided_by_complex(1, &asinValue);
}

Complex acot_complex(Complex* com) {
    Complex atanValue = atan_complex(com);

    return number_divided_by_complex(1, &atanValue);
}

Complex asinh_complex(Complex* com) {
    Complex a = complex_times_complex(com, com);
    Complex b = complex_plus_number(&a, 1);
    Complex c = sqrt_complex(&b);
    Complex d = complex_plus_complex(com, &c);

    return log_complex(&d);
}

Complex acosh_complex(Complex* com) {
    Complex a = complex_plus_number(com, 1);
    Complex b = complex_minus_number(com, 1);
    Complex c = sqrt_complex(&a);
    Complex d = sqrt_complex(&b);
    Complex e = complex_times_complex(&c, &d);
    Complex f = complex_plus_complex(com, &e);

    return log_complex(&f);
}

Complex atanh_complex(Complex* com) {
    Complex a = complex_plus_number(com, 1);
    Complex b = complex_minus_number(com, 1);
    Complex c = log_complex(&a);
    Complex d = log_complex(&b);
    Complex e = complex_minus_complex(&c, &d);

    return complex_times_number(&e, 0.5);
}

Complex asech_complex(Complex* com) {
    Complex acoshValue = acosh_complex(com);

    return number_divided_by_complex(1, &acoshValue);
}

Complex acsch_complex(Complex* com) {
    Complex asinhValue = asinh_complex(com);

    return number_divided_by_complex(1, &asinhValue);
}

Complex acoth_complex(Complex* com) {
    Complex atanhValue = atanh_complex(com);

    return number_divided_by_complex(1, &atanhValue);
}

double arg_complex(Complex* com) {
    return atan(com->imag / com->real);
}

Complex sqrt_complex(Complex* com) {
    return complex_to_power_of_number(com, 0.5);
}

Complex log_complex(Complex* com) {
    Complex result = {
        log(sqrt(com->real * com->real + com->imag * com->imag)),
        arg_complex(com)
    };

    return result;
}

Complex log10_complex(Complex* com) {
    Complex result = {
        log10(sqrt(com->real * com->real + com->imag * com->imag)),
        arg_complex(com)
    };

    return result;
}

Complex exp_complex(Complex* com) {
    return number_to_power_of_complex(M_E, com);
}
