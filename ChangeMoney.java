import java.util.Scanner;

public class ChangeMoney {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = sc.nextInt();
        int totalCoinsCount = 0;
        int[] coinsRates = new int[]{10, 5, 1};
        for (int rate : coinsRates) {
            int howMany = sum / rate;
            sum -= (howMany * rate);
            totalCoinsCount += howMany;
        }
        System.out.println(totalCoinsCount);
    }
}
