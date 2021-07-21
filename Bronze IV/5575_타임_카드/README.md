# 5575 타임 카드

URL : [https://www.acmicpc.net/problem/5575](https://www.acmicpc.net/problem/5575)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct time
{   
    int hour;   // (7 ≦ h ≦ 22)
    int minute; // (0 ≦ m ≦ 59)
    int second; // (0 ≦ s ≦ 59)
    int secondSum;
} Time;

typedef struct start { Time Time; } Start;
typedef struct end { Time Time; } End;

void InputData(Start * S, End * E)
{
    int i;

    // 데이터 받기
    for(i=0; i<3; i++)
    {
        scanf("%d %d %d", 
                &(S + i)->Time.hour, 
                &(S + i)->Time.minute, 
                &(S + i)->Time.second);

        (S + i)->Time.secondSum = (S + i)->Time.hour*3600 + 
                                  (S + i)->Time.minute*60 + 
                                  (S + i)->Time.second;

        scanf("%d %d %d", 
                &(E + i)->Time.hour, 
                &(E + i)->Time.minute, 
                &(E + i)->Time.second);

        (E + i)->Time.secondSum = (E + i)->Time.hour*3600 + 
                                  (E + i)->Time.minute*60 + 
                                  (E + i)->Time.second;

    }
}

void ShowDiffTime(Start * S, End * E)
{
    int i;
    int workTime;

    // 데이터 받기
    for(i=0; i<3; i++)
    {
        workTime = (E + i)->Time.secondSum - (S + i)->Time.secondSum;
        printf("%d %d %d\n",
            (workTime/3600)%24,
            (workTime%3600)/60,
            (workTime%60)
        );
    }
}

int main(void)
{
    int i;
    Start S[3];
    End E[3];

    InputData(S, E);
    ShowDiffTime(S, E);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(){
    int h1,m1,s1,h2,m2,s2;
    int seconds,minutes,hours;

    for(int i = 0; i < 3; i++){
        scanf("%d%d%d%d%d%d", &h1,&m1,&s1,&h2,&m2,&s2);
        if(s1 > s2){
            m2--;
            seconds = 60 - (s1-s2);
        }
        else{
            seconds = s2-s1;
        }

        if(m1 > m2){
            h2--;
            minutes = 60 - (m1-m2);
        }
        else{
            minutes = m2-m1;
        }

        hours = h2-h1;

        printf("%d %d %d\n", hours, minutes, seconds);
    }
    
}
```

```c
#include <stdio.h>
int main(void)
{

    int h, m , s;
    int H, M, S;
    int total;
    for(int i=0;i<3; i++){

        scanf("%d %d %d %d %d %d", &h, &m, &s, &H, &M, &S);
        getchar();
        total = (H-h)*3600 + (M-m)*60 +(S-s);
        printf("%d", total/3600);
        printf(" %d", (total/60)%60);
        printf(" %d\n", (total)%60);

    }

    return 0;
}
```

```c
#include <stdio.h>
int main() {
    int i;
    for (i = 3; i--; ) {
        int H, M, S, h, m, s;
        scanf("%d%d%d%d%d%d", &H, &M, &S, &h, &m, &s);
        s -= S;
        if (s < 0) {
            s += 60;
            --m;
        }
        m -= M;
        if (m < 0) {
            m += 60;
            --h;
        }
        h -= H;
        printf("%d %d %d\n", h, m, s);
    }
}
```