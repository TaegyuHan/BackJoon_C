# 3009 네 번째 점

URL : [https://www.acmicpc.net/problem/3009](https://www.acmicpc.net/problem/3009)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>
int inputNum = 3;

typedef struct position
{
    int x; // 1<= x <=1000
    int y; // 1<= y <=1000
} Position;

typedef struct list
{
    Position Position[3];
} List;

void inputData(List * List)
{
    int i;
    for(i=0; i<inputNum; i++)
    {
        scanf("%d %d", 
                &List->Position[i].x,
                &List->Position[i].y );
    }
}

void findFourPosition(List List)
{
    int result_X,
        result_Y;

    if(List.Position[1].x == List.Position[2].x) {result_X = List.Position[0].x;}
    else if(List.Position[0].x == List.Position[1].x) {result_X = List.Position[2].x;}
    else if(List.Position[0].x == List.Position[2].x) {result_X = List.Position[1].x;}

    if(List.Position[1].y == List.Position[2].y) {result_Y = List.Position[0].y;}
    else if(List.Position[0].y == List.Position[1].y) {result_Y = List.Position[2].y;}
    else if(List.Position[0].y == List.Position[2].y) {result_Y = List.Position[1].y;}

    printf("%d %d", result_X, result_Y);
}

int main(void)
{
    int dig;
    List List;
    inputData(&List);
    findFourPosition(List);

    return 0;
}
```

숏 코딩

```c
//
//  main.c
//  AlgorithmTest
//
//  Created by CoolNzzz on 2020/01/24.
//  Copyright © 2020 CoolNzzz. All rights reserved.
//

#include <stdio.h>

typedef struct {
    int number;
    int count;
} numSet;

int main(int argc, const char * argv[]) {

    numSet numArrayX[2] = {{-1, 0}, {-1, 0}};
    numSet numArrayY[2] = {{-1, 0}, {-1, 0}};
    int x, y;
    
    for (int i = 0; i < 3; i++) {
        int x, y;
        scanf("%d %d", &x, &y);
        
        for (int j = 0; j < 2; j++) {
            if (numArrayX[j].number == -1) {
                numArrayX[j].number = x;
                numArrayX[j].count++;
                break;
            } else if (numArrayX[j].number == x) {
                numArrayX[j].count++;
                break;
            } else {
                continue;
            }
        }
        
        for (int j = 0; j < 2; j++) {
            if (numArrayY[j].number == -1) {
                numArrayY[j].number = y;
                numArrayY[j].count++;
                break;
            } else if (numArrayY[j].number == y) {
                numArrayY[j].count++;
                break;
            } else {
                continue;
            }
        }
    }
        
    x = numArrayX[0].count == 1 ? numArrayX[0].number : numArrayX[1].number;
    y = numArrayY[0].count == 1 ? numArrayY[0].number : numArrayY[1].number;
    
    printf("%d %d\n", x, y);

    return 0;
}
```

```c
#include <stdio.h>
int main(){
    int a1,a2,b1,b2,c1,c2;
    int d1,d2;

    scanf("%d %d",&a1,&a2);
    scanf("%d %d",&b1,&b2);
    scanf("%d %d",&c1,&c2);
    if(a1 != b1){
        if(a1 != c1){
            d1 = a1;
        }
        else{
            d1 = b1;
        }
    }
    else{
        if(a1 != c1){
            d1 = c1;
        }
    }

    if(a2 != b2){
        if(a2 != c2){
            d2 = a2;
        }
        else{
            d2 = b2;
        }
    }
    else{
        if(a2 != c2){
            d2 = c2;
        }
    }
    printf("%d %d",d1,d2);
}
```