/*
    Question: https://www.hackerearth.com/code-monk-array-strings/algorithm/prateek-and-his-friends/
*/

#include <stdio.h>

int main() {
    int t, total_money, no_of_friends, i, j, k, max_so_far;
    int arr[1000000];
    scanf("%d", &t);
    for(i=0; i<t; i++) {
        scanf("%d %d", &no_of_friends, &total_money);
        for(j=0; j<no_of_friends; j++) {
            scanf("%d", &arr[j]);
        }
        // Find the longest sequence equal to total_money
        max_so_far = 0;
        k = 0;
        for(j=0; j<no_of_friends; j++) {
            max_so_far += arr[j];
            if(max_so_far == total_money) {
                printf("YES\n");
                break;
            }
            if(max_so_far > total_money) {
                max_so_far = 0;
                k++;
                j = k-1;
            }
            if(j==(no_of_friends-1)) {
                printf("NO\n");
            }
        }
    }
    return 0;
}
