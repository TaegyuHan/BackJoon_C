# 2443 별찍기 - 6

URL : [https://www.acmicpc.net/problem/2443](https://www.acmicpc.net/problem/2443)

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

void star(int n)
{
    for(int i=0; i<n; i++)
        printf("*");
}

void space(int n)
{
    for(int i=0; i<n; i++)
        printf(" ");
}

void ShowStar(Star S)
{
    int len = S.number*2;
    int i;
    int starNum = len-1,
        spaceNum = 0;

    for(i=1; i<=S.number; i++)
    {
        space(spaceNum);
        star(starNum);

        starNum-=2;
        spaceNum++;

        if(i!=S.number) printf("\n");
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

int main(){
    
    int a= 0;
    int b= 1;
	int i = 0;
    scanf("%d",&a);
    if((a>=0) && (a<=100)){
       for(a;b<=a;){
           for(i=0;i<b-1;i++){
                printf(" ");
            }
           
		   for(i=0;i<2*(a-b+1)-1;i++){
			   printf("*");
		   }
		   b++;
           printf("\n");
       }
        
    }else{
        return 0;
    }
    return 0;
}
```

```c
void blank(int n){
    for(int i=1; i<=n; i++){
        printf(" ");
    }
}

void starr(int n){
    for(int i=1; i<=n; i++){
        printf("*");
    }
}

void star(int n){
    for(int i=1; i<=n; i++){
        blank(i-1);
        starr(2*n - 2*i + 1);
        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d" , &n);
    star(n);
}
```