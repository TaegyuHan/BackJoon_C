# 17388 와글와글 숭고한

URL : [https://www.acmicpc.net/problem/17388](https://www.acmicpc.net/problem/17388)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct univ
{
    int point;
} Univ;

typedef struct univList
{
    Univ Soongsil;
    Univ Korea;
    Univ Hanyang;
} UnivList;

void inputData(UnivList * UL)
{
    scanf("%d %d %d", 
            &UL->Soongsil.point,
            &UL->Korea.point,
            &UL->Hanyang.point );

    return;
}

void CheckParticipation(UnivList * UL)
{
    int minimum = 100;
    int sumPoint = UL->Soongsil.point + 
                   UL->Korea.point + 
                   UL->Hanyang.point;

    if(sumPoint >= minimum)
        printf("OK");
    else
    {
        (UL->Soongsil.point > UL->Korea.point) ?  
        ((UL->Korea.point > UL->Hanyang.point) ? printf("Hanyang") : printf("Korea")) :
        ((UL->Soongsil.point > UL->Hanyang.point) ? printf("Hanyang") : printf("Soongsil"));
    }
    
    return;
}

int main(void)
{
    UnivList UL;

    inputData(&UL);
    CheckParticipation(&UL);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(void) {
    int a, b, c; scanf("%d%d%d", &a, &b, &c);

    if (a + b + c >= 100) {
        puts("OK");
        return 0;
    } else if ((a + b + c < 100) && (a < b) && (a < c)) {
        puts("Soongsil");
        return 0;
    } else if ((a + b + c < 100) && (b < a) && (b < c)) {
        puts("Korea");
        return 0;
    } else if ((a + b + c < 100) && (c < a) && (c < b)) {
        puts("Hanyang");
        return 0;
    }
}
```

```c
#include <stdio.h>
#include <string.h>

int main() {

	int s = 0;
	int k = 0;
	int h = 0;
	scanf("%d %d %d", &s, &k, &h);
	int sum = 0;
	sum = s + k + h;
	if (sum >= 100) {
		printf("OK");
	}
	else {
		if (s < h && s < k) {
			printf("Soongsil");
		}
		if (h < s&&h < k) {
			printf("Hanyang");
		}
		if (k < s&&k < h) {
			printf("Korea");
		}
	}

	return 0;
}
```