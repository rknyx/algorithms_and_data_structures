import java.io.IOException;
import java.util.Scanner;

public class GreatestCommonDivisor {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int big = a > b ? a : b;
        int curr = a > b ? b : a;
        while(true) {
            int res = big % curr;
            if (res == 0) {
                output(curr);
                return;
            }
            big = curr;
            curr = res;
        }
    }

    private static void output(Object object) {
        System.out.println(object);
    }
}