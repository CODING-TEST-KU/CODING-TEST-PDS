package src.java_ver.week1.week6;

import java.util.*;
import java.io.*;


public class bj1238 {
    static class Edge {
        int to, w;

        Edge(int to, int w) {
            this.to = to;
            this.w = w;
        }
    }

    static final int INF = 1_000_000_000;

    static int n, m, x;
    static List<Edge>[] g, rg;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());//노드 수
        m = Integer.parseInt(st.nextToken());//간선 수
        x = Integer.parseInt(st.nextToken());//목적 학생

        g = new ArrayList[n + 1];
        rg = new ArrayList[n + 1];

        //그래프 초기화
        for (int i = 1; i <= n; i++) {
            g[i] = new ArrayList<>();
            rg[i] = new ArrayList<>();
        }

        // 간선 입력 받기
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int t = Integer.parseInt(st.nextToken());
            g[a].add(new Edge(b, t)); //원본 그래프 저장
            rg[b].add(new Edge(a, t));// 간선의 방향을 뒤집은 그래프
        }

        int[] distFromX = dijkstra(g, x);
        int[] distToX = dijkstra(rg, x);

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int totalW = distFromX[i] + distToX[i];
            if (totalW > ans) ans = totalW;
        }
        System.out.println(ans);

    }

    static int[] dijkstra(List<Edge>[] graph, int start) {
        int[] dist = new int[n + 1];
        Arrays.fill(dist, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        dist[start] = 0;
        pq.offer(new int[]{start, 0});

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0];
            int d = cur[1];
            if (d != dist[u]) continue;
            for(Edge e:graph[u]){
                int v=e.to;
                int nd =d+e.w;
                if(nd<dist[v]){
                    dist[v]=nd;
                    pq.offer(new int[]{v,nd});
                }
            }
        }
        return dist;
    }
}
