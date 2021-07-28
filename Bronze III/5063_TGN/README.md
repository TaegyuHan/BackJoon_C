# 5063 TGN

URL : [https://www.acmicpc.net/problem/5063](https://www.acmicpc.net/problem/5063)

```c
#include <stdio.h>

typedef struct _Advertisement
{
	int TestCnt;
	int AnOtherIncome;
	int ADIncome;
	int ADexpenses;

} Advertisement;

void InputDataTestCount(Advertisement* AD)
{
	scanf("%d", &AD->TestCnt);
}

void InputDataAD(Advertisement* AD)
{
	scanf("%d %d %d", 
			&AD->AnOtherIncome,
			&AD->ADIncome,
			&AD->ADexpenses);
}

int ProfitCalculation(Advertisement* AD)
{
	int money = AD->ADIncome - (AD->AnOtherIncome + AD->ADexpenses);

	if (money > 0)
		return 1;
	else if (money == 0)
		return 0;
	else if (money <0)
		return -1;
}

void ShowResult(int state)
{
	if (state > 0)
		printf("advertise\n");
	else if (state == 0)
		printf("does not matter\n");
	else if (state < 0)
		printf("do not advertise\n");
}

int main(void) 
{
	int i;
	int state;
	Advertisement AD;

	InputDataTestCount(&AD);

	for (i = 0; i < AD.TestCnt; i++)
	{
		InputDataAD(&AD);
		state = ProfitCalculation(&AD);
		ShowResult(state);
	}

	return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(void){
    int T;
    int r,e,c;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        scanf("%d %d %d",&r,&e,&c);
        if(r<e-c){
            printf("advertise\n");    
        }
        else if(r==e-c){
            printf("does not matter\n");
        }
        else{
            printf("do not advertise\n");
        }
    }
    return 0;
}
```

```c
#include<stdio.h>
int main(){
	int testCase =0;
	int r=0,e=0,c=0;
	int temp=0;
	scanf("%d",&testCase);
	for(int i=0 ; i<testCase;i++){
		scanf("%d %d %d",&r,&e,&c);
		temp = e-c;
		if(r==temp){
			printf("does not matter\n");
			continue;
		}
		
		if((r)<(temp)){
			printf("advertise\n");
			continue;
		}else{
			printf("do not advertise\n");
			continue;
		}
	
	}
    return 0;
}
```

```c
#include <stdio.h>
int main(void)
{
    int num, r, e, c;
    scanf("%d",&num);
    for(int i=0; i<num; i++)
    {
        scanf("%d %d %d",&r, &e, &c);
        if(e > c+r)
            printf("advertise\n");
        else if(e == c+r)
            printf("does not matter\n");
        else
            printf("do not advertise\n");
    }
    return 0;
}
```