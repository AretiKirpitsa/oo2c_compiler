#include <stdio.h>
#include <stdlib.h>
typedef struct NumberProcessor 
{
	int value;
} NumberProcessor;
NumberProcessor* NumberProcessor_1_init(NumberProcessor *self_ptr, int v)
{
	if(self_ptr == NULL)
		{
		self_ptr = (NumberProcessor *)malloc(sizeof(NumberProcessor));
		}
	self_ptr->value = v;
	return self_ptr;
}
int get_value_1(NumberProcessor *self_ptr)
{
	return self_ptr->value;
}
int is_positive_1(NumberProcessor *self_ptr)
{
	int result;
	result = 0;

	if(self_ptr->value > 0)
{
	result = 1;
	}
	else
	{
	result = 0;
	}

	return result;
}
int sum_to_value_1(NumberProcessor *self_ptr)
{
	int sum, i;
	sum = 0;
	i = 1;

	while(i <= self_ptr->value)
{
	sum = sum + i;
	i = i + 1;
	}
	return sum;
}
int main(void)
{
	struct NumberProcessor *np = NULL;
	int result;
	np = NumberProcessor_1_init(NULL,  5);
	printf("%d \n", get_value_1(np));
	result = is_positive_1(np);
	printf("%d \n", result);
	result = sum_to_value_1(np);
	printf("%d \n", result);
	return 0;
}