package src.week2;

import java.util.*;
import java.io.*;

public class bj1260 {

    private static List<Integer>[] graph;
    private static boolean[] visited;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];

        // ArrayList[] 사용시에는 각 배열마다 초기화를 해주어야한다.
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }


        //graph 입력 받기
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            graph[v1].add(v2);
            graph[v2].add(v1);
        }

        /// !! 번호가 작은 것부터 탐색해야하므로 오름차순으로 정렬해주어야한다.
        for (int i = 1; i < n + 1; i++) {
            Collections.sort(graph[i]);
        }

        visited = new boolean[n + 1];
        dfs(v);
        System.out.println();

        visited = new boolean[n + 1];
        bfs(v);
        System.out.println();

    }

    public static void dfs(int now) {
        //재귀
        visited[now] = true;
        System.out.print(now + " ");

        for (int next : graph[now]) {
            if (!visited[next]) dfs(next);
        }
    }

    public static void bfs(int start) {
        //while
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {
            int now = queue.poll();
            System.out.print(now + " ");

            for (int next : graph[now]) {
                if (!visited[next]) {
                    queue.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}
