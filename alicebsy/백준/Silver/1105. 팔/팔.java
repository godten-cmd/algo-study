import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // 입력값이 있을 때
        if (sc.hasNext()) {
            String L = sc.next();
            String R = sc.next();
            
            int count = 0;
            
            // 두 수의 자릿수가 다르면 무조건 8이 0개인 숫자가 존재
            if (L.length() == R.length()) {
                // 자릿수가 같을 때
                for (int i = 0; i < L.length(); i++) {
                    // 두 숫자가 달라질 때
                    if (L.charAt(i) != R.charAt(i)) {
                        break;
                    }
                    // 두 숫자가 같고, 그 숫자가 8일 때
                    if (L.charAt(i) == '8') {
                        count++;
                    }
                }
            }
            
            System.out.println(count);
        }
        
        sc.close();
    }
}