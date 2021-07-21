# 15963 CASIO

URL : [https://www.acmicpc.net/problem/15963](https://www.acmicpc.net/problem/15963)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct battery
{   
    int songChan;   // 10자리 정수
    int teacher;    // 10자리 정수
} Battery;

int main(void)
{
    Battery B;

    scanf("%d %d", &B.songChan, &B.teacher);
    
    (B.songChan==B.teacher) ? printf("1") : printf("0");

    return 0;
}
```

숏 코딩

```c
int main()
{
    int a,b;
    scanf("%d %d", &a,&b);
    if(a==b){
        printf("1");
    }
    else{
        printf("0");
    }
    return 0;
}
```

```c
#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N,&M);
    if(N==M) {
        printf("1");
        return 0;
    }
    
    printf("0");
    
    return 0;
}
```