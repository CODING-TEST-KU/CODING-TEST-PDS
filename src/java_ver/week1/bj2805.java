package src.java_ver.week1;

import java.util.*;

public class bj2805 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();
        int[] trees = new int[n];
        int end = 0;

        // 나무 길이 입력받으면서 가장 긴 나무 찾기(end에 저장)
        for (int i = 0; i < n; i++) {
            trees[i] = scan.nextInt();
            if (end < trees[i]) end = trees[i];
        }

        int start = 0;
        int result = 0;

        while (start <= end) {
            int half = (start + end) / 2;
            long sum = 0;
            for (int tree : trees) {
                if (tree > half) sum += tree - half;
            }
            if (sum < m) {
                end = half - 1;
            } else {
                result=half;
                start = half + 1;
            }
        }
        System.out.println(result);
    }
}
