#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int n;

    scanf("%d", &n);
    if (n % 2 == 0)
        printf("SK\n");
    else
        printf("CY\n");
    return 0;
}
