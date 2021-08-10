# 2839 설탕배달

URL : [https://www.acmicpc.net/problem/2839](https://www.acmicpc.net/problem/2839)

```c
#include <stdio.h>

#define KILOGRAM_5 5
#define KILOGRAM_3 3

int INPUT_INT;

void InputIntData()
{
	scanf("%d", &INPUT_INT);
}

void FindCount( int quotient_5, int remainder_5,
								int quotient_3, int remainder_3 )
{
	// 나머지 없음 성공
	if (remainder_3 == 0)
	{
		printf("%d", quotient_3 + quotient_5);
		return;
	}

	// N킬로그램 제작 불가
	if (quotient_5 == 0 && remainder_3 != 0)
	{
		printf("-1");
		return;
	}

	// N킬로그램 제작 불가
	if (quotient_5 != 0 && remainder_3 != 0)
	{
		FindCount( quotient_5 - 1,
						   remainder_5 + KILOGRAM_5,
						   (remainder_5 + KILOGRAM_5) / KILOGRAM_3,
						   (remainder_5 + KILOGRAM_5) % KILOGRAM_3 );
		return;
	}
}

int main(void)
{
	InputIntData();

	int quotient_5 = INPUT_INT / KILOGRAM_5;
	int remainder_5 = INPUT_INT % KILOGRAM_5;

	int quotient_3 = remainder_5 / KILOGRAM_3;
	int remainder_3 = remainder_5 % KILOGRAM_3;
	
	FindCount(quotient_5, remainder_5, quotient_3, remainder_3);

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main()
{
    /* code */

    int in, five, three; //input, output(min), temp

    scanf("%d", &in); // 설탕 무게 받아오기

    // min = in; // min 초기화

    /*
        1. 최대한 5키로에 담는다.
        2. 남는게 3 이하면, 5키로짜리 하나를 없앤다.
        3. 3키로에 모두 담는다.
    */

   five = in / 5; // 5키로 짜리
   in %= 5;       // 나머지 설탕

   while(five >= 0){        // 5키로에 0보다 크면
       if(!(in % 3)){       // 나머지가 3키로에 담을 수 없다면
           three = in / 3;  // 3키로에 담는다 
           in %= 3;         // in = (in%5)%3  3키로에 담고 남은 나머지를 저장
           break;           // while문을 빠져 나온다
       }
       five--;              // 5키로 하나를 버린다
       in += 5;             // 나머지에 5키로를 더한다.
   }

    printf("%d", in == 0? five+three : -1); // 출력

    return 0;
}
```

```c
#include <stdio.h>
int N3[5] = {0,2,4,1,3};
int main(void)
{
    int n, k;
    scanf("%d",&k);
    n = N3[k%5];
    k = k<n*3?-1:(k-n*3)/5+n;
    printf("%d\n", k);
    return 0;
}
```