package src.week1;

import java.util.*;

public class bj10815 {
    static int[] numbers;

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = scan.nextInt();
        }

        Arrays.sort(numbers);

        int m = scan.nextInt();
        int[] targets = new int[m];
        for (int i = 0; i < m; i++) {
            targets[i] = scan.nextInt();
        }

        // 결과 출력
        for (int i = 0; i < targets.length; i++) {
            System.out.print(search(targets[i]));
            if (i != targets.length - 1) System.out.print(" ");
        }
    }

    private static int search(int target) {
        int start = 0;
        int end = numbers.length - 1;

        while (end >= start) {
            int mid = (start + end) / 2;
            if (numbers[mid] == target) {
                return 1;
            } else if (numbers[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return 0;
    }
}
