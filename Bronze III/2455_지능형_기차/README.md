# 2455 지능형 기차

URL : [https://www.acmicpc.net/problem/2455](https://www.acmicpc.net/problem/2455)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

#define STATION 4
#define IN(X, Y) ((X) + (Y))
#define OUT(X, Y) ((X) - (Y))
#define CHECK(X, Y) ((X > Y) ? X : Y)

typedef struct train
{
    int in;
    int out;
    int people;
} Train;

void inputData(Train * T)
{
    scanf("%d %d",
            &T->out, 
            &T->in );
}

void arrival(Train * T)
{
    T->people = OUT(T->people, T->out);
    T->people = IN(T->people, T->in);
}

int main(void)
{
    int i;
    int result=0;
    Train T;
    T.people = 0;

    for(i=0; i<STATION; i++)
    {
        inputData(&T);
        arrival(&T);
        result = CHECK(result, T.people);
    }

    printf("%d", result);

    return 0;
}
```

숏코딩

```c
int stopTrain(int from, int to, int *countOut, int *countIn, int *countStay);

int main(void) {
	
	int countOut;
	int countIn;

	int countCurrent = 0;
	int countMax = 0;
	
	int i;
 	for(i = 0; i < 4; i++) {
		do {
			scanf("%d %d", &countOut, &countIn);
		} while (!(countOut >= 0 && countOut <= 10000
		        && countIn  >= 0 && countIn  <= 10000));

		countCurrent = countCurrent - countOut + countIn;
		if(countCurrent > countMax) {
		 	countMax = countCurrent;
		}
	} 
	
	printf("%d", countMax);
 
	return 0;
}
```

```c
void DescendingOrder(int arr[], int size)
{
	for (int i = 0; i < size - 1; i++)
	{
		for (int j = 0; j < size - 1 - i; j++)
		{
			if (arr[j] < arr[j + 1])
			{
				int temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}
int main()
{
	int Train_Members[STATION_COUNT] = { 0, };
	int current_members = 0;
	int get_on;
	int get_off;

	for (int i = 0; i < STATION_COUNT; i++)
	{
		scanf("%d %d", &get_off, &get_on);
		current_members -= get_off;
		current_members += get_on;
		Train_Members[i] = current_members;
	}

	DescendingOrder(Train_Members, STATION_COUNT);

	printf("%d\n", Train_Members[0]);

	return 0;
}
```

```c
main()
{
	int ppl = 0;
	int jo = 0;
	int ot = 0;
	int max;
	int i;
	int arrSUM[10];

	scanf("%d %d",&ot,&jo);
	arrSUM[0] = jo;
	ppl = jo;
	for (i = 1; i < 4; i++){
		scanf("%d %d",&ot,&jo);
		ppl = ppl + jo - ot;
		arrSUM[i] = ppl;
	}

	max = arrSUM[0];
	for (i = 1; i < 4; i++){
		if(arrSUM[i]>max){
			max = arrSUM[i];
		}
		else{
		}
	}
	
//	printf("%d\n%d\n%d\n%d\n%d\n",max,arrSUM[0],arrSUM[1],arrSUM[2],arrSUM[3]);
	printf("%d",max);
}
```