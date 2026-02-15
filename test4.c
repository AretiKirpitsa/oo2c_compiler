#include <stdio.h>
#include <stdlib.h>
typedef struct Point 
{
	int x, y;
} Point;
Point* Point_1_init(Point *self_ptr, int x, int y)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Point *)malloc(sizeof(Point));
		}
	self_ptr->x = x;
	self_ptr->y = y;
	return self_ptr;
}
int get_x_1(Point *self_ptr)
{
	return self_ptr->x;
}
int get_y_1(Point *self_ptr)
{
	return self_ptr->y;
}
void set_x_1(Point *self_ptr, int new_x)
{
	self_ptr->x = new_x;
}
int distance_from_origin_1(Point *self_ptr)
{
	return self_ptr->x * self_ptr->x + self_ptr->y * self_ptr->y;
}
typedef struct ColoredPoint 
{
	Point Point_parent;
	int color;
} ColoredPoint;
ColoredPoint* ColoredPoint_1_init(ColoredPoint *self_ptr, int x, int y, int color)
{
	if(self_ptr == NULL)
		{
		self_ptr = (ColoredPoint *)malloc(sizeof(ColoredPoint));
		}
	self_ptr->Point_parent.x = x;
	self_ptr->Point_parent.y = y;
	self_ptr->color = color;
	return self_ptr;
}
int get_color_1(ColoredPoint *self_ptr)
{
	return self_ptr->color;
}
void set_color_1(ColoredPoint *self_ptr, int new_color)
{
	self_ptr->color = new_color;
}
int main(void)
{
	struct Point *p = NULL;
	struct ColoredPoint *cp = NULL;
	int result;
	p = Point_1_init(NULL,  3, 4);
	printf("%d %d \n", get_x_1(p), get_y_1(p));
	result = distance_from_origin_1(p);
	printf("%d \n", result);
	set_x_1(p,  5);
	printf("%d \n", get_x_1(p));
	cp = ColoredPoint_1_init(NULL,  10, 20, 255);
	printf("%d %d %d \n", get_x_1(&cp->Point_parent), get_y_1(&cp->Point_parent), get_color_1(cp));
	set_color_1(cp,  128);
	printf("%d \n", get_color_1(cp));
	return 0;
}