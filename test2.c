#include <stdio.h>
#include <stdlib.h>
typedef struct Counter 
{
	int count;
} Counter;
Counter* Counter_1_init(Counter *self_ptr, int start)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Counter *)malloc(sizeof(Counter));
		}
	self_ptr->count = start;
	return self_ptr;
}
void increment_1(Counter *self_ptr)
{
	self_ptr->count = self_ptr->count + 1;
}
int get_count_1(Counter *self_ptr)
{
	return self_ptr->count;
}
int main(void)
{
	struct Counter *c = NULL;
	c = Counter_1_init(NULL,  0);
	printf("%d \n", get_count_1(c));
	increment_1(c);
	printf("%d \n", get_count_1(c));
	increment_1(c);
	printf("%d \n", get_count_1(c));
	return 0;
}