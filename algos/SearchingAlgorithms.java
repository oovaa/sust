import java.util.HashMap;
import java.util.Map;

public class SearchingAlgorithms {

    /*
     * 
     * linear search
     * i = 0 // -----> 1
     * while i < n and arr[i] != R do // -----> n
     * i++ // -----> 1
     * if i < n return i // -----> 1
     * else return -1 // -----> 1
     * 1 + n + 1+ 1 = 3+n = n
     
     * 
     * so the best case is found in the first inedx O(1)
     * the avg is O(n/2)
     * the worst is O(n)
     * 
     * 
     * can be improved by  Sentinel Linear.
     */

    // ==========================================
    // 1. SENTINEL LINEAR SEARCH (Improved Linear)
    // ==========================================
    /*
     * PSEUDO CODE:
     * Set Sentinel at arr[n-1]
     * Scan without checking i < n
     * Restore arr[n-1]
     * Check if found
     *
     *
     * sol:
     * i = 0 (1) + Loop (n) + Check (1) = n + 2
     *
     * best case: O(1)
     * avg case: O(n) (mathematically n/2 steps)
     * worst case: O(n)
     *
     * Improvement: Removes the "i < n" check inside the loop,
     * reducing comparisons by 50%.
     */
    public static int sentinelLinearSearch(int[] arr, int target) {
        int n = arr.length; // -----> 1
        if (n == 0)
            return -1; // -----> 1

        int last = arr[n - 1]; // -----> 1
        arr[n - 1] = target; // -----> 1 (Set Sentinel)

        int i = 0; // -----> 1
        while (arr[i] != target) { // -----> n (No i < n check!)
            i++; // -----> n
        }

        arr[n - 1] = last; // -----> 1 (Restore)

        if (i < n - 1 || arr[n - 1] == target) // -----> 1
            return i; // -----> 1

        return -1; // -----> 1
    }

    // ==========================================
    // 2. JUMP SEARCH (Requires Sorted Array)
    // ==========================================
    /*
     * PSEUDO CODE:
     * Jump in steps of SQRT(n)
     * Perform linear search in the block
     *
     *
     * sol:
     * 1+1+1 + sqrt(n) + 1+1+1 + sqrt(n) + 1+1 = 2*sqrt(n)
     *
     * Time Complexity: O(sqrt(n))
     */
    public static int jumpSearch(int[] arr, int target) {
        int n = arr.length; // ----> 1
        int step = (int) Math.floor(Math.sqrt(n)); // -----> 1
        int prev = 0; // -----> 1

        // Jump blocks
        while (arr[Math.min(step, n) - 1] < target) { // -----> sqrt(n)
            prev = step; // -----> 1
            step += (int) Math.floor(Math.sqrt(n)); // -----> 1
            if (prev >= n) // -----> 1
                return -1; // -----> 1
        }

        // Linear search within block
        while (arr[prev] < target) { // -----> sqrt(n)
            prev++; // -----> 1
            if (prev == Math.min(step, n)) // -----> 1
                return -1; // -----> 1
        }

        if (arr[prev] == target) // -----> 1
            return prev; // -----> 1
        return -1; // -----> 1
    }

    // ==========================================
    // 3. INTERPOLATION SEARCH (Requires Sorted, Uniform Array
    // ==========================================
    /*
     * PSEUDO CODE:
     * Probe position based on value formula
     * Adjust low/high based on probe
     *
     *
     * sol:
     * 1+1 + n + 1+1+1+1+1 = O(n)
     *
     * worst case: O(n) (if data increases exponentially)
     * avg case: O(log(log(n))) (if data is uniform)
     */
    public static int interpolationSearch(int[] arr, int target) {
        int low = 0; // ----> 
        int high = arr.length - 1; // ----> 1

        while (low <= high && target >= arr[low] && target <= arr[high]) { // ----> n (worst) or log(log n) (avg)

            if (low == high) { // ----> 1
                if (arr[low] == target)
                    return low; // ----> 1
                return -1; // ----> 1
            }

            // Calculating position
            int pos = low + (((high - low) / (arr[high] - arr[low])) * (target - arr[low])); // ----> n

            if (arr[pos] == target)
                return pos; // ----> 1

            if (arr[pos] < target)
                low = pos + 1; // ----> 1
            else
                high = pos - 1; // ----> 1
        }
        return -1; // ----> 1
    }

