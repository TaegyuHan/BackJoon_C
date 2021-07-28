# 2506 점수계산

URL : [https://www.acmicpc.net/problem/2506](https://www.acmicpc.net/problem/2506)

```c
#include <stdio.h>

typedef struct _Point
{
	int problemNum; //  N (1 ≤ N ≤ 100)
	int answerPoint; // 
	int OX; // 0 or 1

} Point;

void InputDataProblemNum(Point* Point)
{
	scanf("%d", &Point->problemNum);
}

void InputDataOX(Point* Point)
{
	scanf("%d", &Point->OX);
}

int CheckOX(Point* Point)
{
	int result;
	if (Point->OX == 1)
	{
		result = Point->answerPoint;
		(Point->answerPoint)++;
	}
	else
	{
		result = 0;
		Point->answerPoint = 1;
	}
	return result;
}

int main(void) 
{

	int i;
	int sumPoint = 0;
	Point Point = {0, 1, 0};

	InputDataProblemNum(&Point);

	for (i = 0; i < Point.problemNum; i++)
	{
		InputDataOX(&Point);
		sumPoint += CheckOX(&Point);
	}

	printf("%d", sumPoint);

	return 0;
}
```

숏 코딩

```c
#include<stdio.h>

int main(void)
{
	int n, i;
	int sum = 0;
	int check = 0; //연속해서 1인지 확인
	int add = 1;
	int score[100] = { 0 };

	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		scanf("%d", &score[i]);
		if (score[i] == 1)
		{
			if (check == 1) //check가 1이면
				add += 1; //추가로 1을 더함
			sum += add; //점수계산
			check = 1;
		}
		else
		{
			check = 0; //check를 0으로 초기화
			add = 1; //더하는 점수를 1로 초기화
		}
	}
	printf("%d", sum);
	return 0;
}
```

```c
#include <stdio.h>

int main()
{
    int num;
    scanf("%d",&num);
    int a[num];
    int i;
    int grade[num];
    int status=0;
    int total=0;
    for(i=0;i<num;i++){
        scanf("%d",&a[i]);
    }
    for(i=0;i<num;i++){
        if(a[i]==0){
            grade[i]=0;
            status=0;
        }
        else{
            grade[i]=1+status;
            status++;
        }
    }
    for(i=0;i<num;i++){
        total=total+grade[i];
    }
    printf("%d",total);
    return 0;
}
```