# 2920 음계

URL : [https://www.acmicpc.net/problem/2920](https://www.acmicpc.net/problem/2920)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

int main(void)
{
    char i, j=0;
    char list[16];
    char ascending=1,
         descending=1,
         mixed=1;

    scanf("%[^\n]s", list);

    for(i=0; list[i]!=NULL; i++)
    {
        if(list[i]==' ')
            continue;

        if(descending==1 && list[i]=='8'-j)
        {
            ascending=0;
            mixed=0;
        }
        else if(ascending==1 && list[i]=='1'+j)
        {
            descending=0;
            mixed=0;
        }
        else
        {
            ascending=0;
            descending=0;
            mixed=1;
            printf("mixed");
            return 0;
        }
        j++;
    }

    if(descending==1)
        printf("descending");
    else
        printf("ascending");

    return 0;
}
```

숏코딩

```c
s;main(i){for(;~scanf("%d",&i);)s=s*2+i;puts(s-502?s-1793?"mixed":"descending":"ascending");}
```

```c
#include<stdio.h>
int main()
{
	int a[8],b,c=0;
	for(b=0;b<8;b++){
		scanf("%d",&a[b]);
		if(a[b]==b+1){
			c+=1;
		}
		else if(a[b]==8-b){
			c+=2;
		}
	}
	if(c==8)
		printf("ascending");
	else if(c==16)
		printf("descending");
	else
		printf("mixed");
	
	return 0;
}
```

```c
#include <stdio.h>
int main(){
	int a, b, c, state, i;
	scanf("%d%d", &a, &b);
	state = b - a > 0 ? 1 : 0;
	for(i = 0; i < 6; i++){
		scanf("%d", &c);
		if(state != c - b > 0 ? 1 : 0){
			printf("mixed");
			return 0;
		}
		a = b;
		b = c;
	}
	printf("%sscending", state ? "a" : "de");
}
```

```c
#include<stdio.h>
int main(){
	int as=0, ds=0;	
	int a[8];
	
	for(int i = 0; i<8; i++){
		scanf("%d", &a[i]);
		
		if(i+1==a[i])
			as++;
		else if(8-i == a[i])
			ds++;
	}
	
		if(as==8)
			printf("ascending");	
		else if(ds==8)
			printf("descending");
		else
			printf("mixed");

	return 0;
}
```