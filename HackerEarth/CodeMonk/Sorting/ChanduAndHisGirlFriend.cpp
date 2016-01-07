#include <iostream>

using namespace std;

int partition(long int arr[], int start, int end) {
	int j, i = start + 1;
	int piv = arr[start];
	for(j=start+1; j <= end; j++) {
		if(arr[j] > piv) {
			swap(arr[i], arr[j]);
			i++;
		}
	}
	swap(arr[start], arr[i-1]);
	return i-1;
}

int quick_sort(long int arr[], int start, int end) {
	if(start < end) {
		int piv_pos = partition(arr, start, end);
		quick_sort(arr, start, piv_pos-1);
		quick_sort(arr, piv_pos+1, end);
	}
}

int main() {
	int T, N, i;
	long int arr[100000];
	cin >> T;
	while(T--) {
		cin >> N;
		for(i=0; i < N; i++) {
			cin >> arr[i];
		}
		quick_sort(arr, 0, N-1);
		for(i=0; i < N; i++) {
			cout << arr[i] << " ";
		}
		cout << endl;
	}
	return 0;
}
