#include <stdio.h>

#define ORDER 8
#define TWO_ORDER_POWER 256
#define SHARK_POLY 0x1f5
//Binary representation: 111110101
//Equivalent poly: x^8 + x^7 + x^6 + x^5 + x^4 + x^2 + 1
#define DEGREE_LIMIT_MASK 0x100
//Binary representation: 100000000
//Equivalent poly: x^8
#define IRREDUCIBLE_POLY SHARK_POLY
#define DIM 3

/*
	Other polynomials to add:
	- Square
	- BKSQ
	- Rijndael
	- Khazad
	- Anubis
	- ...
*/

unsigned int discrete_log_inverse [TWO_ORDER_POWER];
unsigned int discrete_log [TWO_ORDER_POWER];

void init_discrete_log() {
	discrete_log_inverse[0] = 1;
	for (int i = 1; i < TWO_ORDER_POWER; i++) {
		int j = discrete_log_inverse[i-1] << 1;
		if (j & DEGREE_LIMIT_MASK) {
			j ^= IRREDUCIBLE_POLY;
		}
		discrete_log_inverse[i] = j;
	}
	
	discrete_log[0] = 0;
	for (int i = 1; i < TWO_ORDER_POWER - 1; i++) {
		discrete_log[discrete_log_inverse[i]] = i;
	}
}

unsigned int add_poly(unsigned int poly1, unsigned int poly2) {
	return poly1 ^ poly2;
}

unsigned int subtract_poly(unsigned int poly1, unsigned int poly2) {
	return poly1 ^ poly2;
}

unsigned int multiply_poly(unsigned int poly1, unsigned int poly2) {
	if (poly1 == 0) {
		return 0;
	}
	if (poly2 == 0) {
		return 0;
	}
	unsigned int modulus = TWO_ORDER_POWER - 1;
	return discrete_log_inverse[(discrete_log[poly1] + discrete_log[poly2]) % modulus];
}

unsigned int invert_poly(unsigned int poly) {
	if (poly == 0) {
		return 0;
	}
	unsigned int modulus = TWO_ORDER_POWER - 1;
	return discrete_log_inverse[-discrete_log[poly] + modulus];
}

void matrix_multiplication(unsigned int result [DIM][DIM], unsigned int mat1 [DIM][DIM], unsigned int mat2 [DIM][DIM]) {
	for (int i = 0; i < DIM; i++) {
		for (int j = 0; j < DIM; j++) {
			result[i][j] = 0;
			
			for (int k = 0; k < DIM; k++) {
				unsigned int mul = multiply_poly(mat1[i][k], mat2[k][j]);
				unsigned int add = add_poly(result[i][j], mul);
				result[i][j] = add;
				//result[i][j] += mat1[i][k] * mat2[k][j], but * and + are in GF2^m
			}
		}
	}
}

void print_poly(unsigned int p, unsigned int base) {
	if (base == 10) {
		printf("%u ", p);	
	}
	else if (base == 16) {
		printf("0x%x ", p);
	}
}

void print_matrix(unsigned int mat [DIM][DIM], unsigned int base) {
	for (int i = 0; i < DIM; i++) {
		for (int j = 0; j < DIM; j++) {
			print_poly(mat[i][j], base);
		}
		printf("\n");
	}
}

/*void matrix_inversion(unsigned int** result, unsigned int **a, unsigned int dim) {
	return;
}*/

/*void test_det() {
	unsigned int a [2][2] = {{2, 3}, {4, 5}};
	print_matrix(a, 10);
	print_poly(matrix_determinant(a, 2, 2), 10);
}*/

void get_cofactor(unsigned int mat[DIM][DIM], unsigned int temp[DIM][DIM], int p, int q, int n) {
    int i = 0, j = 0;
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < n; col++) {
            if (row != p && col != q) {
                temp[i][j++] = mat[row][col];
                if (j == n - 1) {
                    j = 0;
                    i++;
                }
            }
        }
    }
}

unsigned int determinant_of_matrix(unsigned int mat[DIM][DIM], unsigned int n) {
    int D = 0;
 
    if (n == 1)
        return mat[0][0];
 
    unsigned int temp[DIM][DIM];
 
    int sign = 1;
 
    for (int f = 0; f < n; f++) {
        get_cofactor(mat, temp, 0, f, n);
        //D += sign * mat[0][f] * determinantOfMatrix(temp, n - 1)
		//in GF2^m
		
		unsigned int recursive_det = determinant_of_matrix(temp, n - 1);
		unsigned int mul = multiply_poly(mat[0][f], recursive_det);
		
		if (sign == 1) {
			D = add_poly(D, mul);
		} else {
			D = subtract_poly(D, mul);
		}
        sign = -sign;
    }
    return D;
}

void test_big_det() {
	unsigned int a [3][3] = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
	print_matrix(a, 16);
	print_poly(determinant_of_matrix(a, 3), 16);
}

/*void test_mul() {
	init_discrete_log();
	
	for (unsigned int p1 = 0; p1 < TWO_ORDER_POWER; p1++) {
		for (unsigned int p2 = 0; p2 < TWO_ORDER_POWER; p2++) {
			unsigned int result = multiply_poly(p1, p2);
			printf("%u * %u = %u\n", p1, p2, result);
		}
	}
}*/

/*void test_inv() {
	init_discrete_log();
	
	for (unsigned int p = 1; p < TWO_ORDER_POWER; p++) {
		unsigned int inverse = invert_poly(p);
		unsigned int mul_result = multiply_poly(p, inverse);
		if (mul_result == 1) {
			printf("OK\n");
		} else {
			printf("FAILED\n");
		}
	}
}*/

/*void test_matrix_mul() {
	unsigned int result [2][2] = {{0, 0}, {0, 0}};
	unsigned int a [2][2] = {{2, 3}, {4, 5}};
	unsigned int b [2][2] = {{6, 7}, {8, 9}};
	
	matrix_multiplication(result, a, b);
	print_matrix(result, 16);
}*/

int main() {
	init_discrete_log();
	//test_mul();
	//test_inv();
	//test_matrix_mul();
	//test_det();
	test_big_det();
	return 0;
}


