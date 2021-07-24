# 1009 분산처리

URL : [https://www.acmicpc.net/problem/1009](https://www.acmicpc.net/problem/1009)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
int TestCount;

typedef struct test
{
    int a; //  (1 ≤ a < 100)
    int b; //  (1 ≤ b < 1,000,000)
    int pattern[10];
    int patternLen;
} Test;

void inputData(Test * T)
{
    scanf("%d %d", 
            &T->a,
            &T->b );
}

void findPattern(Test * T)
{
    int i = 1;
    int fristNum = T->a,
        fristCheck = T->a%10;
    int lastNum = T->a;
    T->pattern[0] = fristNum;

    do
    {
        lastNum = (fristNum * lastNum)%10;
        T->pattern[i] = lastNum;
        i++;
    }
    while(fristCheck!=lastNum);

    T->patternLen = --i;
}

void findTestComputer(Test T)
{
    int i;
    int index,
        len = T.patternLen,
        mulCont = T.b;

    // 자신의 수 계속 나오는 상황 
    if (len==1) 
    { 
        if(T.a%10==0) { printf("10\n"); return; }
 
        printf("%d\n", T.a%10); return; 
    }

    // 다른 상황
    index = (mulCont%len==0) ? (len-1) : (mulCont%len-1);
    printf("%d\n", T.pattern[index]%10);
}

int main(void)
{
    int i;
    Test T;
    scanf("%d", &TestCount);

    for(i=0; i<TestCount; i++)
    {   
        inputData(&T);
        findPattern(&T);
        findTestComputer(T);
    }

    return 0;
}
```

숏코딩

```c
#include <stdio.h>

int main(void)
{
    int t, i, a, b, r;
    int div_a, div_b;

    scanf("%d", &t);

    while( t-- )
    {
        scanf("%d %d", &a, &b);

        div_a = a%10;

        switch( div_a )
        {
            case 0:
                printf("10\n");
                break;
            case 1:
            case 5:
            case 6:
                printf("%d\n", div_a);
                break;
            case 9: 
                if( b % 2 == 0 )
                    printf("1\n");
                else
                    printf("9\n");
                break;
            default:
                div_b = b % 4;
                if( div_b == 0 )
                    div_b = 4;

                for( i = 1, r = a; i < div_b; i++ )
                    r = r*a;
                printf("%d\n", r % 10);
                break;
        }
    }

    return 0;
}
```

```c
#include <stdio.h>
#include <math.h>

int main (void)
{
   int a,b;
   int n;
   int i;
   int s;
   int c;
   int result[10000];

   scanf("%d", &n);
   
   
   for(i=0; i<n; i++)
   {
      result[i] = 1;
      scanf("%d %d", &a, &b);

      for(s = 0; s < b; s++)
      {
         result[i] = (result[i]*a)%10;
      }

   }

   for(i = 0; i < n; i++)
   {
      if(result[i] == 0)
      {
         printf("10\n");
      }
      
      else
      {
         printf("%d\n", result[i]);
      }
   }

   return 0;
}
```