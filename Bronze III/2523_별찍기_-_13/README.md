# 2523 별찍기 - 13

URL : [https://www.acmicpc.net/problem/2523](https://www.acmicpc.net/problem/2523)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct star
{
    int number;
} Star;

void inputData(Star * S)
{
    scanf("%d", &S->number);
}

void ShowStar(Star S)
{
    int len = S.number;
    int i, j, k;

    // 위 부분
    for(i=1; i<len+1; i++)
    {   
        for(j=0; j<i; j++)
            printf("*");
        printf("\n");
    }

    // 아래 부분
    for(i=len-1; i>0; i--)
    {   
        for(j=0; j<i; j++)
            printf("*");

        if(i!=1) printf("\n");
    }
}

int main(void)
{
    Star S;
    inputData(&S);
    ShowStar(S);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main()
{
  int i, j, n, num = 1;
  scanf("%i", &n);
  for(i = 1; i < 2 * n; i++){                                                                                  
    for(j = 0; j < num; j++){                                                                                  
      printf("*");                                                                                             
    }                                                                                                          
    printf("\n");                                                                                              
    (i < n) ? num++ : num--;                                                                                   
  }                                                                                                            
}
```

```c
#include <stdio.h>
int main()
{
        int a,b=1,def,mem;
        scanf("%d",&a);
        def=a;
        if(def==1)
                printf("*");
        else
        {   
                for(;a>=b;b++)
                {   
                        mem=b;
                        for(;mem>0;mem--)
                                printf("*");
                        printf("\n");
                }   
                b=def-1;
                        for(;b>0;b--)
                        {   
                                mem=b;
                                for(;mem>0;mem--)
                                        printf("*");
                                if(b!=1)
                                        printf("\n");
                        }   
        }   

}
```