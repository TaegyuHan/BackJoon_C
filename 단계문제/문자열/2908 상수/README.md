# 2908 상수

URL : [https://www.acmicpc.net/problem/2908](https://www.acmicpc.net/problem/2908)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, j;
    char numArray[2][4];

    scanf("%s %s", numArray[1], numArray[2]); // 입력 받기

    for(i=3; i>=0; i--)
    {   
        // 크다면?
        if(numArray[1][i] > numArray[2][i])
        {
            j=1; // 첫번째 수 선택
            break;
        }
        // 작다면?
        if(numArray[1][i] < numArray[2][i])
        {
            j=2; // 두번째 수 선택
            break;
        }
        // 같다면
        if(numArray[1][i] = numArray[2][i])
        {   // 계속 진행
            continue;
        }
    }

    // 반대로 출력
    for(i=2; i>=0; i--)
        printf("%c", numArray[j][i]);

    return 0;
}
```

<br>

숏코딩

```c
main(a,b){scanf("%d%d",&a,&b);a+=99*(a%10-a/100);b+=99*(b%10-b/100);printf("%d",a>b?a:b);}
```

```c
// 숫자 뒤집는 함수 제작
int rev(int a) {return (a % 10) * 100 + (a / 10) % 10 * 10 + a / 100;}

int main() {
	int a, b;
	scanf("%d %d", &a, &b);
	a = rev(a), b = rev(b);
	printf("%d\n", (a > b) ? a : b);
}
```

```c
#include<stdio.h>
int main(void)
{
    int a;
    int b;
    scanf("%d %d", &a,&b);
    
    a = ((a%10)*100)+((a%100)/10*10)+(a/100);
    b = ((b%10)*100)+((b%100)/10*10)+(b/100);
    
    printf("%d\n",a>b? a:b);
    
    return 0;
}
```