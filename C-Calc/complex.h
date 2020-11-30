#ifndef COMPLEX_H
#define COMPLEX_H


typedef struct complex_t {
    double real;
    double imag;
} Complex;

Complex IMAG;

Complex complex_plus_number(Complex* left, double right);

Complex complex_plus_complex(Complex* left, Complex* right);

Complex number_minus_complex(double left, Complex* right);

Complex complex_minus_number(Complex* left, double right);

Complex complex_minus_complex(Complex* left, Complex* right);

Complex complex_times_number(Complex* left, double right);

Complex complex_times_complex(Complex* left, Complex* right);

Complex number_divided_by_complex(double left, Complex* right);

Complex complex_divided_by_number(Complex* left, double right);

Complex complex_divided_by_complex(Complex* left, Complex* right);

Complex number_to_power_of_complex(double left, Complex* right);

Complex complex_to_power_of_number(Complex* left, double right);

Complex complex_to_power_of_complex(Complex* left, Complex* right);

Complex conjugate_complex(Complex* com);

Complex negate_complex(Complex* com);

double abs_complex(Complex* complex);

Complex normalize_complex(Complex* complex);

int complex_equals_number(Complex* left, double right);

int complex_equals_complex(Complex* left, Complex* right);

Complex sin_complex(Complex* com);

Complex cos_complex(Complex* com);

Complex tan_complex(Complex* com);

Complex sec_complex(Complex* com);

Complex csc_complex(Complex* com);

Complex cot_complex(Complex* com);

Complex sinh_complex(Complex* com);

Complex cosh_complex(Complex* com);

Complex tanh_complex(Complex* com);

Complex sech_complex(Complex* com);

Complex csch_complex(Complex* com);

Complex coth_complex(Complex* com);

Complex asin_complex(Complex* com);

Complex acos_complex(Complex* com);

Complex atan_complex(Complex* com);

Complex asec_complex(Complex* com);

Complex acsc_complex(Complex* com);

Complex acot_complex(Complex* com);

Complex asinh_complex(Complex* com);

Complex acosh_complex(Complex* com);

Complex atanh_complex(Complex* com);

Complex asech_complex(Complex* com);

Complex acsch_complex(Complex* com);

Complex acoth_complex(Complex* com);

double arg_complex(Complex* com);

Complex sqrt_complex(Complex* com);

Complex log_complex(Complex* com);

Complex log10_complex(Complex* com);

Complex exp_complex(Complex* com);

const char* to_string_complex(Complex* com);


#endif
