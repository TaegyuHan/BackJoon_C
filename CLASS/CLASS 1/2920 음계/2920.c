#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>


int main(void)
{
    char i, j=0;
    char list[16];
    char ascending=1,
         descending=1,
         mixed=1;

    scanf("%[^\n]s", list);

    for(i=0; list[i]!=NULL; i++)
    {
        if(list[i]==' ')
            continue;

        if(descending==1 && list[i]=='8'-j)
        {
            ascending=0;
            mixed=0;
        }
        else if(ascending==1 && list[i]=='1'+j)
        {
            descending=0;
            mixed=0;
        }
        else
        {
            ascending=0;
            descending=0;
            mixed=1;
            printf("mixed");
            return 0;
        }
        j++;
    }

    if(descending==1)
        printf("descending");
    else
        printf("ascending");

    return 0;
}
