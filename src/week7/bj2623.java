package src.week7;

import java.io.*;
import java.util.*;

public class bj2623 {

    static int n, m;
    static List<Integer>[] graph;
    static int[] indegree;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        indegree = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        //그래프 입력 받기
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int prev = Integer.parseInt(st.nextToken());
            for (int j = 1; j < k; j++) {
                int next = Integer.parseInt(st.nextToken());
                graph[prev].add(next);
                indegree[next]++;
                prev = next;
            }
        }

        //base
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            if (indegree[i] == 0) q.add(i);
        }

        //step
        List<Integer> result = new ArrayList<>();
        while (!q.isEmpty()) {
            int cur=q.poll();
            result.add(cur);
            for(int nxt:graph[cur]){
                indegree[nxt]--;
                if(indegree[nxt]==0)q.add(nxt);
            }
        }
        if (result.size() != n) {
            System.out.println(0);
        } else {
            for (int x : result) System.out.println(x);
        }
    }


}
