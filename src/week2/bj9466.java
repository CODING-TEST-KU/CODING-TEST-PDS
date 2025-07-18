package src.week2;

import java.util.*;
import java.io.*;

public class bj9466 {

    private static int[] numbers;
    private static boolean[] visited, done;
    private static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {

            int n = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());

            numbers = new int[n + 1];
            visited = new boolean[n + 1];
            done = new boolean[n + 1];
//            selected = new boolean[n + 1];
            count   = 0;

            for (int j = 1; j < n + 1; j++) {
                numbers[j] = Integer.parseInt(st.nextToken());
            }

            for (int j = 1; j <= n; j++) {
                if (!visited[j]) team(j);
            }

            System.out.println(n-count);
        }
    }

    private static void team(int now) {
        visited[now] = true;
        int next = numbers[now];
        if (!done[next] && !visited[next]) {
            team(next);
        } else if (!done[next] && visited[next]) {//자기자신과 팀인경우 next==now가 되어 포함
            //사이클 발견한 경우
            int temp = next;
            while (temp != now) {
                // 어차피 사이클 구조이므로 한바퀴 더 돌아
                count++;
                temp = numbers[temp];
            }
            count++;
        }
        done[now] = true;
    }
}
