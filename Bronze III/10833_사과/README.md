# 10833 사과

URL : [https://www.acmicpc.net/problem/10833](https://www.acmicpc.net/problem/10833)

```c
#include <stdio.h>

#define CUP_NUM 3

typedef struct _School
{
	int SchoolNum; // N (1 ≤ N ≤ 100)
	int ManNum;
	int AppleNum;
} School;

void InputDataSchoolNum(School* School)
{
	scanf("%d", &School->SchoolNum);
}

void InputDataManApple(School* School)
{
	scanf("%d %d",
		&School->ManNum,
		&School->AppleNum );
}

int splitAppleRemainder(School * School)
{
	return School->AppleNum % School->ManNum;
}

int main(void) {

	int i;
	int RemainApple = 0;

	School School;
	InputDataSchoolNum(&School);

	for (i = 0; i < School.SchoolNum; i++)
	{
		InputDataManApple(&School);
		RemainApple += splitAppleRemainder(&School);
	}

	printf("%d", RemainApple);

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N;
	int studentn[100];
	int applen[100];
	scanf("%d",&N);

	int i;
	for (i = 0; i < N; i++)
	{
		scanf("%d%d",&studentn[i],&applen[i]);
	}

	int total = 0;
	
	for (i = 0; i < N; i++)
	{
		total += (applen[i] % studentn[i]);
	}

	printf("%d",total);

	return 0;
}
```

```c
#include<stdio.h>

int main() {
    int n;
    scanf("%d",&n);
    
    int student,apple;
    int totalRemainApples = 0;
    
    for(int i = 0 ; i < n ; i++){
        scanf("%d%d",&student,&apple);
        
        totalRemainApples += apple%student; 
    }
    printf("%d",totalRemainApples);
}
```