# 10162 전자레인지

URL : [https://www.acmicpc.net/problem/10162](https://www.acmicpc.net/problem/10162)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

struct numberList
{
    int A;
    int B;
    int C;
};

int main(void)
{
    int i;
    int InputTime;
    int cntA, cntB, cntC;
    int Possible;

    struct numberList numberList = {
        300, //A
        60,  //B
        10   //C
    };

    scanf("%d", &InputTime);

    cntA = InputTime/numberList.A;
    cntB = (InputTime - (cntA*numberList.A))/numberList.B;
    cntC = (InputTime - (cntA*numberList.A) - (cntB*numberList.B))/numberList.C;
    Possible = (InputTime - (cntA*numberList.A) - (cntB*numberList.B))%numberList.C;

    if(!Possible)
        printf("%d %d %d", cntA, cntB, cntC);
    else
        printf("-1");

	return 0;
}
```

숏 코드

```c
#include <stdio.h>

int main(){
    int T;
    scanf("%d",&T);
    
    int A = 300, B = 60, C = 10;
    
    if(T%C !=0) printf("%d",C-11);
    else printf("%d %d %d",T/A,T%A/B,T%A%B/C);
    return 0;
}
```

```c
#include <stdio.h>

int main()
{
	int t, m_ = 300, m = 60, s = 10, a, b, c;

	scanf("%d", &t);
	a = t / m_;
	t -= a*m_;
	b = t / m;
	t -= b*m;
	c = t / s;
	t -= c*s;
	if (t != 0) printf("-1\n");
	else printf("%d %d %d\n", a, b, c);
}
```

```c
#include <stdio.h>
int main()
{
	int T;
	int A = 300;
	int B = 60;
	int C = 10;

	scanf("%d", &T);
	if (T % 10 == 0)
	{
		printf("%d %d %d", T / A, (T%A) / B, (T%B) / 10);
	}
	if (T % 10 != 0)
	{
		printf("%d", -1);
	}
	return 0;
}
```