# 1193 분수찾기

URL : [https://www.acmicpc.net/problem/1193](https://www.acmicpc.net/problem/1193)

```c
#include <stdio.h>

void DownShowArry(int i, int cnt)
{
    int j;
    for (j=i-1; j>0; j--)
    {   
        if((i-j)==cnt)
            printf("%d/%d\n", j, i-j);
    }
}

void UpShowArry(int i, int cnt)
{
    int j=1;
    for (j=i-1; j>0; j--)
    {
        if((i-j)==cnt)
            printf("%d/%d\n", i-j, j);
    }
}

int main(void)
{
    int i=0, j;
    int InputNum, Sum=0,
        temp;

    scanf("%d", &InputNum);

    for (i; Sum<InputNum; i++)
    {
        Sum += i;
    }

    // 그 행에서의 번째
    temp = InputNum-(Sum-(i-1));

    if(i%2==1)
        UpShowArry(i, temp);
    else
        DownShowArry(i, temp);

    return 0;
}
```