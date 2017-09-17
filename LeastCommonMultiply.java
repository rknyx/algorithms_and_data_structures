import java.util.Scanner;

public class LeastCommonMultiply {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println((long)a * (long)b / greatestCommonDivisor(a, b));
    }

    private static int greatestCommonDivisor(int a, int b) {
        int big = a > b ? a : b;
        int curr = a > b ? b : a;
        while(true) {
            int res = big % curr;
            if (res == 0) {
                return curr;
            }
            big = curr;
            curr = res;
        }
    }
}
