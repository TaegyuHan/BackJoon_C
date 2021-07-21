# 2530 인공지능 시계

URL : [https://www.acmicpc.net/problem/2530](https://www.acmicpc.net/problem/2530)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct time
{
    int hour;   // (0 ≤ hour≤ 23)
    int minute; // (0 ≤ minute ≤ 59)
    int second; // (0 ≤ second ≤ 59)
    int timeSum;
    int makeSecond;
} Time;

int main(void)
{
    Time Time;
    scanf("%d %d %d %d",
            &Time.hour, 
            &Time.minute, 
            &Time.second,
            &Time.makeSecond );

    // 시간 모두 더하기
    Time.timeSum = Time.hour*3600 + 
                   Time.minute*60 + 
                   Time.second + 
                   Time.makeSecond; 

    // 시간 나누기
    Time.hour = (Time.timeSum/3600)%24;
    Time.minute = (Time.timeSum%3600)/60;
    Time.second = (Time.timeSum%60);

    printf("%d %d %d", Time.hour, Time.minute, Time.second);

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>

int main(){
	int hour = 0, min = 0, sec = 0;				//현재시간을 담는 변수(시, 분, 초), 0<=hour<=23, 0<=min<=59, 0<=sec<=59
	int cook_time = 0;					//요리하는데 필요한 시간(초), 0<=cook_time<=500,000
	int mok, namerge;				//cook_time을 60(초)로 나눈 몫과 나머지
	int time_sec, cook_after_time;

	//(1) 입력받기
	scanf("%d %d %d", &hour, &min, &sec);
	scanf("%d", &cook_time);

	//(2) 현재 시각을 초로 표현하기 & cook_time이 포함된 시간
	time_sec = hour * 3600 + min * 60 + sec;
	cook_after_time = cook_time + time_sec;

	//(3) 시,분,초로 표현하기
	hour = cook_after_time / 3600;
	cook_after_time -= hour * 3600;

	min = cook_after_time / 60;
	cook_after_time -= min * 60;
	
	sec = cook_after_time;

	//(4) 시간 출력하기
	if (hour >= 24){
		hour = hour % 24;
	}
	printf("%d %d %d\n", hour, min, sec);

	//system("pause");
	return 0;

}
```

```c
#include<stdio.h>

int main(){
	int min, hour,sec;
	int process;
	int prohour, promin,prosec;
	int temp;

	scanf("%d %d %d", &hour, &min,&sec);
	scanf("%d", &process);

	process = process % 86400;
	prosec = process % 60;
	temp = process / 60;
	promin = temp % 60;
	prohour = temp / 60;

	sec = sec + prosec;

	if (sec > 59){
		if (sec == 60){ sec = 0; promin += 1; }
		else{
			promin += 1;
			sec -= 60;
		}
	}

	min = min + promin;

	if (min > 59){
		if (min == 60){ min = 0; prohour += 1; }
		else{
			prohour += 1;
			min -= 60;
		}
	}

	hour = hour + prohour;

	if (hour >= 24){
		if (hour == 24){
			hour = 0;
		}
		else{
			hour -= 24;
		}
	}

	printf("%d %d %d\n", hour, min, sec);

}
```

```c
#include <stdio.h>

int main(void) {
    int hour, min, sec;
    int add_time;
    int finish_sec;
    
    scanf("%d %d %d", &hour, &min, &sec);
    scanf("%d", &add_time);
    
    finish_sec = sec + add_time;
    
    while(1) {
        if(finish_sec >=60) {
            min +=1;
            finish_sec -= 60;
            
            if(min>= 60) {
                hour +=1;
                min -= 60;
                
                if(hour >= 24) {
                    hour -= 24;
                }
            }
        }
        else
            break;
    }
    printf("%d %d %d\n", hour, min, finish_sec);
    
    return 0;
}
```