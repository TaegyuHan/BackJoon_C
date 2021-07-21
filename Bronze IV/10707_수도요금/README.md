# 10707 수도요금

URL : [https://www.acmicpc.net/problem/10707](https://www.acmicpc.net/problem/10707)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct company
{   
    int X_OneLBill;        // 1 이상 10000
    int Y_BasicBill;       // 1 이상 10000
    int Y_Maximum;         // 1 이상 10000
    int Y_OneLExtraCharge; // 1 이상 10000
    int USE_Water;         // 1 이상 10000

} Company;

int Y_CpyCalculation(int BasicBill,int Maximum, int OneLExtraCharge, int USE_Water)
{
    int result;

    if(USE_Water > Maximum)
        result = (BasicBill + (USE_Water - Maximum)*OneLExtraCharge);
    else
        result = BasicBill;

    return result;
}

int main(void)
{
    Company CPY;
    int X_CpyBill;
    int Y_CpyBill;

    scanf("%d %d %d %d %d",
            &X_CpyBill,
            &CPY.Y_BasicBill,
            &CPY.Y_Maximum,
            &CPY.Y_OneLExtraCharge,
            &CPY.USE_Water );

    X_CpyBill = X_CpyBill * CPY.USE_Water;

    Y_CpyBill = Y_CpyCalculation(CPY.Y_BasicBill, CPY.Y_Maximum,
                                 CPY.Y_OneLExtraCharge, CPY.USE_Water);

    if(X_CpyBill > Y_CpyBill)
        printf("%d", Y_CpyBill);
    else
        printf("%d", X_CpyBill);

    return 0;
}
```

숏 코딩

```c
#include<stdio.h>
int calc_X(int used, int literpermoney){
	return (used * literpermoney);
	// (리터당 요금 * 사용량) 청구 
}

int calc_Y(int used, int basemoney, int limitliter, int literpermoney){
	if(used <= limitliter){
	//기본사용량 이하 사용: 
		return basemoney;
		// 기본요금만 청구. 
	}else{
	//기본사용량 초과 사용: 
		return (basemoney + ((used - limitliter) * literpermoney));
		// (기본요금 + (초과사용량 * 리터당 요금))  청구. 
	}
}

int main(void){
	int used = 0;				// 사용량 
	int literpermoneyX = 0;		// X사의 리터당 요금 
	int limitliterY = 0;		// Y사의 기본사용량. 
	int basemoneyY = 0;			// Y사의 기본요금 
	int literpermoneyY = 0;		// Y사의 리터당 초과요금.
	
	scanf("%d", &literpermoneyX);
	scanf("%d", &basemoneyY);
	scanf("%d", &limitliterY);  
	scanf("%d", &literpermoneyY); 
	scanf("%d", &used);
	
	
	
	int moneyX = calc_X(used, literpermoneyX);
	// X사 요금 계산. 
	int moneyY = calc_Y(used, basemoneyY, limitliterY, literpermoneyY);
	// Y사 요금 계산. 
	
	int money = (moneyX > moneyY)?(moneyY):(moneyX);
	//삼항연산자: Y사가 저렴하면 Y사 값, 아니면 X사 값. 
	printf("%d\n", money);
	//출력 
	
	return 0;
}
```

```c
#include <stdio.h>

int xGasPrice(int xGas, int joi)
{
	return xGas * joi;
}
int yGasPrice(int yGas, int joi, int yGasBasic, int yGasMax)
{
	int excess = 0;
	int basicGasPrice = 0;
	if(joi >= yGasMax)
	{
		excess = joi - yGasMax;
		basicGasPrice = yGas * excess;
		return yGasBasic + basicGasPrice;
	}
	if(excess == 0)
	{
		basicGasPrice = 0;	
	}
	return yGasBasic + basicGasPrice;
}

int main(void) {
	int xGas;
	int yGasBasic;
	int yGasMax;
	int yGas;
	int joi;
	
	scanf("%d %d %d %d %d", &xGas, &yGasBasic, &yGasMax, &yGas, &joi);
	
	//printf("%d, %d", xGasPrice(xGas, joi), yGasPrice(yGas, joi, yGasBasic, yGasMax));
	if(xGasPrice(xGas, joi) < yGasPrice(yGas, joi, yGasBasic, yGasMax) )
	{
		printf("%d", xGasPrice(xGas, joi));
	}
	else {
		printf("%d", yGasPrice(yGas, joi, yGasBasic, yGasMax));
	}
	
	return 0;
}
```