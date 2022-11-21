public class MinimumBribe {
    public static void main(String[] args) {
        int[] q = {2, 1, 5, 3, 4};
        System.out.println(minimumBribe(q));
    }

    public static int minimumBribe(int[] q) {
        int bribes = 0;
        for (int i = 0; i < q.length; i++) {
            if (q[i] - (i + 1) > 2) {
                System.out.println("Too chaotic");
                return 0;
            }
            for (int j = Math.max(0, q[i] - 2); j < i; j++) {
                if (q[j] > q[i]) {
                    bribes++;
                }
            }
        }
        System.out.println(bribes);
        return bribes;
    }
}
