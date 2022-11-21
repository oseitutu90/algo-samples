public class balance {
    // find number to balance in string of brackets
    public static void main(String[] args) {
        String s = "((()))";
        String s1 = "(()()())";
        System.out.println(isBalanced(s));
        System.out.println(isBalanced(s1));
    }

    public static int isBalanced(String s) {
        int balance = 0;
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                balance++;
            } else if(s.charAt(i) == ')'){
                balance--;
            }
        }
        return Math.abs(balance);
    }
}