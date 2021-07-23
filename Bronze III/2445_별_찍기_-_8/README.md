# 2445 별 찍기 - 8

URL : [https://www.acmicpc.net/problem/2445](https://www.acmicpc.net/problem/2445)

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
    for(i=0; i<=(len-1); i++)
    {
        for(j=0; j<i+1; j++)
            printf("*");

        for(k=(len-i-1)*2; k>0; k--)
            printf(" ");

        for(j=0; j<i+1; j++)
            printf("*");

        printf("\n");
    }

     // 아래 부분
    for(i=(len)-2; i>=0; i--)
    {
        for(j=0; j<i+1; j++)
            printf("*");

        for(k=(len-i-1)*2; k>0; k--)
            printf(" ");

        for(j=0; j<i+1; j++)
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

void star(int n){
	int i;
	for (i=0;i<n;i++){
		printf("*");
	}
}

void space(int n){
	int i;
	for (i=0;i<n;i++){
		printf(" ");
	}
}

int main(){
	int n,k;
	scanf("%d",&n);
	for (k=1;k<=n;k++){
		star(k);
		space(2*(n-k));
		star(k);
		printf("\n");
	}
	for (k=n-1;k>0;k--){
		star(k);
		space(2*(n-k));
		star(k);
		printf("\n");
	}
}
```

```c
#include<stdio.h>
int main(){
	int i, j, n;
	scanf("%d", &n);

	for(i=1; i<n; i++){
		for(j=1; j<=2*n; j++){
			if( j<=i || j>2*n-i )
				printf("*");
			else 
				printf(" ");
		}
		printf("\n");
	}

	for(i=n; i>=1; i--){
		for(j=1; j<=2*n; j++){
			if( j<=i || j>2*n-i )
				printf("*");
			else 
				printf(" ");
		}
		if(n!=1) printf("\n");
	}
}
```