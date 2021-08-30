# 1676 팩토리얼 0의 개수

URL : [https://www.acmicpc.net/problem/1676](https://www.acmicpc.net/problem/1676)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Data
{
    int fiveCount;
    int twoCount;
    int factorialNum;
} Data;

void inputIntData(int* num) { scanf("%d", num); return; }

int checkFive(int num) { return (num % 5 == 0) ? 1 : 0; }
int checkTwo(int num) { return (num % 2 == 0) ? 1 : 0; }

void PrimeFactorization(Data* D, int num)
{
    int i;
    for (i = 2; i <= num; i++)
    {
        if (num % i == 0)
        {
            // 2또는 5이면 개수 1 증가
            D->fiveCount += checkFive(i);
            D->twoCount += checkTwo(i);

            num = num / i;
            i = 1;
        }
    }
    
    return;
}

int main()
{
    Data* D = (Data*)malloc(sizeof(Data));
    memset(D, 0, sizeof(Data));
    int i;
    int result;

    inputIntData(&(D->factorialNum));

    for (i = D->factorialNum; i > 0; i--)
        PrimeFactorization(D, i);

    result = (D->fiveCount > D->twoCount) ?
                D->twoCount : D->fiveCount;

    printf("%d", result);

    return 0;
}
```

소인수 분해

[https://desire-with-passion.tistory.com/67](https://desire-with-passion.tistory.com/67)

```c
#include <stdio.h>

int main()

{

	int i, n;

	printf("소인수분해 하고싶은 수를 입력하세요 \n");

	scanf("%d", &n);

	printf("%d 를 입력하셨습니다. \n", n);

	printf("%d = ", n);

	for (i = 2; i <= n; i++)

	{

		if (n % i == 0)

		{

			printf("%d ", i);

			n = n / i;

			if (n % i == 0)

			{

				printf("* ");

			}

			else if (n % i != 0)

			{

				if (n > i)

					printf("* ");

			}

			i = 1;

		}

	}

	printf("\n");

	return 0;

}
```

숏 코딩

```c
#include <stdio.h>

int check_Two(int num) {
    
    int now_Num = num;
    int how_Many = 0;
    
    for ( ; ;how_Many++) {
        
        if (now_Num % 2 == 0) {
            
            now_Num /= 2;
        }
        else {break;}
        
    }
    
    
    return how_Many;
}

int check_Five(int num) {
    
    int now_Num = num;
    int how_Many = 0;
    
    for ( ; ;how_Many++) {
        
        if (now_Num % 5 == 0) {
            
            now_Num /= 5;
        }
        else {break;}
        
    }
    
    
    return how_Many;
}

int main() {
    
    int N;
    int array_Two_Five[2] ={0,0};
    
    scanf("%d", &N);
    
    for (int i = 1; i <= N ;i++) {
            
        array_Two_Five[0] += check_Two(i);
        array_Two_Five[1] += check_Five(i);
    }
    
    if (array_Two_Five[0] >= array_Two_Five[1]) {printf("%d", array_Two_Five[1]);}
    else {printf("%d", array_Two_Five[0]);}

    return 0;
}
```

```c
#include <stdio.h>

#define MIN2(a,b)       ((a) < (b) ? (a) : (b))

int main()
{
        int two = 0, five = 0;
        int i, j, n;

        scanf("%d", &n);

        for (i = 2; i <= n; i++) {
                j = i;
                while (j % 2 == 0) {
                        j /= 2;
                        two++;
                }
                while (j % 5 == 0) {
                        j /= 5;
                        five++;
                }
        }

        printf("%d\n", MIN2(five, two));

        return 0;
}
```

```c
#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    unsigned long long factorial = 1;
    int cnt = 0;
    for (int i = 1; i <= num;i++)
    {
        factorial = factorial * i;
        while(factorial % 10 == 0)
        {
            factorial = factorial / 10;
            cnt++;
        }
        unsigned long long temp = factorial;
        temp = temp / 1000;
        temp = temp * 1000;
        factorial = factorial - temp;
    }
    printf("%d", cnt);
    return 0;
}
```

```c
#include<stdio.h>
int count2=0,count5 = 0;
void over_watch(int n) {
	if (n % 5 == 0) {
		count5++;
		n /= 5;
		over_watch(n);
	}
}
void over_sasquatch(int n) {
	if (n % 2 == 0) {
		count2++;
		n /= 2;
		over_sasquatch(n);
	}
}

int main(void) {
	int N,i,count=0;
	
	scanf("%d", &N);

	for (i = 1; i <= N; i++) {
		over_sasquatch(i);
		over_watch(i);
	}
	count = count2 >= count5 ? count5 : count2;
	printf("%d", count);
}
```