#include <stdio.h>

int main(void)
{
    unsigned int i=0;
    unsigned int CheckNum, sum=1;
    scanf("%d", &CheckNum);

    do
    {   // 6개씩 벌집이 늘어남
        sum += 6*i;
        i++;
    }
    while(sum < CheckNum);

    printf("%d", i);

    return 0;
}