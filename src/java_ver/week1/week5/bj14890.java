package src.java_ver.week1.week5;

import java.util.*;
import java.io.*;

public class bj14890 {

    static int n, l;
    static int[][] map;

    static int count = 0;

    public static void main(String[] args) throws IOException {

        //1. 높이차이가 1인가
        //2. 경사로 밑면을 위한 연속된 길이 존재하는가
        //3. 그 범위는 배열 내부인가
        //4. 경사로는 중복 저장되지 않았는가
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        map = new int[n][n];

        //map 입력받기 (0 ~ n-1)
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        //todo 모든 행 체크
        for (int[] row : map) {
            if (path(row)) count++;
        }

        // todo 모든 열 체크
        for (int i = 0; i < n; i++) {
            int[] col = new int[n];
            for (int j = 0; j < n; j++) {
                col[j] = map[j][i];
            }
            if (path(col)) count++;
        }
        System.out.println(count);

    }

    //todo 경사 체크 메서드
    private static boolean path(int[] load) {
        boolean[] used = new boolean[n];
        // 내리막체크
        for (int i = 0; i < n - 1; i++) {
            // 높이체크
            int gap = load[i] - load[i + 1];
            if (gap == 0) continue; // 높이가 같은 경우
            if (gap < -1 || gap > 1) return false;
            if (gap == 1) {
                // 내리막체크
                for (int k = 1; k < l + 1; k++) {
                    if (i + k > n - 1) return false;// map 범위 체크
                    if (used[i + k]) return false; // 경사로 중복 체크
                    if (load[i + 1] != load[i + k]) return false; // 경사로 밑면 길이 체크
//                    used[i + k] = true;
                }
                for (int k = 1; k < l + 1; k++) {
                    used[i + k] = true;
                }

            }
        }

        // 오르막체크
        for (int i = n - 1; i > 0; i--) {
            // 높이체크
            int gap = load[i - 1] - load[i];
            if (gap == 0) continue; // 높이가 같은 경우
            if (gap == -1) {
                // 오르막체크
                for (int k = 1; k < l + 1; k++) {//1
                    if (i - k < 0) return false;// map 범위 체크
                    if (used[i - k]) return false; // 경사로 중복 체크
                    if (load[i - 1] != load[i - k]) return false; // 경사로 밑면 길이 체크
//                    used[i - k] = true; 중간에 끊긴 경사로를 처리하지 못함
                }
                for (int k = 1; k < l + 1; k++) {
                    used[i - k] = true;
                }

            }
        }
        return true;
    }
}
