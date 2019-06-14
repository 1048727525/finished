#include "stack.h"
typedef double DataType;
//init stack
void init_stack(struct stack*s)
{
    memset(s->ele, 0, sizeof(s->ele));
    s->top = -1;
}

//push stack
int push_stack(struct stack*s, DataType data)
{
    if(s->top + 1 == STACK_SIZE)
    {
        printf("Error:The stack is full.\n");
        return -1;
    }
    else
    {
        s->top += 1;
        s->ele[s->top] = data;
        return 1;
    }
}

//pop stack
DataType pop_stack(struct stack*s)
{
    if(s->top == -1)
    {
        printf("Error:The stack is empty.\n");
        return -1.01;
    }
    else
    {
        DataType tmp = s->ele[s->top];
        (s->top)--;
        return tmp;
    }   
}

//destory stack
int destory(struct stack *s)
{
	s->top = -1;
	memset(s->ele, 0, sizeof(s->ele));
    return 0;
}

//traverse
int traverse(struct stack *s)
{
    for(int i =0;i<=(s->top);i++)
    {
        printf("%.2f", s->ele[i]);
        printf(" ");
    }
    printf("\n");
    return 0;
}

//stack op
int is_empty(struct stack *s)
{
    if (s-> top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

//get stack top
DataType get_top(struct stack *s)
{ 
    if(is_empty(s)==1)
    {
        printf("Error:The stack is empty.\n");
        return -1.01;
    }
    else
    {
        return s->ele[s->top];
    }
}

//get the len of stack
int get_size(struct stack *s)
{
    return (s->top + 1);
}