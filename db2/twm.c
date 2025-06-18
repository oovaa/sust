#include <stdio.h>

void *mergSort(int *arr);
void *mergSortRec(int *arr, int l, int r);
void *mergSortedArr(int *arr, int l, int m, int r);

int main(int argc, char *argv[])
{

    int arr1[] = {1, 3, 5, 7, 9};
    int arr2[] = {2, 4, 6, 8, 10};
    int arr3[] = {0, 2, 4, 6, 8, 10};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    int size3 = sizeof(arr3) / sizeof(arr3[0]);
    printf("Array 1: ");
    for (int i = 0; i < size1; i++)

        printf("%d ", arr1[i]);

    printf("\nArray 2: ");
    for (int i = 0; i < size2; i++)

        printf("%d ", arr2[i]);

    printf("\nArray 3: ");
    for (int i = 0; i < size3; i++)
        printf("%d ", arr3[i]);

    return 0;
}

void *mergSort(int *arr)
{
    if (arr == NULL)
        return NULL;

    int len = sizeof(arr) / sizeof(arr[0]);
    mergSortRec(arr, 0, len - 1);
}
