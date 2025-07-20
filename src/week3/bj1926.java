package src.week3;

import java.util.*;
import java.io.*;

public class bj1926 {

    static int[][] picture;
    static boolean[][] visited;
    static int n;
    static int m;

    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    static int count = 0;
    static int maxSize = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        picture = new int[n][m];
        visited =new boolean[n][m];

        // 그림 입력받기
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                picture[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (picture[i][j] == 1 && !visited[i][j]) {
                    bfs(i, j);
                }
            }
        }

        System.out.println(count);
        System.out.println(maxSize);

    }

    static void bfs(int x, int y) {
        Queue<Integer[]> queue = new LinkedList<>();
        queue.offer(new Integer[]{x, y});
        visited[x][y] = true;
        int recordSize = 1;
        count++;

        while (!queue.isEmpty()) {
            Integer[] pos = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nextX = pos[0] + dx[i];
                int nextY = pos[1] + dy[i];
                if (nextX < 0 || nextX >= n || nextY < 0 || nextY >= m) continue;
                if (picture[nextX][nextY] == 1 && !visited[nextX][nextY]) {
                    queue.offer(new Integer[]{nextX, nextY});
                    visited[nextX][nextY]=true;
                    recordSize++;
                }
            }
        }
        if (maxSize < recordSize) maxSize = recordSize;
    }
}
