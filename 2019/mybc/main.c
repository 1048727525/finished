#include "main.h"
//从输入的字符串中读取一个元素（符号or数字）
//reto = true时表示当前元素为运算符，retn记录当前元素，i记录下标
int get_op(char *str, int *reto, double *retn, int *i)
{
    int neg_label = 0;
    //略去表达式中的空格
    while (str[*i] == ' ')
    {
        *i += 1;
    }

    //将算式的开头记为EHEAD
    if(*i==0 && is_empty(&op)==1)
    {
        *reto = 1;
        *retn = EHEAD;
        //*retn = 0;
        return 1; 
    }
    //遍历字符为null，并将算式尾记为EHEAD
    if(str[*i]==0)
    {
        *reto = 1;
        *retn = EHEAD;
        return 1;
    }
    //遍历字符为数字
    if(str[*i]>='0'&&str[*i]<='9')
    {
        *reto =0;
    }
    //遍历字符为字母时，将字母连续读出
    else if((str[*i]>='A'&&str[*i]<='Z')||(str[*i]>='a'&&str[*i]<='z'))
    {
        *reto = 2;
        int tmp = str[*i];
        *retn = tmp;
        return 1;
    }
    //判断"-"是否为负号；"+"是否为正号
    else if((str[*i]=='+'||str[*i]=='-')&&((*i)==0||(is_num(str[(*i)-1])==0)||str[(*i)-1]=='('))
    {
        *reto = 0;
        if(str[*i]=='-')
            neg_label = 1;
        (*i)++;
    }
    else
    {
        *reto = 1;
        //为各个运算符设定优先级
        switch (str[*i])
        {
        case '(': *retn = 100; break;
        case ')': *retn = -1; break;
        case '+': *retn = 1; break;
        case '-': *retn = 2; break;
        case '*': *retn = 3; break;
        case '/': *retn = 4; break;
        case '^': *retn = 5; break;
        case ',': *retn = 6; break;
        default:
            return put_error(0);
            break;
        }
        *i += 1;
        return 1;
    }
    
    *retn = 0;
    //整数部分存储
    for(;str[*i]>='0'&&str[*i]<='9';(*i)++)
    {
        (*retn) *= 10;
        (*retn) += str[*i] - '0'; 
    }
    //小数部分存储
    double tmp = 0;
    int point_last = 0;
    if(str[*i] == '.')
    {
        (*i)++;
        for(;str[*i]>='0'&&str[*i]<='9';(*i)++)
        {
            point_last ++;
            tmp += (str[*i] - '0')*pow(0.1, point_last);
        }
    }
    *retn += tmp;
    //变负数
    if(neg_label==1)
    {
        *retn = 0-(*retn);
        neg_label = 0;
    }
    return 1;
}

void putstr(char *c)
{
    for(int i = 0; c[i]!=0; i++)
    {
        putchar(c[i]);
    }
}

double function_compute(int fun_label, double fun_para, double *paras)
{
    //根据不同的函数标识，返回不同的运算结果
    switch (fun_label)
    {
    case 0:
        return fun_para;
        break;
    case 1:
        return sin(fun_para);
    case 2:
        return cos(fun_para);
    case 3:
        return log(fun_para);
    case 4:
        return exp(fun_para);
    case 5:
        return sqrt(fun_para);
    case 6:
        return fabs(fun_para);
    case 7:
        return pow(fun_para, paras[0]);
    default:
        break;
    }
}

