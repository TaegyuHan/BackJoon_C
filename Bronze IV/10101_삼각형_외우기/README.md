# 10101 삼각형 외우기

URL : [https://www.acmicpc.net/problem/10101](https://www.acmicpc.net/problem/10101)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct triangle
{   
    int angleA;  // 0 <= angleA <= 180 
    int angleB;  // 0 <= angleB <= 180
    int angleC;  // 0 <= angleC <= 180
} Triangle;

int main(void)
{
    Triangle TR;
    int angleSum;

    scanf("%d %d %d",
            &TR.angleA,
            &TR.angleB,
            &TR.angleC );

    angleSum = TR.angleA + TR.angleB + TR.angleC;

    // 세각의 크기가 60
    if( TR.angleA==60 &&
        TR.angleB==60 && 
        TR.angleC==60 )
    {
        printf("Equilateral");
    } // 180 각이 아닌 경우
    else if (angleSum!=180)
    {
        printf("Error");
    } // 합이 180각이면서 두각이 같은경우
    else if ( TR.angleA==TR.angleB ||
              TR.angleA==TR.angleC ||
              TR.angleC==TR.angleB )
    {   
        printf("Isosceles");
    } // 합이 180각이면서 같은 각이 없는 경우
    else
    {
        printf("Scalene");
    }

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main()
{
	int a,b,c;
	int sum;
	scanf("%d %d %d",&a,&b,&c);
	sum=a+b+c;
	
	if(sum!=180) printf("Error");
	else {
		if(a==b && b==c) printf("Equilateral");
		else if(a!=b && b!=c && a!=c) printf("Scalene");
		else printf("Isosceles");
	}
		
	return 0; 
}
```

```c
#include <stdio.h>
int main() {
	int a, b, c;
	scanf("%d\n %d\n %d", &a, &b, &c);
	if (a + b + c == 180)
		if (a == 60 && b == 60 && c == 60) printf("Equilateral");
		else if (a == b || a == c || b == c) printf("Isosceles");
		else
			printf("Scalene");
	else printf("Error");

}
```

```c
#include <stdio.h>

int main(void)
{
	int a, b, c;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	if (a == b && b == c) printf("Equilateral");
	else if (a + b + c == 180)
	{
		if (a == b || b == c || a == c) printf("Isosceles");
		else printf("Scalene");
	}
	else printf("Error");
	
	return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);
	if(a==60&&b==60&&c==60){
		printf("Equilateral");
	}
	else if(a+b+c==180){
		if(a==b||b==c||c==a){
			printf("Isosceles");
		}
		else{
			printf("Scalene");
		}
	}
	else{
		printf("Error");
	}
	return 0;
}
```