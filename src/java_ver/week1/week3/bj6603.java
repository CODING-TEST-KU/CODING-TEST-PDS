package src.java_ver.week1.week3;

import java.util.*;
import java.io.*;

public class bj6603 {

    public static int n;
    public static int[] lotto;
    public static boolean[] visited;
    public static List<Integer> numList;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        lotto = new int[6];
        visited = new boolean[n];

        while (n != 0) {
            numList = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                numList.add(Integer.parseInt(st.nextToken()));
            }

            dfs(0,0);

            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            System.out.println();
        }
    }

    public static void dfs(int depth, int start) {
        if (depth == 6) {
            for (int num : lotto) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        } else if (depth < 6) {
            for (int k = start; k < n; k++) {
                    lotto[depth] = numList.get(k);
                    dfs(depth+1,k+1);
            }
        }
    }
}
