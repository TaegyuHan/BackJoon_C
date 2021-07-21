# 2420 사파리월드

URL : [https://www.acmicpc.net/problem/2420](https://www.acmicpc.net/problem/2420)

```c
#define _CRT_SECURE_NOWARNINGS
#include <stdio.h>

typedef long long int LLINT;

typedef struct safariWorld
{
    LLINT subDomain1; // (-2,000,000,000 ≤ subDomain1 ≤ 2,000,000,000)
    LLINT subDomain2; // (-2,000,000,000 ≤ subDomain2 ≤ 2,000,000,000)
} SafariWorld;

LLINT abs(LLINT num) 
{ 
    return (num > 0) ? num : -num; 
}

int main(void)
{
    LLINT result;
    SafariWorld SafariWorld;

    scanf("%lld %lld", 
            &SafariWorld.subDomain1,
            &SafariWorld.subDomain2 );

    printf("%lld",
            abs(SafariWorld.subDomain1 - SafariWorld.subDomain2));

    return 0;
}
```

숏 코딩

```c
#include <stdio.h>
int main()
{    
	int n, m;
	int result_a;
	unsigned int result;
	scanf("%d %d", &n, &m);
	if( (n > 0 && m > 0) || (n < 0 && m < 0))    
	{   // minus        
		if( n > m ) 
			result_a = n - m;  
		else  
			result_a = m - n; 
		if( result_a < 0)
			result = result_a * -1;
		else    
			result = result_a;
	}    
	else 
	{ 
		if( n < 0) 
			n = n * -1;  
		if( m < 0)
			m = m * -1;    
		result = (unsigned int )n + (unsigned int)m;
	}   
	printf("%u\n", result);
	return 0;
}
```

```c
#include <stdio.h>

main(){
	long long int n,m,result;
	scanf("%lld %lld",&n,&m);
	if(n<0&&m<0){
		if(n>m){
			result = m*-1 + n;
		}else{
			result = n*-1 +m;
		}
	}else if(n<0&&m>=0){
		result = (n-m)*(-1);
	}else if(n>=0&&m<0){
		result = (m-n)*(-1);
	}else if(n>=0&&m>=0){
		if(n>m){
			result = n-m;
		}else{
			result = m-n;
		}
	}
	printf("%lld",result);
	
}
```