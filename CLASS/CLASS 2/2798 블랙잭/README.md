# 2798 블랙잭

URL : [https://www.acmicpc.net/problem/2798](https://www.acmicpc.net/problem/2798)

```c
#include <stdio.h>

#define MAX_CARD_COUNT 101

// DATA -------------------------------------- * 

int DATA_COUNT; // (3 ≤ N ≤ 100)
int MAX_POINT; // (10 ≤ M ≤ 300,000)

int CardList[MAX_CARD_COUNT]; // 카드 배열
int temp[MAX_CARD_COUNT]; // 카드 배열

// DATA END ---------------------------------- *

void InputIntData(int* n)
{
    scanf("%d", n);
}

void TreeCardSelect()
{
    int i, j, k;
    int sum;
    int result = 0;

    for (i = 0; i < DATA_COUNT; i++)
    {
        for (j = i + 1; j < DATA_COUNT; j++)
        {
            for (k = j + 1; k < DATA_COUNT; k++)
            {
                sum = CardList[i] +
                      CardList[j] +
                      CardList[k];
                if (sum <= MAX_POINT && sum > result)
                    result = sum;
            }
        }
    }

    printf("%d\n", result);
}

int main()
{
    int i;

    // 데이터 입력
    InputIntData(&DATA_COUNT);
    InputIntData(&MAX_POINT);
    for (i = 0; i < DATA_COUNT; i++)
    {
        InputIntData(&CardList[i]);
    }

    // M을 넘지 않으면서 M에 최대한 가까운 
    // 카드 3장의 합
    TreeCardSelect();

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>
int blackjack(int a, int b, int c, int max){
    int sum=a+b+c;
    if (sum<max) return sum;
    else if (sum==max) return -1;
    else return 0;
}
int main(void){
    int n;
    int max;
    scanf("%d %d",&n, &max);
    int *num=(int*)malloc(sizeof(int)*n);
    for (int i=0;i<n;i++) scanf("%d", &num[i]);
    int jack=0;
    int pre_sum=0;
    while (jack==0){
        for (int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                for(int k=j+1;k<n;k++){
                    int sum=blackjack(num[i],num[j],num[k],max);
                    if (sum==-1) {jack=1; pre_sum=max;}
                    else if (sum>pre_sum) pre_sum=sum;
                }
            }
        }
        jack=1;
    }
    printf("%d",pre_sum);
    free(num);
}
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int m, n, sum=0, num[100];

int main()
{
   int i, j, k, l;
   scanf("%d %d", &n, &m);
   for(i=0;i<n;i++)
   {
       scanf("%d", &num[i]);
   }
   for(i=0; i<n; i++)
   {
       for(j=i+1; j<n; j++)
       {
           for(k=j+1; k<n; k++)
           {
               l=num[i]+num[j]+num[k];
               if(l==m)
               {
                   sum=l;
               }
               else if(l<m)
               {
                   if(l>sum)
                   {
                       sum=l;
                   }
               }
           }
       }
   }
   if(n==3)
   {
       sum=num[0]+num[1]+num[2];
   }
   printf("%d", sum);
   return 0;
}
```