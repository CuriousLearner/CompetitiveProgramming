/*
    Question: https://www.hackerearth.com/code-monk-array-strings/algorithm/chandu-and-consecutive-letters/
*/

#include <stdio.h>

void make_good_string(char str[], int size) {
    int i, j;
    char temp;
    for(i=1; i<size; i++) {
        j = i;
        if(str[i] == str[i-1]) {
            while(str[j]!='\0') {
                str[j-1] = str[j];
                j++;
            }
            str[size-1] = '\0'; 
            size = size - 1;
            i--;
        }
    }
}

int main() {
    int t, i;
    char str[30];
    scanf("%d", &t);
    for(i=0; i<t; i++) {
        scanf("%s", str);
        make_good_string(str, strlen(str));
        printf("%s\n", str);
    }
    return 0;
}
