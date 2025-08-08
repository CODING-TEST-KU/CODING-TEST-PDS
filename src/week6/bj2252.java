package src.week6;

import java.util.*;
import java.io.*;

public class bj2252 {

    static int n, m;
    static List<Integer>[] graph;
    static int[] indegree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        indegree = new int[n + 1];
        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }


        //그래프 입력 받으며 indegree값 갱신
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int front = Integer.parseInt(st.nextToken());
            int back = Integer.parseInt(st.nextToken());
            graph[front].add(back);
            indegree[back]++;
        }

        //indegree가 0인 경우 큐에 넣기
        Queue<Integer> zeroIndegree = new ArrayDeque<>();
        for (int i = 1; i <= n ; i++) {
            if (indegree[i] == 0) zeroIndegree.add(i);
        }

        // queue 가 빌때까지
        while (!zeroIndegree.isEmpty()) {
            int now = zeroIndegree.poll();
            for (int next : graph[now]) { //노드에 연결된 다른 노드들 indegree 감소 및 0인 경우 queue에 넣기
                indegree[next]--;
                if (indegree[next] == 0) zeroIndegree.add(next);
            }
            System.out.print(now + " ");
        }

    }
}