    // ==========================================
    // 4. BINARY SEARCH (Requires Sorted Array)
    // ==========================================
    /*
     * PSEUDO CODE:
     * Split array in half repeatedly
     *
     *
     * sol:
     * 1+1 + log(n) + 1+1+1 = O(log n)
     *
     * worst case: O(log n)
     * avg case: O(log n)
     */
    public static int binarySearch(int[] arr, int target, int low, int high) {
        while (low <= high) { // -----> log(n)
            int mid = low + (high - low) / 2; // -----> log(n)

            if (arr[mid] == target) // -----> log(n)
                return mid;
            else if (arr[mid] < target) // -----> log(n)
                low = mid + 1; // -----> log(n)
            else
                high = mid - 1; // -----> log(n)
        }
        return -1; // -----> 1
    }

    // Overload for simple calling
    public static int binarySearch(int[] arr, int target) {
        return binarySearch(arr, target, 0, arr.length - 1);
    }

    // ==========================================
    // 5. EXPONENTIAL SEARCH (Requires Sorted Array)
    // ==========================================
    /*
     * PSEUDO CODE:
     * Find range by doubling i
     * Binary Search the range
     *
     *
     * sol:
     * 1 + log(i) + log(n) = O(log n)
     *
     * worst case: O(log n)
     */
    public static int exponentialSearch(int[] arr, int target) {
        int n = arr.length;
        if (arr[0] == target) // -----> 1
            return 0;

        int i = 1; // -----> 1
        while (i < n && arr[i] <= target) { // -----> log(i)
            i = i * 2; // -----> log(i)
        }

        // Call Binary Search for the identified range
        return binarySearch(arr, target, i / 2, Math.min(i, n - 1)); // ------> log(n)
    }

    // ==========================================
    // 6. HASH TABLE SEARCH
    // ==========================================
    /*
     * PSEUDO CODE:
     * Build HashMap (Map value -> index)
     * Lookup target
     *
     *
     * sol:
     * 
     * 
     * hash is the best in the avg case cuz it is O(1) normally due to hashing
     * when the items have the same hash it stores them in boket
     * wich is a linked list in the same hash location so searching becomes linear
     * O(n)
     * 
     * 
     * Build: O(n)
     * Search: O(1)
     *
     * best/avg case: O(1) (Direct lookup)
     * worst case: O(n) (Collisions leading to linked list scan)
     */
    public static int hashTableSearch(int[] arr, int target) {
        Map<Integer, Integer> map = new HashMap<>(); // -----> 1

        // Preprocessing: Build the Table
        for (int i = 0; i < arr.length; i++) { // -----> n
            map.put(arr[i], i); // -----> n
        }

        // Actual search
        if (map.containsKey(target)) { // -----> 1 (avg)
            return map.get(target); // -----> 1
        }
        return -1; // -----> 1
    }

    // ==========================================
    // MAIN METHOD (Usage Examples)
    // ==========================================
    public static void main(String[] args) {
        int[] sortedData = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120 };
        int[] unsortedData = { 35, 12, 99, 10, 5, 70, 2 };
        int target = 70;

        System.out.println("--- 1. Sentinel Linear Search (Unsorted) ---");
        System.out.println("Found 70 at index: " + sentinelLinearSearch(unsortedData, target));

        System.out.println("\n--- 2. Jump Search (Sorted) ---");
        System.out.println("Found 70 at index: " + jumpSearch(sortedData, target));

        System.out.println("\n--- 3. Interpolation Search (Sorted) ---");
        System.out.println("Found 70 at index: " + interpolationSearch(sortedData, target));

        System.out.println("\n--- 4. Binary Search (Sorted) ---");
        System.out.println("Found 70 at index: " + binarySearch(sortedData, target));

        System.out.println("\n--- 5. Exponential Search (Sorted) ---");
        System.out.println("Found 70 at index: " + exponentialSearch(sortedData, target));

        System.out.println("\n--- 6. Hash Table Search (Any Data) ---");
        System.out.println("Found 70 at index: " + hashTableSearch(unsortedData, target));
    }
}