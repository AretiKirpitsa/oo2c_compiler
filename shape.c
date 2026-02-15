#include <stdio.h>
#include <stdlib.h>
typedef struct Shape 
{
	int x, y;
	int color;
} Shape;
Shape* Shape_1_init(Shape *self_ptr, int x, int y)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Shape *)malloc(sizeof(Shape));
		}
	self_ptr->x = x;
	self_ptr->y = y;
	return self_ptr;
}
Shape* Shape_2_init(Shape *self_ptr, int x, int y, int color)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Shape *)malloc(sizeof(Shape));
		}
	self_ptr->x = x;
	self_ptr->y = y;
	self_ptr->color = color;
	return self_ptr;
}
void move_1(Shape *self_ptr, int dx, int dy)
{
	self_ptr->x = self_ptr->x + dx;
	self_ptr->y = self_ptr->y + dy;
}
void move_2(Shape *self_ptr, int dx)
{
	self_ptr->x = self_ptr->x + dx;
}
void set_x_1(Shape *self_ptr, int x)
{
	self_ptr->x = x;
}
int get_x_1(Shape *self_ptr)
{
	return self_ptr->x;
}
typedef struct Circle 
{
	Shape Shape_parent;
	int radius;
	int color;
} Circle;
Circle* Circle_1_init(Circle *self_ptr, int radius)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Circle *)malloc(sizeof(Circle));
		}
	self_ptr->radius = radius;
	return self_ptr;
}
Circle* Circle_2_init(Circle *self_ptr, int x, int y, int color, int radius)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Circle *)malloc(sizeof(Circle));
		}
	self_ptr->Shape_parent.x = x;
	self_ptr->Shape_parent.y = y;
	self_ptr->color = color;
	self_ptr->radius = radius;
	return self_ptr;
}
int get_radius_1(Circle *self_ptr)
{
	return self_ptr->radius;
}
int area_1(Circle *self_ptr)
{
	int int_pi;
	int_pi = 3;
	return int_pi * self_ptr->radius * self_ptr->radius;
}
typedef struct Square 
{
	Shape Shape_parent;
	int side;
} Square;
Square* Square_1_init(Square *self_ptr, int side)
{
	if(self_ptr == NULL)
		{
		self_ptr = (Square *)malloc(sizeof(Square));
		}
	self_ptr->side = side;
	return self_ptr;
}
int get_side_1(Square *self_ptr)
{
	return self_ptr->side;
}
int area_2(Square *self_ptr)
{
	return self_ptr->side * self_ptr->side;
}
typedef struct SquareWithCirclesOnCorners 
{
	Square Square_parent;
	Circle Circle_parent;
} SquareWithCirclesOnCorners;
SquareWithCirclesOnCorners* SquareWithCirclesOnCorners_1_init(SquareWithCirclesOnCorners *self_ptr, int side, int radius)
{
	if(self_ptr == NULL)
		{
		self_ptr = (SquareWithCirclesOnCorners *)malloc(sizeof(SquareWithCirclesOnCorners));
		}
	self_ptr->Square_parent.side = side;
	self_ptr->Circle_parent.radius = radius;
	return self_ptr;
}
int area_3(SquareWithCirclesOnCorners *self_ptr)
{
	int int_pi;
	int_pi = 3;
	return get_side_1(&self_ptr->Square_parent) * get_side_1(&self_ptr->Square_parent) + 3 * int_pi * get_radius_1(&self_ptr->Circle_parent) * get_radius_1(&self_ptr->Circle_parent);
}
typedef struct SquareWithCirclesOnCorners2 
{
	struct Square *s;
	struct Circle *c;
} SquareWithCirclesOnCorners2;
SquareWithCirclesOnCorners2* SquareWithCirclesOnCorners2_1_init(SquareWithCirclesOnCorners2 *self_ptr, int side, int radius)
{
	if(self_ptr == NULL)
		{
		self_ptr = (SquareWithCirclesOnCorners2 *)malloc(sizeof(SquareWithCirclesOnCorners2));
		}
	self_ptr->s = Square_1_init(NULL,  side);
	self_ptr->c = Circle_1_init(NULL,  radius);
	return self_ptr;
}
int area_4(SquareWithCirclesOnCorners2 *self_ptr)
{
	int int_pi_part;
	int_pi_part = 3;
	return get_side_1(self_ptr->s) * get_side_1(self_ptr->s) + 3 * int_pi_part * get_radius_1(self_ptr->c) * get_radius_1(self_ptr->c);
}
int main(void)
{
	struct Circle *c = NULL;
	struct Square *s = NULL;
	struct SquareWithCirclesOnCorners *s1 = NULL;
	struct SquareWithCirclesOnCorners2 *s2 = NULL;
	c = Circle_1_init(NULL,  4);
	printf("%d \n", area_1(c));
	s = Square_1_init(NULL,  4);
	printf("%d \n", area_2(s));
	s1 = SquareWithCirclesOnCorners_1_init(NULL,  3, 5);
	s2 = SquareWithCirclesOnCorners2_1_init(NULL,  3, 5);
	printf("%d \n", area_3(s1));
	printf("%d \n", area_4(s2));
	return 0;
}