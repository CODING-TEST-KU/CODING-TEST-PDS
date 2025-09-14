package src.java_ver.week1.week2;

import java.io.*;
import java.util.*;

public class bj1058_dfs {
    static int n;
    static char[][] map;
    static boolean[] visited;
    static Set<Integer> friendSet;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new char[n][n];

        for (int i = 0; i < n; i++) {
            map[i] = br.readLine().toCharArray();
        }

        int max = 0;

        for (int i = 0; i < n; i++) {
            visited = new boolean[n];
            friendSet = new HashSet<>();
            dfs(i, i, 0);
            max = Math.max(max, friendSet.size());
        }

        System.out.println(max);
    }

    private static void dfs(int start, int current, int depth) {
        if (depth > 2) return;

        for (int i = 0; i < n; i++) {
            if (i == start) continue; // 자기 자신은 포함하지 않음
            if (map[current][i] == 'Y' && !visited[i]) {
                visited[i] = true;
                if (depth < 2) {
                    friendSet.add(i);
                    dfs(start, i, depth + 1);
                }
            }
        }
    }
}
