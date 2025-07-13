package src.week2;

import java.util.*;
import java.io.*;

public class bj2178 {

    private static int[][] map;
    private static Queue<int[]> queue = new LinkedList<>();
    private static boolean[][] visited;

    //2차원 배열 상하좌우방향
    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    //목표지점 위치 저장
    private static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        visited = new boolean[n][m];
        // map 입력받기
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }

        queue.add(new int[]{0, 0, 1});
        visited[0][0] = true;
        bfs();
    }

    private static void bfs() {

        while (!queue.isEmpty()) {
            //방문 노드 poll
            int[] now = queue.poll();
            int x = now[0];
            int y = now[1];
            int count = now[2];

            if (x == n - 1 && y == m - 1) {
                System.out.println(count);
                return;
            }

            //주변노드 queue에 넣기
            for (int f = 0; f < 4; f++) {
                int nx = x + dx[f];
                int ny = y + dy[f];
                if (nx >= 0 && ny >= 0 && nx < n && ny < m && map[nx][ny] == 1 && visited[nx][ny] == false) {
                    queue.add(new int[]{nx, ny, count + 1});
                    visited[nx][ny] = true;
                }
            }
        }
    }
}
