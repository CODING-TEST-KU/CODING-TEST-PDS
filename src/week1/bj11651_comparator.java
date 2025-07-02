package src.week1;

import java.util.Arrays;
import java.util.Scanner;

public class bj11651_comparator {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[][] point = new int[n][2];//n개의 좌표 (x,y)

        for (int i = 0; i < n; i++) {
            point[i][0] = scan.nextInt();
            point[i][1] = scan.nextInt();
        }

        Arrays.sort(point, (a, b) -> {
            if (a[1] != b[1]) {
                return a[1] - b[1];
            }
            return a[0] - b[0];
        });

        for (int i = 0; i < n; i++) {
            System.out.println(point[i][0] + " " + point[i][1]);
        }
    }
}
