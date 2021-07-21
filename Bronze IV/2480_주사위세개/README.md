# 2480 주사위세개

URL : [https://www.acmicpc.net/problem/2480](https://www.acmicpc.net/problem/2480)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef struct dice
{
    int number;
} Dice;

int main(void)
{
    int i;
    int tempNumber;
    Dice Dice[3];

    for(i=0; i<3; i++)
    {
        scanf("%d", &Dice[i].number);
    }

    // 3개가 같은 수
    if(Dice[0].number==Dice[1].number && 
       Dice[0].number==Dice[2].number)
    {
        printf("%d", 10000+Dice[0].number*1000);
        return 0;
    } // 2개가 같은 수
    else if(Dice[0].number==Dice[1].number || 
            Dice[0].number==Dice[2].number ||
            Dice[1].number==Dice[2].number )
    {
        tempNumber = (Dice[0].number==Dice[1].number) ? 
                      Dice[1].number : Dice[2].number;
        printf("%d", 1000 + tempNumber*100);
        return 0;
    } // 3개의 수가 전부 다른 경우
    else
    {   // 3개중에 가장큰수 tempNumber에 저장
        tempNumber = (Dice[0].number > Dice[1].number) ? 
                     ((Dice[0].number > Dice[2].number) ? Dice[0].number : Dice[2].number ) : 
                     ((Dice[1].number > Dice[2].number) ? Dice[1].number : Dice[2].number );
        printf("%d", tempNumber*100);
        return 0;
    }
}
```

숏 코딩

```c
#include <stdio.h>

int size_re(int *p, int *p1, int *p2);
int same_count(int *p, int *p1, int *p2);
int sum(int flag, int big,int *p, int *p1, int *p2);

int main()
{
	int num[3]={0};
	int big=0;
	int same_flag=0;

	scanf("%d %d %d", &num[0], &num[1], &num[2]);

	big=size_re(num,num+1,num+2);

	same_flag=same_count(num,num+1,num+2);

	sum(same_flag, big, num,num+1,num+2);

}

int size_re(int *p, int *p1, int *p2)
{
	int big=0;
	big=(p[0]>p[1])? p[0] : p[1];

	big=(big>p[2])? big : p[2];

	return big;
}

int same_count(int *p, int *p1, int *p2) // 다를 경우 1, 2개가 같을경우2 3개가 다 같을경우 4
{
	int count=1;
	int one=1;
	while(one--)
	{
		if(p[0]==p[1]) count++;
		
		if(p[2]==p[1]) count++;
		
		if(p[0]==p[2]) count++;
	}

	return count;
}

int sum(int flag, int big, int *p, int *p1, int *p2)
{
	int sum=0;

	if(flag==1)
	{
		printf("%d", big*100);
	}

	else if(flag==2)
	{
		if(p[0]==p[1]) printf("%d",1000+p[0]*100);
		else if(p[0]==p[2]) printf("%d",1000+p[0]*100);
		else if(p[1]==p[2]) printf("%d",1000+p[1]*100);
		else;
	}

	else if(flag==4)
	{
		printf("%d", 10000+p[0]*1000);
	}

	else;
}
```

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if(a==b&&b==c)
         {
              printf("%d",10000+a*1000);
         }
 
    else if(a==b&&a!=c||b==c&&b!=a||a==c&&a!=b)
                       {
                             if     (a==b)
                                     {printf("%d",1000+b*100);}
                             else if(a==c)
                                     {printf("%d",1000+a*100);}
                             else
                                     {printf("%d",1000+c*100);}
                       }
    else
                          {
      if(a>b){
              if(c>a)
                 {printf("%d",c*100);}
              else if(c>b)
                 {printf("%d",a*100);}
              else
                 {printf("%d",a*100);}
              }
      
      else   {
              if(c>b)
                 {printf("%d",c*100);}
              else if(c>a)
                 {printf("%d",b*100);}
              else
                 {printf("%d",b*100);}
              }
                           }
           

  return 0;
}
```

```c
#include <stdio.h>

int main()
{
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if(a==b&&b==c)
        printf("%d",10000+1000*a);
    else if(a==b && b!=c)
        printf("%d",1000+100*a);
    else if(c==b && a!=c)
        printf("%d",1000+100*c);
    else if(a==c && b!=c)
        printf("%d",1000+100*c);
    else
        if(a>b)
            if(b>=c)
                printf("%d",a*100);
            else if(a>c)
                printf("%d",a*100);
            else
                printf("%d",c*100);
        else
            if(a>=c)
                printf("%d",b*100);
            else if(b>c)
                printf("%d",b*100);
            else
                printf("%d",c*100);
    return 0;
}
```

```c
#include <stdio.h>

int main()
{
	int a, b, c;
	
	scanf("%d %d %d", &a, &b, &c);
	
	if (a == b)
	{
		if (a == c)
		{
			printf("%d", 10000 + a * 1000);
		}
		else
		{
			printf("%d", 1000 + a * 100);
		}
	}
	else if (a == c || b == c)
	{
		printf("%d", 1000 + c * 100);
	}
	else
	{
		if (a < b)
		{
			a = b;
		}
		if (a > c)
		{
			c = a;
		}
		printf("%d", c * 100);

	}

}
```