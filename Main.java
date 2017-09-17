import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Scanner;

class Main {
    private static BufferedReader reader = null;

    public static void main(String[] args) throws IOException {
        Solutions.large_fibo_last_digit(args);
    }


    private static int[] intArrayFromInput() throws IOException {
        int length = Integer.parseInt(nextLine());
        String[] parts = nextLine().split(" ");
        closeInput();
        int[] numbers = new int[parts.length];
        for (int i = 0; i < length; ++i) {
            numbers[i] = Integer.parseInt(parts[i]);
        }
        return numbers;
    }

    private static String nextLine() throws IOException {
        if (reader == null) {
            reader = new BufferedReader(new InputStreamReader(System.in));
        }
        return reader.readLine();
    }

    private static void closeInput() throws IOException {
        if (reader != null) {
            reader.close();
        }
    }

    private static void output(Object object) {
        System.out.println(object);
    }

    private static class Algorithms {
        public static long calc_fib_naive(int n) {
            if (n <= 1)
                return n;

            return calc_fib_naive(n - 1) + calc_fib_naive(n - 2);
        }

        public static long calc_fib_fast(int n) {
            long prev_prev = 1;
            long prev = 1;
            long curr = 1;
            if (n == 0) {
                return 0;
            } else if (n < 3) {
                return curr;
            }
            for (int i = 3; i <= n; ++i) {
                curr = prev_prev + prev;
                prev_prev = prev;
                prev = curr;
            }
            return curr;
        }

        public static long calc_big_fib_fast_last_digit(int n) {
            long prev_prev = 1;
            long prev = 1;
            long curr = 1;
            if (n == 0) {
                return 0;
            } else if (n < 3) {
                return curr;
            }
            for (int i = 3; i <= n; ++i) {
                curr = (prev_prev + prev) % 10;
                prev_prev = prev;
                prev = curr;
            }
            return curr;
        }

    }

    private static class Solutions {



        public static void APlusB() throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String str = br.readLine();
            String[] parts = str.split(" ");
            int first = Integer.parseInt(parts[0]);
            int second = Integer.parseInt(parts[1]);
            System.out.println(first + second);
        }

        public static void maxProduct(String[] args) throws IOException {
            int[] numbers = intArrayFromInput();
            int max = 0, res;
            for (int i : numbers) {
                for (int k : numbers) {
                    res = i * k;
                    if (res > max) {
                        max = res;
                    }
                }
            }
            output(max);
        }

        public static void maxProductFast(String[] args) throws IOException {
            int[] numbers = intArrayFromInput();
            long biggest = 0, secondBiggest = 0;
            for (int i : numbers) {
                if (i > biggest) {
                    secondBiggest = biggest;
                    biggest = i;
                } else if (i > secondBiggest) {
                    secondBiggest = i;
                }
            }
            output(secondBiggest * biggest);
        }

        public static void fibo(String[] args) {
            Scanner in = new Scanner(System.in);
            int n = in.nextInt();
            output(Algorithms.calc_fib_fast(n));
        }

        public static void large_fibo_last_digit(String[] args) {
            Scanner in = new Scanner(System.in);
            output(Algorithms.calc_big_fib_fast_last_digit(in.nextInt()));
        }
    }
}