#include<iostream>
using namespace std;
int main()
{
    int x,min,max;
    while(scanf("%d",&x)==1)
    {
        min=x<min?x:min;
        max=x>max?x:max;
    }
    printf("%d %d",min,max);
return 0;
}