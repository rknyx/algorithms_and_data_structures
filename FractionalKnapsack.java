import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Scanner;

public class FractionalKnapsack {
    private static class Item implements Comparable<Item>{
        public int weight, value;
        public double valuePerKg;
        public Item(int value, int weight, double valuePerKg) {
            this.weight = weight;
            this.value = value;
            this.valuePerKg = valuePerKg;
        }

        public int compareTo(Item other) {
            return Double.compare(other.valuePerKg, this.valuePerKg);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int itemsCount = sc.nextInt();
        int knapsackSize = sc.nextInt();
        Item[] items = new Item[itemsCount];
        int tempWeight, tempValue;
        for (int i = 0; i < itemsCount; ++i) {
            tempValue = sc.nextInt();
            tempWeight = sc.nextInt();
            items[i] = new Item(tempValue, tempWeight, (double)tempValue/(double)tempWeight);
        }

        Arrays.sort(items);
        double howMuchKgToGet, resultValue = 0;
        for (Item item : items) {
            if (knapsackSize == 0) {
                break;
            }
            //сколько его можно взять
            howMuchKgToGet = Math.min(knapsackSize, item.weight);
            knapsackSize -= howMuchKgToGet;
            resultValue += howMuchKgToGet * item.valuePerKg;
        }
        DecimalFormat df = new DecimalFormat("#.####");
        df.setRoundingMode(RoundingMode.HALF_UP);
        System.out.println(df.format(resultValue));
    }
}
