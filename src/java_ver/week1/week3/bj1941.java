package src.java_ver.week1.week3;

import java.util.*;
import java.io.*;

public class bj1941 {

    static char[][] classroom= new char[5][5];
    static int ans;
    static boolean[] visited;
    static int[] checked = new int[7];

    private static int[] dx = {0, 0, -1, 1};
    private static int[] dy = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //교실 구성 입력받기
        for (int i = 0; i < 5; i++) {
            String line = br.readLine();
            for (int j = 0; j < 5; j++) {
                classroom[i][j] = line.charAt(j);
            }
        }

        //탐색 시작
        combination(0, 0, 0);
        System.out.println(ans);

    }

    static void combination(int count, int start, int countS) {
        if (count - countS > 3) {
            return;
        }
        if (count == 7) {
            visited = new boolean[7];
            bfs(checked[0] / 5, checked[0] % 5);//첫 위치[0]부터 탐색 시작
            return;
        }

        for (int i = start; i < 25; i++) {
            int x = i / 5;
            int y = i % 5;
            checked[count] = i;
            combination(count + 1, i + 1, (classroom[x][y] == 'S' ? countS + 1 : countS));
        }
    }

    static void bfs(int i, int j) {
        int num = 1;
        visited[0] = true;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{i, j});
        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int x = pos[0];
            int y = pos[1];
            for (int dir = 0; dir < 4; dir++) {
                int nx = x + dx[dir];
                int ny = y + dy[dir];
                if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5) continue;// 배열 범위 확인
                int next = 5 * nx + ny;
                for (int k = 0; k < 7; k++) {
                    if (!visited[k] && checked[k] == next) {
                        visited[k] = true;
                        num++;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
        }

        //총 7명의 공주가 모였다면 정답 개수 ++
        if (num == 7) ans++;
    }

}
