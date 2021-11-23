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
#define DIM 8

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

unsigned int poly_xtime_cost(unsigned int poly) {
	unsigned int degree_mask = DEGREE_LIMIT_MASK;
	unsigned int degree = ORDER;
	while ((poly & degree_mask) == 0) {
		degree_mask >>= 1;
		degree--;
	}
	return degree;
}

unsigned int poly_xor_cost(unsigned int poly) {
	unsigned int mask = 1;
	unsigned int set_bits = 0;
	unsigned int current_bit = 0;
	while (current_bit <= ORDER) {
		set_bits += ((poly & mask) != 0);
		mask <<= 1;
		current_bit++;
	}
	return set_bits - 1;
}

unsigned int matrix_xtime_cost(unsigned int mat [DIM][DIM]) {
	unsigned int total_cost = 0;
	for (int row = 0; row < DIM; row++) {
		unsigned int row_cost = 0;
		for (int col = 0; col < DIM; col++) {
			row_cost += poly_xtime_cost(mat[row][col]);
		}
		printf("Row %d costs %d xtime\n", row, row_cost);
		total_cost += row_cost;
	}
	printf("The full matrix costs %d xtime\n", total_cost);
	return total_cost;
}

unsigned int matrix_xor_cost(unsigned int mat[DIM][DIM]) {
	unsigned int total_cost = 0;
	for (int row = 0; row < DIM; row++) {
		unsigned int row_cost = DIM - 1; //sum elements
		for (int col = 0; col < DIM; col++) {
			row_cost += poly_xor_cost(mat[row][col]);
		}
		printf("Row %d costs %d xor\n", row, row_cost);
		total_cost += row_cost;
	}
	printf("The full matrix costs %d xor\n", total_cost);
	return total_cost;
}

void matrix_total_cost(unsigned int mat[DIM][DIM]) {
	unsigned int xtime = matrix_xtime_cost(mat);
	unsigned int xor = matrix_xor_cost(mat);
	printf("This matrix requires %d xor and %d xtime\n", xor, xtime);
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

/*void test_big_det() {
	unsigned int a [3][3] = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
	print_matrix(a, 16);
	print_poly(determinant_of_matrix(a, 3), 16);
}*/

/*void test_matrix_cost_square() {
	unsigned int square_mat [4][4] = {
		{0x02, 0x01, 0x01, 0x03},
		{0x03, 0x02, 0x01, 0x01},
		{0x01, 0x03, 0x02, 0x01},
		{0x01, 0x01, 0x03, 0x02}
	};
	
	unsigned int square_mat_inv [4][4] = {
		{0x0e, 0x09, 0x0d, 0x0b},
		{0x0b, 0x0e, 0x09, 0x0d},
		{0x0d, 0x0b, 0x0e, 0x09},
		{0x09, 0x0d, 0x0b, 0x0e}
	};
	
	matrix_total_cost(square_mat_inv);
}*/

void test_matrix_cost_shark() {
	unsigned int shark [8][8] = {
		{0xce, 0x95, 0x57, 0x82, 0x8a, 0x19, 0xb0, 0x01},
		{0xe7, 0xfe, 0x05, 0xd2, 0x52, 0xc1, 0x88, 0xf1},
		{0xb9, 0xda, 0x4d, 0xd1, 0x9e, 0x17, 0x83, 0x86},
		{0xd0, 0x9d, 0x26, 0x2c, 0x5d, 0x9f, 0x6d, 0x75},
		{0x52, 0xa9, 0x07, 0x6c, 0xb9, 0x8f, 0x70, 0x17},
		{0x87, 0x28, 0x3a, 0x5a, 0xf4, 0x33, 0x0b, 0x6c},
		{0x74, 0x51, 0x15, 0xcf, 0x09, 0xa4, 0x62, 0x09},
		{0x0b, 0x31, 0x7f, 0x86, 0xbe, 0x05, 0x83, 0x34}
	};
	
	unsigned int shark_inv [8][8] = {
		{0xe7, 0x30, 0x90, 0x85, 0xd0, 0x4b, 0x91, 0x41},
		{0x53, 0x95, 0x9b, 0xa5, 0x96, 0xbc, 0xa1, 0x68},A AAkkkaaaKKdjskhdoi
		{0x02, 0x45, 0xf7, 0x65, 0x5c, 0x1f, 0xb6, 0x52},
		{0xa2, 0xca, 0x22, 0x94, 0x44, 0x63, 0x2a, 0xa2},
		{0xfc, 0x67, 0x8e, 0x10, 0x29, 0x75, 0x85, 0x71},
		{0x24, 0x45, 0xa2, 0xcf, 0x2f, 0x22, 0xc1, 0x0e},
		{0xa1, 0xf1, 0x71, 0x40, 0x91, 0x27, 0x18, 0xa5},
		{0x56, 0xf4, 0xaf, 0x32, 0xd2, 0xa4, 0xdc, 0x71}
	};
	matrix_total_cost(shark_inv);
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
	//test_big_det();
	//unsigned int p = 0xce;
	//printf("%d", poly_xtime_cost(p));
	//printf("%d", poly_xor_cost(p));
	test_matrix_cost_shark();
	return 0;
}


