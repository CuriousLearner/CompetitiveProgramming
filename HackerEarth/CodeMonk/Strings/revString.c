/*
    Question: https://www.hackerearth.com/code-monk-array-strings/algorithm/terrible-chandu/
*/

#include <stdio.h>

void reverse(char str[], int size) {
    int i,j;
    char temp;
    for(i=0,j=size-1;i<=j;i++,j--) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;
    }
}

int main()
{
    int t, i, size;
    char str[30];
    scanf("%d\n", &t);
    for(i=0; i<t;i++) {
        scanf("%s", str);
        reverse(str, strlen(str));
        printf("%s\n", str);
    }
    return 0;
}
