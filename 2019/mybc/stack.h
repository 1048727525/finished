#define STACK_SIZE 100
typedef double DataType;
typedef struct stack
{
    DataType ele[STACK_SIZE];
    int top;
};
//init stack
void init_stack(struct stack*s);
//push stack
int push_stack(struct stack*s, DataType data);
//pop stack
DataType pop_stack(struct stack*s);
//destory stack
int destory(struct stack *s);
//traverse
int traverse(struct stack *s);
//stack op
int is_empty(struct stack *s);
//get stack top
DataType get_top(struct stack *s);
//get the len of stack
int get_size(struct stack *s);

