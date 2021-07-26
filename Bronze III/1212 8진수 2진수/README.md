# 1212 8진수 2진수

URL : [https://www.acmicpc.net/problem/1212](https://www.acmicpc.net/problem/1212)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

#define CHAR_TO_NUM(X) ((X)-(48))
char number[333335]; // 8진수 문자열

void InputData()
{
    scanf("%s", number);
    return;
}

void makeBin(int n, char first)
{
    int temp = n;

    if(first && temp==0){ printf("0"); }

    if(temp >= 4)
    { 
        temp -= 4; 
        first = 0;
        printf("1"); 
    }
    else if(!first){ printf("0"); }

    if(temp >= 2)
    { 
        temp -= 2; 
        first = 0;
        printf("1"); 
    }
    else if(!first){ printf("0"); }

    if(temp >= 1)
    { 
        temp -= 1; 
        printf("1"); 
    }
    else if(!first){ printf("0"); }
}

void octTobin()
{
    int i;
    char first = 1;

    for(i=0; number[i]!='\0'; i++)
    {   
        makeBin((int)CHAR_TO_NUM(number[i]), first);
        first = 0;
    }
}

int main(void)
{
    InputData();
    octTobin();

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>

void    set_binary(char **b_set)
{
    b_set[0] = "0";
    b_set[1] = "1";
    b_set[2] = "10";
    b_set[3] = "11";
    b_set[4] = "100";
    b_set[5] = "101";
    b_set[6] = "110";
    b_set[7] = "111";
}

int     get_length(char *n)
{
    int     len;

    len = 0;
    while (n[len])
        len++;
    return (len);
}

void    get_octal(char *octl, char **b_set)
{
    int     i;
    int     oct_len;
    int     b_len;
    char    zero[3][3] = { "\0", "0", "00" };

    if (octl)
    {
        oct_len = get_length(octl);
        printf("%s", b_set[octl[0] - 48]);
    }
    i = 1;
    b_len = 0;
    while (i < oct_len)
    {
        b_len = 3 - get_length(b_set[octl[i] - 48]);
        printf("%s", zero[b_len]);
        printf("%s", b_set[octl[i] - 48]);
        i++;
    }
    if (octl)
        printf("\n");
}

int     main(void)
{
    char    **binary_set;
    char    *octal;
 
    if (!(binary_set = malloc(sizeof(char *) * 8)))
        return (0);
    else
        set_binary(binary_set);
    if (!(octal = malloc(sizeof(char) * 333335)))
        return (0);
    else
    {
        scanf("%s", octal);
        get_octal(octal, binary_set);
    }
    if (binary_set && octal)
    {
        free(binary_set);
        free(octal);
    }
    return (0);
}
```