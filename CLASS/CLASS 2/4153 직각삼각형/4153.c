#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

void ShowResult(int a, int b, int c)
{
    if( a*a == (b*b) + (c*c))
        printf("right\n");
    else
        printf("wrong\n");
}

int main(void)
{
    int a, b, c;

    do
    {
        scanf("%d %d %d", &a, &b, &c);

        if(a>b && a>c)
            ShowResult(a, b, c);
        else if(b>a && b>c)
            ShowResult(b, a, c);
        else if(c>a && c>b)
            ShowResult(c, b, a);
    }
    while(a!=0 && b!=0 && c!=0);

    return 0;
}