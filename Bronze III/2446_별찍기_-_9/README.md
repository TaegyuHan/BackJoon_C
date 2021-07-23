# 2446 별찍기 - 9

URL : [https://www.acmicpc.net/problem/2446](https://www.acmicpc.net/problem/2446)

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
    int len = S.number*2;
    int i, j, k;

    // 위부분
    for(i=0; i<len; i+=2)
    {
        for(j=i/2; j>0; j--)
            printf("%c", ' ');

        for(k=0; k<(len-1-i); k++)
            printf("*");

        printf("\n");
    }

    // 아래 부분
    for(i=(len-4); i>=0; i-=2)
    {
        for(j=i/2; j>0; j--)
            printf("%c", ' ');

        for(k=0; k<(len-1-i); k++)
            printf("*");

        if(i!=0) printf("\n");
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
int main(void) {
    int N;
    scanf("%d", &N);

    /*2*N-1개의 행 = 0부터 2*N까지
    ex)(N=3라고 가정) 5개의 행(0~4)
    0행 - *(2*3-1 = 5개) + 공백(0개) = 5   0행부터 < N-1행까지 역삼각형 부분
    1행 - *(2*2-1 = 3개) + 공백(1개) = 4
    2행 - *(2*1-1 = 1개) + 공백(2개) = 3   꼭짓점 부분 = N-1행
    3행 - *(2*2-1 = 3개) + 공백(1개) = 4   N+1행부터 < 2*N-1행까지 정삼각형 부분
    4행 - *(2*3-1 = 5개) + 공백(0개) = 5*/

    int part1 = N - 1;    //역삼각형+꼭짓점 부분
    int part2 = N + 1, part3 = 2 * N - 1;    //정삼각형 부분
    int starPrint = 2 * N - 1;    //5, 4, 3, 4, 5같은 대칭성의 시작 부분
    int space = 0;    //0, 1, 2, 3, 2, 1같은 대칭성 공백의 시작 부분   

    for (int i = 0; i <= part1; i++) {
        for (int j = 0; j < starPrint; j++) {
            if (j < space) printf(" ");    //j가 0, 1, 2인 동안 공백도 행마다 0, 1, 2개
            else printf("*");
        }
        printf("\n");
        starPrint--;
        space++;
    }

    starPrint+=2;
    space -= 2;

    for (int i = part2; i <= part3; i++) {
        for (int j = 0; j < starPrint; j++) {
            if (j < space) printf(" ");
            else printf("*");
        }
        printf("\n");
        starPrint++;
        space--;
    }
    return 0;
}
```

```c
#include <stdio.h>

int main(void) {
    int input, highest;

    scanf("%d", &input);

    if (scanf)

    highest = input*2-1;

    for (int i=input; i>0; i--) {
        if (highest - i*2-1 >= 0) {
            int empty = highest - ((i*2)-1);
            int start = 0;

            while (start < empty/2) {
                printf(" ");
                start++;
            }

            for (int j=i*2-1; j>0; j--) {
                printf("*");
            }

            
        }

        else {
                for (int j=i*2-1; j>0; j--) {

                printf("*");

            } 
        }    
        printf("\n");
    }

    //Reverse print
    for (int i=2; i<input+1; i++) {
        if (highest - i*2-1 >= 0) {
            int empty = highest - ((i*2)-1);
            int start = 0;

            while (start < empty/2) {
                printf(" ");
                start++;
            }

            for (int j=0; j<i*2-1; j++) {
                printf("*");
            }

    
        }

        else {
                for (int j=0; j<i*2-1; j++) {
                printf("*");
            } 
        }  
        printf("\n");
    }
}
```

```c
#include <stdio.h>

int main(){
        int num;
        scanf("%d",&num);

        for(int i = 0; i< num; i++){
                for (int j = 0; j <num; j++){
                        if(j >= i){
                                printf("*");
                        }else{
                                printf(" ");
                        }
                }

                for (int j = num-1; j > i; j--){
                        printf("*");
                }
                printf("\n");
        }

        for(int i = 0; i < num-1; i++){
                for (int j = num-1; j > 0; j--){
                        if(j-1 > i){
                                printf(" ");
                        }else{
                                printf("*");
                        }
                }

                for (int j = 0 ;j < i+2; j++){
                        printf("*");
                }
                printf("\n");
        }

        return 0;
}
```