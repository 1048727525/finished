#include "check.h"
int is_num(char x)
{
    if(x>='0'&&x<='9')
        return 1;
    else
        return 0;
}

int is_character(char x)
{
    int m = (int)x;
    if((m>='A'&&m<='Z')||(m>='a'&&m<='z'))
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int is_op(char x)
{
    switch (x)
    {
    case '+':
        break;
    case '-':
        break;
    case '*':
        break;
    case '/':
        break;
    case '^':
        break;
    case ',':
        break;
    case ' ':
        break;
    case '.':
        break;
    default:
        return 0;
        break;
    }
    return 1;
}

int is_brackets(char x)
{
    if(x=='('||x==')')
        return 1;
    return 0;
}

int is_legel(char x)
{
    if(is_num(x)==1)
        return 1;
    else if(is_character(x)==1)
        return 1;
    else if(is_op(x)==1)
        return 1;
    else if(is_brackets(x)==1)
        return 1;
    else
        return 0;    
    
}