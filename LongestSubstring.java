import java.util.HashSet;
import java.util.Set;

public class LongestSubstring {
    public static void main(String[] args) {
        String s = "abcabcbb";
        System.out.println(lengthOfLongestSubstring(s)==3);
    }
    public static int lengthOfLongestSubstring(String s){
            // 1. Create a set to store the characters
        Set<Character> set = new HashSet<>();
            // 2. Create two pointers to store the start and end of the substring
        int firstLetterIndex = 0, LastLetterIndex = 0;
            // 3. Create a variable to store the length of the longest substring
        int max = 0;
            // 4. Loop through the string
        while (firstLetterIndex < s.length() && LastLetterIndex < s.length()){
            // 5. If the set does not contain the character at j, add it to the set
            if (!set.contains(s.charAt(LastLetterIndex))){
                set.add(s.charAt(LastLetterIndex));
                j++;
                // 6. Update the max length
                max = Math.max(max, LastLetterIndex - firstLetterIndex);// 7. If the set contains the character at j, remove the character at i from the set
            }
            // 7. If the set contains the character at j, remove the character at i
            else {
                set.remove(s.charAt(firstLetterIndex++));
            }
        }
        return max;
    }
}
