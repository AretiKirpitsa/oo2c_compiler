#include <stdio.h>
#include <stdlib.h>
typedef struct Calculator 
{
	int value;
} Calculator;
Calculator* Calculator_1_init(Calculator *self_ptr)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Calculator *)malloc(sizeof(Calculator));
		}
	self_ptr->value = 0;
	return self_ptr;
}
Calculator* Calculator_2_init(Calculator *self_ptr, int initial)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Calculator *)malloc(sizeof(Calculator));
		}
	self_ptr->value = initial;
	return self_ptr;
}
void add_1(Calculator *self_ptr, int a)
{
	self_ptr->value = self_ptr->value + a;
}
void add_2(Calculator *self_ptr, int a, int b)
{
	self_ptr->value = self_ptr->value + a + b;
}
void multiply_1(Calculator *self_ptr, int factor)
{
	self_ptr->value = self_ptr->value * factor;
}
int get_value_1(Calculator *self_ptr)
{
	return self_ptr->value;
}
void reset_1(Calculator *self_ptr)
{
	self_ptr->value = 0;
}
int main(void)
{
	struct Calculator *c1 = NULL, *c2 = NULL;
	int temp;
	c1 = Calculator_1_init(NULL);
	printf("%d \n", get_value_1(c1));
	add_1(c1,  5);
	printf("%d \n", get_value_1(c1));
	add_2(c1,  3, 7);
	printf("%d \n", get_value_1(c1));
	multiply_1(c1,  2);
	printf("%d \n", get_value_1(c1));
	c2 = Calculator_2_init(NULL,  100);
	printf("%d \n", get_value_1(c2));
	add_1(c2,  50);
	printf("%d \n", get_value_1(c2));
	return 0;
}