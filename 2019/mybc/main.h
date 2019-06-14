#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <errno.h>
#include "stack.h"
#include "myerror.h"
#include "check.h"
#include <string.h>
#define STACK_SIZE 100
#define DOUBLE_SIZE 100
#define EHEAD -100
#define STR_SIZE 100
#define KEY_WORD_SIZE 100
#define pi 3.1415926
#define e 2.7182818284
int scale=2;
struct stack op;
struct stack num;
struct stack fun;
int jump_label = 0;
char cmd[STR_SIZE] = "->";
//从输入的字符串中读取一个元素（符号or数字）
//reto = true时表示当前元素为运算符，retn记录当前元素，i记录下标
int get_op(char *str, int *reto, double *retn, int *i);
void putstr(char *c);
double function_compute(int fun_label, double fun_para, double *paras);
//计算带括号的计算式子
double calculator_brackets(char *str);
int pre_handle_str(char *str);
int clear_str(char *str);