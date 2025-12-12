public class assigment1 {

    public static void main(String[] args) {
        int[] arr = { 5, 3, 7, 12, 8, 4, 1, 2 };
        for (int i : arr) {
            System.out.print(i + " - ");
        }
        System.out.println();

        insertion_sort(arr);
        for (int i : arr) {
            System.out.print(i + " - ");
        }
        System.out.println();

    }

    static void bubble_sort(int[] arr) {
        /////// 1 + n *n * 1 + 1 + 1 + 1 = 5 + n*n = n^2
        int temp; // o(1)
        for (int i = 0; i < arr.length; i++) { // o (n)
            for (int j = i; j < arr.length; j++) { // o(n)
                if (arr[j] < arr[i]) { // o(1)
                    temp = arr[j]; // O(1)
                    arr[j] = arr[i]; // O(1)
                    arr[i] = temp; // O(1)
                }
            }
        }
    }

    // iiiiinnnnnn
    static void insertion_sort(int[] arr) {
        /////// 1 + n * 1 * 1 * n * 1 * 1 + 1 = 1 + n*n = n^2

        int n = arr.length; // o 1
        for (int i = 1; i < n; ++i) { // o(n)
            int key = arr[i]; // o(1)
            int j = i - 1; // O(1)

            while (j >= 0 && arr[j] > key) { // o(i) worst case o(n)
                arr[j + 1] = arr[j]; // O(1)
                j = j - 1; // O(1)
            }
            arr[j + 1] = key; // O(1)
        }
    }

    static void selection_sort(int[] arr) {
        ///// 1 * n * 1 * n 1 * 1 * 1 = n*n = n^2
        int min, temp; // min is the first o (1)
        for (int i = 0; i < arr.length; i++) { // first loop used for swap o(n)
            min = i; // o(1)
            for (int j = i + 1; j < arr.length; j++) // lop to find the min from i to end O(n)
                if (arr[j] < arr[min]) // if j < min min = j o(1)
                    min = j;
            // System.out.println("min " + min + " i " + i + " arr[i] " + arr[i]);
            temp = arr[min]; // o(1)
            arr[min] = arr[i]; // o(1)
            arr[i] = temp; // o(1)
        }

    }

    // Assignment 1:

    // Explain by (steps) show me the efficient or time complexity of

    // 1- selection sort algorithm
    // 2- insertion sort algorithm
    // 3- bubble 🫧 sort algorithm

    // by way the efficient is O(n)^2 for both.

    // samih369369@gmail.com
}