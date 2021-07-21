# 10156 과자

URL : [https://www.acmicpc.net/problem/10156](https://www.acmicpc.net/problem/10156)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct dongsu
{
    int snacks; // (1 ≤ snacks ≤ 1,000) 
    int number; // (1 ≤ number ≤ 1,000) 
    int money;  // (1 ≤ money ≤ 100,000)
} Dongsu;

int main(void)
{
    int result;
    Dongsu Dongsu;

    scanf("%d %d %d", 
            &Dongsu.snacks,
            &Dongsu.number,
            &Dongsu.money );

    result = Dongsu.snacks * Dongsu.number - Dongsu.money;
    if(result > 0)
        printf("%d", result);
    else 
        printf("0");

    return 0;
}
```

숏코딩

```c
#include <stdio.h>

typedef unsigned long int ULong;

int main(int argc, char *argv[]);
void Input(ULong *snack, ULong *numberOfSnack, ULong *money);
ULong AddMoney(ULong snack, ULong numberOfSnack, ULong money);
void Output(ULong addMoney);

int main(int argc, char *argv[])
{
	ULong snack;
	ULong numberOfSnack;
	ULong money;
	ULong addMoney;

	Input(&snack, &numberOfSnack, &money);
	addMoney = AddMoney(snack, numberOfSnack, money);
	Output(addMoney);
	return 0;
}

void Input(ULong *snack, ULong *numberOfSnack, ULong *money)
{
	scanf("%d", snack);
	scanf("%d", numberOfSnack);
	scanf("%d", money);
}

ULong AddMoney(ULong snack, ULong numberOfSnack, ULong money)
{
	ULong addMoney;
	ULong price;

	price = snack * numberOfSnack;
	if (price > money)
	{
		addMoney = price - money;
	}
    else
    {
        addMoney = 0; 
    }

	return addMoney;
}

void Output(ULong addMoney)
{
	printf("%d\n", addMoney);
}
```

```c
#include <stdio.h>

/*과자*/

int main()
{
    /*동수는 현재 가지고 있는 돈이 모자랄 경우 부모님께 모자란 돈을 받으려고 한다.*/
    
    /*과자 한 개의 가격은 K이고, 사려고 하는 과자의 개수는 N, 현재 가지고 있는 돈의 액수는 M이다.*/
    int K, N, M;
    scanf("%d %d %d", &K, &N, &M);
    
    /*부모님께 받아야하는 액수는 과자 한 개의 가격 × 개수에서 자신의 현재 가지고 있는 돈의 액수를 뺀만큼이다.*/
    
    int result = K*N-M;
    
    /*가지고 있는 돈만으로 충분하다면, 그 결과값은 0이 될 것이다.*/
    if(result < 0)
    {
        result = 0;
    }
    
    printf("%d", result);
}
```

```c
#include <stdio.h>

#include	<stdlib.h>

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
		int
main ( int argc, char *argv[] )
{
		int snack_price, snack_num, mymoney, result;
		scanf("%d %d %d",&snack_price,&snack_num,&mymoney);
		result = snack_price*snack_num - mymoney;
		if(result>0)
		{
				printf("%d\n",result);
		}
		else
		{
				printf ( "0\n" );
		}
		return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
```