#include <stdio.h>
#include <limits.h>

#define K 3  // Number of sorted arrays to merge
#define N 4  // Number of elements in each array

// Merge K sorted arrays into result[]
// Find the index of the array with the current minimum element
int findMinIndex(int arr[K][N], int idx[K]) {
    int min_val = INT_MAX, min_idx = -1;
    for (int j = 0; j < K; ++j) {
        if (idx[j] < N && arr[j][idx[j]] < min_val) {
            min_val = arr[j][idx[j]];
            min_idx = j;
        }
    }
    return min_idx;
}

// Merge K sorted arrays into result[]
void kWayMerge(int arr[K][N], int result[K*N]) {
    int idx[K] = {0}; // Current index of each array

    for (int i = 0; i < K*N; ++i) {
        int min_idx = findMinIndex(arr, idx);
        result[i] = arr[min_idx][idx[min_idx]];
        idx[min_idx]++;
    }
}

int main() {
    int arr[K][N] = {
        {1, 5, 9, 21},
        {4, 6, 8, 20},
        {2, 7, 15, 22}
    };
    int result[K*N];

    kWayMerge(arr, result);

    printf("Merged array:\n");
    for (int i = 0; i < K*N; ++i)
        printf("%d ", result[i]);
    printf("\n");

    return 0;
}