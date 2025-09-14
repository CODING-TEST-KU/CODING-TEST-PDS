package src.java_ver.week1;

import java.util.Scanner;

public class bj11651 {
    //bubble 정렬 버젼
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        int tempx, tempy;

        for (int i = 0; i < n; i++) {
            x[i] = scan.nextInt();
            y[i] = scan.nextInt();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (y[j] > y[j + 1]) {
                    tempx = x[j];
                    tempy = y[j];
                    x[j] = x[j + 1];
                    y[j] = y[j + 1];
                    x[j + 1] = tempx;
                    y[j + 1] = tempy;
                } else if (y[j] == y[j + 1] && x[j] > x[j + 1]) {
                    tempx = x[j];
                    tempy = y[j];
                    x[j] = x[j + 1];
                    y[j] = y[j + 1];
                    x[j + 1] = tempx;
                    y[j + 1] = tempy;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.println(x[i]+" "+y[i]);
        }
    }
}
