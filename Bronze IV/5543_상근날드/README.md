# 5543 상근날드

URL : [https://www.acmicpc.net/problem/5543](https://www.acmicpc.net/problem/5543)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

struct menu
{
    int TopBurger;
    int MidBurger;
    int BotBurger;
    int Coke;
    int Sprite;
};

int main(void)
{

    int LowPricedBurger,
        LowPricedDrink;
    struct menu home;

    scanf("%d", &home.TopBurger);
    scanf("%d", &home.MidBurger);
    scanf("%d", &home.BotBurger);
    scanf("%d", &home.Coke);
    scanf("%d", &home.Sprite);

    LowPricedBurger =
     (home.TopBurger >= home.MidBurger) ? 
        ((home.MidBurger >= home.BotBurger) ? home.BotBurger : home.MidBurger) : 
        ((home.TopBurger >= home.BotBurger) ? home.BotBurger : home.TopBurger);

    LowPricedDrink =
        (home.Coke >= home.Sprite) ? home.Sprite : home.Coke;

    printf("%d", LowPricedBurger + LowPricedDrink - 50);

	return 0;
}
```

숏 코드

```c
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int bugger[3] = {0};
    int drink[2] = {0};
    int input = 0;
    int i,j,temp = 0;
    
    for(i = 0; i < 3; i++){
        scanf("%d", &input);
        
        if((input<100)||(input>2000)){
            printf("input correctly!");
            exit(1);
        }
        
        bugger[i] = input;
    }
    
    for(i = 0; i < 2; i++){
        scanf("%d", &input);
        
        if((input<100)||(input>2000)){
            printf("input correctly!");
            exit(1);
        }
        
        drink[i] = input;
    }
    
    for(i = 0; i < 3; i++){
        for(j = i; j < 3; j++){
            if(bugger[i]>bugger[j]){
                temp = bugger[i];
                bugger[i] = bugger[j];
                bugger[j] = temp;
            }
        }
    }
    
    for(i = 0; i < 2; i++){
        for(j = i; j < 2; j++){
            if(drink[i]>drink[j]){
                temp = drink[i];
                drink[i] = drink[j];
                drink[j] = temp;
            }
        }
    }
    
    printf("%d", (drink[0] + bugger[0] - 50));
    
    return 0;
}
```

```c
#include <stdio.h>
#define SET_DISCOUNT 50;

int main() {
    int burger[3];
    int beverage[2];
    int minSetPrice = 0;
    
    for(int i=0; i<3; i++) {
        scanf("%d", &burger[i]);
    }
    
    for(int i=0; i<2; i++) {
        scanf("%d", &beverage[i]);
    }
    
    for(int i=0; i<sizeof(burger)/sizeof(int); i++) {
        for(int j=0; j<sizeof(beverage)/sizeof(int); j++) {
            int priceOfSet = burger[i]+beverage[j] - SET_DISCOUNT;
            
            if(
                minSetPrice == 0  ||
                minSetPrice > priceOfSet
            ) {
                minSetPrice = priceOfSet;
            }
        }
    }
    
    printf("%d", minSetPrice);
    
    
    return 0;
}
```