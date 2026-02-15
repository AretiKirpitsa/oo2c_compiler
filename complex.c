#include <stdio.h>
#include <stdlib.h>
typedef struct Complex 
{
	int real, img;
} Complex;
Complex* Complex_1_init(Complex *self_ptr)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Complex *)malloc(sizeof(Complex));
		}
	self_ptr->real = 0;
	self_ptr->img = 0;
	return self_ptr;
	return self_ptr;
}
Complex* Complex_2_init(Complex *self_ptr, int real, int img)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Complex *)malloc(sizeof(Complex));
		}
	self_ptr->real = real;
	self_ptr->img = img;
	return self_ptr;
	return self_ptr;
}
void set_real_1(Complex *self_ptr, int real)
{
	self_ptr->real = real;
}
void set_img_1(Complex *self_ptr, int img)
{
	self_ptr->img = img;
}
Complex* get_complex_1(Complex *self_ptr)
{
	return self_ptr;
}
void set_complex_1(Complex *self_ptr, int real, int img)
{
	self_ptr->real = real;
	self_ptr->img = img;
}
int get_real_1(Complex *self_ptr)
{
	return self_ptr->real;
}
int get_img_1(Complex *self_ptr)
{
	return self_ptr->img;
}
int squared_modulus_1(Complex *self_ptr)
{
	return self_ptr->real * self_ptr->real + self_ptr->img * self_ptr->img;
}
void add_1(Complex *self_ptr, Complex *c1, Complex *c2)
{
	self_ptr->real = c1->real + c2->real;
	self_ptr->img = c1->img + c2->img;
}
void print_complex_1(Complex *self_ptr)
{
	printf("%d %d \n", self_ptr->real, self_ptr->img);
}
int main(void)
{
	struct Complex *c1 = NULL, *c2 = NULL, *c3 = NULL;
	c1 = Complex_2_init(NULL,  1, 2);
	c2 = Complex_2_init(NULL,  3, 4);
	c3 = Complex_1_init(NULL);
	print_complex_1(c1);
	print_complex_1(c2);
	add_1(c3,  c1, c2);
	print_complex_1(c3);
	set_real_1(c3,  squared_modulus_1(c1));
	set_img_1(c3,  squared_modulus_1(c2));
	print_complex_1(c3);
	return 0;
}