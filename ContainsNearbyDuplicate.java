import java.util.HashSet;
import java.util.Set;

public class ContainsNearbyDuplicate {
    public static void main(String[] args) {
        
    }
    // find a the nearby dupicate number in an array
    public static int findNearbyDuplicate(int[] nums){
        // 1. Create a set to store the numbers
        Set<Integer> set = new HashSet<>();
        // 2. Loop through the array
        for (int i = 0; i < nums.length; i++){
            // 3. If the set contains the number, return the number
            if (set.contains(nums[i])){
                return nums[i];
            }
            // 4. If the set does not contain the number, add it to the set
            else {
                set.add(nums[i]);
            }
        }
        // 5. If there is no duplicate number, return -1
        return -1;
    }
}
