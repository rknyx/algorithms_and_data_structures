import java.math.BigInteger;
import java.util.Scanner;

public class HugeFibonacciNumberModulo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger fibNum = sc.nextBigInteger();
        int divisor = sc.nextInt();
        int periodLength = calc_pizano_period(divisor);
        long similarSeqNumber = fibNum.mod(BigInteger.valueOf(periodLength)).intValue();
        BigInteger newFibNumber = calc_fib_fast(similarSeqNumber);
        System.out.println(newFibNumber.mod(BigInteger.valueOf(divisor)));
    }



    public static BigInteger calc_fib_fast(long n) {
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        BigInteger c = BigInteger.ONE;
        if (n == 0) {
            return BigInteger.ZERO;
        } else if (n < 2) {
            return BigInteger.valueOf(n);
        }
        for (int i = 2; i <= n; ++i) {
            c = a.add(b);
            a = b;
            b = c;
        }
        return c;
    }

    public static int calc_pizano_period(int m) {
        long a = 0, b = 1, c;
        for (int i = 2;; ++i) {
            c = a + b % m;
            if (i == Integer.MAX_VALUE) {
                throw new RuntimeException("Seems that we reach max int but still don't find pizano seq length");
            }
            a = b; b = c;
            if (a % m == 0 && b % m == 1) {
                return i - 1;
            }
        }
    }
}
