import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Algorithms2 {

    // --- HUFFMAN CODING COMPONENTS ---
    static class HuffmanNode implements Comparable<HuffmanNode> {
        int freq;
        char c;
        HuffmanNode left, right;

        public int compareTo(HuffmanNode node) {
            return this.freq - node.freq;
        }
    }

    public static void runHuffman(String text) {
        System.out.println("--- Huffman Coding ---");
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : text.toCharArray()) freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);

        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>();
        freqMap.forEach((character, frequency) -> {
            HuffmanNode node = new HuffmanNode();
            node.c = character;
            node.freq = frequency;
            pq.add(node);
        });

        while (pq.size() > 1) {
            HuffmanNode x = pq.poll();
            HuffmanNode y = pq.poll();
            HuffmanNode parent = new HuffmanNode();
            parent.freq = x.freq + y.freq;
            parent.c = '\0'; // Internal node
            parent.left = x;
            parent.right = y;
            pq.add(parent);
        }

        Map<Character, String> codes = new HashMap<>();
        generateCodes(pq.peek(), "", codes);
        
        System.out.println("Input: " + text);
        codes.forEach((k, v) -> System.out.println("'" + k + "': " + v));
        System.out.println();
    }

    private static void generateCodes(HuffmanNode node, String s, Map<Character, String> codes) {
        if (node.left == null && node.right == null && node.c != '\0') {
            codes.put(node.c, s);
            return;
        }
        if (node.left != null) generateCodes(node.left, s + "0", codes);
        if (node.right != null) generateCodes(node.right, s + "1", codes);
    }

    // --- TSP APPROXIMATION (NEAREST NEIGHBOR) ---
    public static void runTSP(double[][] matrix) {
        System.out.println("--- TSP Nearest Neighbor ---");
        int n = matrix.length;
        boolean[] visited = new boolean[n];
        List<Integer> path = new ArrayList<>();

        int current = 0; // Starting at the first city
        path.add(current);
        visited[current] = true;

        for (int i = 0; i < n - 1; i++) {
            int nearest = -1;
            double min = Double.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                if (!visited[j] && matrix[current][j] < min) {
                    min = matrix[current][j];
                    nearest = j;
                }
            }
            visited[nearest] = true;
            path.add(nearest);
            current = nearest;
        }
        path.add(0); // Return to start
        System.out.println("Route: " + path);
    }

    // --- MAIN METHOD ---
    public static void main(String[] args) {
        // 1. Huffman Example
        runHuffman("hello huffman");

        // 2. TSP Example (Distance Matrix)
        // Cities: 0, 1, 2, 3
        double[][] distances = {
            {0, 10, 15, 20},
            {10, 0, 35, 25},
            {15, 35, 0, 30},
            {20, 25, 30, 0}
        };
        runTSP(distances);
    }
}