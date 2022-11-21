class FindTheMissingNumber {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 10};
        System.out.println(findMissingNumber(arr)==9);
    }
    public static int findMissingNumber(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        int n = nums.length + 1; // n is the length of the array + 1
        return n * (n + 1) / 2 - sum; // Gauss' formula
    }
   
}