//计算带括号的计算式子
double calculator_brackets(char *str)
{
    //判断是否括号匹配
    int match_label = 0;
    for(int i =0; str[i]!=0;i++)
    {
        //判断是否为合法输入
        if(is_legel(str[i])==0)
            return put_error(0);
        if(str[i]=='(')
            match_label++;
        else if(str[i]==')')
        {
            match_label--;
        }
    }
    if (match_label!=0)
        return put_error(1);

    int reto = -1;
    double retn = EHEAD;
    int i = 0;
    //清空数字栈与运算符栈
    while (is_empty(&op) == 0)
    {
        if(pop_stack(&op)==1.01)
            return -1;
    }
    while (is_empty(&num) == 0)
    {
        if(pop_stack(&num)==1.01)
            return -1;
    }
    char va[STR_SIZE];
    double paras[DOUBLE_SIZE];
    int paras_pos = 0;
    int lb = 0;
    while (1)
    {
        if(get_op(str, &reto, &retn, &i)==-1)
            return -1;
        //如果当前读入为数字，直接存储
        if(reto == 0)
        {
            clear_str(va);
            if(push_stack(&num, retn)==-1)
                return -1;
        }
        //如果是字母则读取全部字母，并进行相应的判断
        else if(reto==2)
        {
            //printf("%i\n", (int)retn);
            int add_char = (int)retn;
            if (strlen(va)<STR_SIZE)
                va[strlen(va)]=(char)add_char;
            else
            {
                return put_error(0);
            }
            if(strcmp("pi", va)==0&&is_character(str[i+1])==0)
            {
                clear_str(va);
                if(push_stack(&num, pi)==-1)
                    return -1;
            }
            else if(strcmp("e", va)==0&&is_character(str[i+1])==0)
            {
                clear_str(va);
                if(push_stack(&num, e)==-1)
                    return -1;
            }
            else if(strcmp("sin", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 1)==-1)
                        return -1;
                    if(push_stack(&op, 100)==-1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function sin(x) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("cos", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 2)==-1)
                        return -1;
                    if(push_stack(&op, 100)==-1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function cos(x) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("ln", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 3)==-1)
                        return -1;
                    if(push_stack(&op, 100) == -1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function ln(x) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("exp", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 4)==-1)
                        return -1;
                    if(push_stack(&op, 100)==-1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function exp(x) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("sqrt", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 5)==-1)
                        return -1;
                    if(push_stack(&op, 100)==-1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function sqrt(x) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("fabs", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 6)==-1)
                        return -1;
                    if(push_stack(&op, 100)==-1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function fabs(x) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("power", va)==0)
            {
                if(str[i+1]=='(')
                {
                    if(push_stack(&fun, 7)==-1)
                        return -1;
                    if(push_stack(&op, 100)==-1)
                        return -1;
                    i++;
                    clear_str(va);
                }
                else
                {
                    printf("The function power(x, y) has been used mistakely");
                    return -1;
                }
            }
            else if(strcmp("exit", va)==0)
            {
                return -1;
            }
            i++;
        }
        else
        {
            clear_str(va);
            if (retn == 100)
            {
                if(push_stack(&fun, 0)==-1)
                    return -1;
            }
            double tmp;
            //若运算堆栈为空或当前读入的运算符优先级大于栈顶运算符，将该运算符压入堆栈
            if(is_empty(&op)==1 || retn>=get_top(&op))
            {
                if(retn == -1)
                {
                    return put_error(1);
                }
                if(push_stack(&op, retn)==-1)
                    return -1;

            }
            else
            {
                //只要当前运算符优先级小于栈顶运算符，重复循环
                while (retn<get_top(&op))
                {
                    if (retn == -1)
                        lb=1;
                    //如果符号栈中栈顶为左括号，则弹出栈顶，并跳出循环
                    if(get_top(&op)==100)
                    {
                        
                        if(lb==1)
                        {
                            double fun_label_d = pop_stack(&fun);
                            if(fun_label_d==-1.01)
                                return -1;
                            int fun_label = (int)fun_label_d;
                            double fun_para = pop_stack(&num);
                            if(fun_para==-1.01)
                                return -1;
                            if(push_stack(&num, function_compute(fun_label, fun_para, paras))==-1)
                                return -1;
                            if(pop_stack(&op)==-1.01)
                                return -1;
                            lb = 0;
                        }
                        break;
                    }
                    int ret = get_top(&op);
                    if(pop_stack(&op) == -1.01)
                        return -1;
                    double b = get_top(&num);
                    if(pop_stack(&num)==-1.01)
                        return -1;
                    double a = get_top(&num);
                    if(pop_stack(&num)==-1.01)
                        return -1;
                    switch (ret)
                    {
                    case 1:
                        tmp = a + b;
                        break;
                    case 2:
                        tmp = a - b;
                        break;
                    case 3:
                        tmp = a * b;
                        break;
                    case 4:
                        tmp = a / b;
                        break;
                    case 5:
                        tmp = pow (a, b);
                    case 6:
                        paras[paras_pos++] = b;
                        tmp = a;
                        break;
                    default:
                        break;
                    }
                    
                    if(push_stack(&num, tmp)==-1)
                        return -1;
                }
                if(retn != -1)
                {
                    if(push_stack(&op, retn)==-1)
                        return -1;
                }
                
                
            }
        }
        if(get_size(&op) == 2 && get_top(&op) == EHEAD)
        {
            break;
        }
    }
    if(is_empty(&num) == 1)
        {
            return put_error(0);
        }
    return get_top(&num);
}

//预处理输入的公式，处理特殊情况
int pre_handle_str(char *str)
{
    char str_no_block[STACK_SIZE];
    clear_str(str_no_block);
    int m = 0;
    for(int i =0; str[i]!=0;i++)
    {
        while (str[i] == ' ')
        {
            i += 1;
        }
        str_no_block[m++] = str[i];
    }
    //对精度进行设置，利用"scale=”的命令设置精度
    char str_scale[STR_SIZE] = "scale=";
    int scale_tmp = 0;
    if(strncmp(str_scale, str_no_block, 6)==0)
    {
        for (int i = 6;str_no_block[i]!=0;i++)
        {
            if ((str_no_block[i]>='0'&&str_no_block[i]<='9')==0)
            {
                return put_error(0);
            }
            scale_tmp *= 10;
            scale_tmp += str_no_block[i] - '0'; 
        }
        jump_label = 1;
        scale = scale_tmp;
    }
    //对命令提示符进行设置，利用”cmd=“的命令设置命令提示符
    char str_label[STR_SIZE] = "cmd=";
    if(strncmp(str_label, str_no_block, 4)==0)
    {
        clear_str(cmd);
        int m = 0;
        for(int i = 4;str_no_block[i]!=0;i++)
        {
            cmd[m++]=str_no_block[i];
        }
        jump_label = 1;
    }
    return 1;
}

int clear_str(char *str)
{
    int i = 0;
    while (str[i]!=0)
    {
        str[i++]=0;
    }
    return 1;
    
}


int main() 
{
    char *keyword[KEY_WORD_SIZE];
    double value[KEY_WORD_SIZE];


    init_stack(&op);
    init_stack(&num);
    while (1)
    {
        jump_label = 0;
        putstr(cmd);
        char *str[STACK_SIZE];
        gets(str);
        if(pre_handle_str(str)==-1)
            continue;

        if (jump_label==0)
        {
            double res = calculator_brackets(str);
            printf("%.*f\n", scale, res);
            if(res == -1)
                continue;
        }
            
        //printf("%.*f\n", scale, calculator_no_brackets(str));
    } 
    
    
    return 0;
}