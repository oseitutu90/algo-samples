import java.util.HashSet;
import java.util.Set;

public class SingleNumberProblem {
    public static void main(String[] args) {
        int[] nums = {2,2,1,1,4,4,5,6,6};
        System.out.println(findSingleNumber(nums));
    }

    // find the single number in an array
    public static int findSingleNumber(int [] nums){
        // 1. Create a set to store the numbers
        Set<Integer> set = new HashSet<>();
        // 2. Loop through the array
        for (int i = 0; i < nums.length; i++){
            // 3. If the set contains the number, remove it from the set
            if (set.contains(nums[i])){
                set.remove(nums[i]);
            }
            // 4. If the set does not contain the number, add it to the set
            else {
                set.add(nums[i]);
            }
        }
        // 5. Return the number in the set
        return set.iterator().next();

    }
    
}
