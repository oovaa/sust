#include <stdio.h>
#include <stdlib.h>

void mergeSort(int *arr, int len);
void mergeSortRec(int *arr, int l, int r);
void merge(int *arr, int l, int m, int r);

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

    int unsorted[] = {7, 2, 9, 1, 5, 3, 8, 4, 6, 0};
    int unsorted_size = sizeof(unsorted) / sizeof(unsorted[0]);
    printf("\nUnsorted array: ");
    for (int i = 0; i < unsorted_size; i++)
        printf("%d ", unsorted[i]);
    printf("\n");
    mergeSort(unsorted, unsorted_size);
    printf("Sorted array:   ");
    for (int i = 0; i < unsorted_size; i++)
        printf("%d ", unsorted[i]);
    printf("\n");

    return 0;
}

void mergeSort(int *arr, int len)
{
    if (arr == NULL)
        return;

    mergeSortRec(arr, 0, len - 1);
}

void mergeSortRec(int *arr, int l, int r)
{

    if (l >= r)
        return;

    int m = (r + l) / 2;

    mergeSortRec(arr, l, m);
    mergeSortRec(arr, m + 1, r);

    merge(arr, l, m, r);
}

void merge(int *arr, int l, int m, int r)
{
    int size = r - l + 1;
    int *temp = malloc((r - l + 1) * sizeof(int));
    int i = l, j = m + 1, k = 0;

    while (i <= m && j <= r)
    {
        if (arr[i] < arr[j])

        {
            temp[k] = arr[i];
            i++;
        }
        else if (arr[i] > arr[j])
        {
            temp[k] = arr[j];
            j++;
        }
        else
        {
            temp[k] = arr[i];
            i++;
        }
        k++;
    }
    while (i <= m)
    {
        temp[k] = arr[i];
        i++;
        k++;
    }
    while (j <= r)
    {
        temp[k] = arr[j];
        j++;
        k++;
    }
    for (int x = 0; x < size; x++)
        arr[l + x] = temp[x];
    free(temp);
}
