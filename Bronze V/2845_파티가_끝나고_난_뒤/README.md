# 2845 파티가 끝나고 난 뒤

URL : [https://www.acmicpc.net/problem/2845](https://www.acmicpc.net/problem/2845)

```c
int main(void)
{
    int i;
    int M, P;
    int news;
    
    scanf("%d %d", &M, &P);

    for(i=0; i<5; i++)
    {
        scanf("%d", &news);

        if(i<5)
            printf("%d ", news-(M*P));
        else
            printf("%d", news-(M*P));
    }

    return 0;
}
```