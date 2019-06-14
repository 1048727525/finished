#include <stdio.h>
int put_error(int i)
{
    switch (i)
    {
    case 0:
        printf("Error:illegal input\n");
        return -1;
        break;
    case 1:
        printf("Error:括号不匹配\n");
        return -1;
        break;
    case 2:
        printf("Error:The stack is full.\n");
        return -1;
        break;
    case 3:
        printf("Error:The stack is empty.\n");
        return -1;
        break;
    default:
        break;
    }
}