# 5532 방학 숙제

URL : [https://www.acmicpc.net/problem/5532](https://www.acmicpc.net/problem/5532)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct homeWork
{   
    int vacationDay;// 2 ≤ day ≤ 40
    int math;       // 1 ≤ math ≤ 1000
    int korean;     // 1 ≤ korean ≤ 1000
    int mathSolve;  // 1 ≤ mathSolve ≤ 100
    int korSolve;   // 1 ≤ korSolve ≤ 100
} HomeWork;

int main(void)
{
    int mathCompleteDay;
    int korCompleteDay;
    int CompletionDay;

    HomeWork HW;

    scanf("%d %d %d %d %d",
            &HW.vacationDay, 
            &HW.math, 
            &HW.korean,
            &HW.mathSolve,
            &HW.korSolve );

    mathCompleteDay = (HW.math%HW.mathSolve==0) ? 
                        (HW.math/HW.mathSolve) : ((HW.math/HW.mathSolve) + 1);

    korCompleteDay = (HW.korean%HW.korSolve==0) ? 
                        (HW.korean/HW.korSolve) : ((HW.korean/HW.korSolve) + 1);

    CompletionDay = (mathCompleteDay > korCompleteDay) ?
                        mathCompleteDay : korCompleteDay;

    printf("%d ", HW.vacationDay - CompletionDay);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int vacation(int L, int A, int B, int C, int D) {
 
    int day_math, day_lan;
 
    if ((A%C) != 0) {
 
        day_lan = A / C + 1;
 
    }
 
    else day_lan = A / C;
 
    if ((B%D) != 0) {
 
        day_math = B / D + 1;
    }
    else day_math = B / D;
 
    return (day_lan > day_math) ? L - day_lan : L - day_math;
}

int main(){
 
    int L, A, B, C, D;
 
    scanf("%d\n", &L);
    scanf("%d\n", &A);
    scanf("%d\n", &B);
    scanf("%d\n", &C);
    scanf("%d", &D);
    printf("%d\n", vacation(L, A, B, C, D)); // Q2
 
    return 0;
}
```