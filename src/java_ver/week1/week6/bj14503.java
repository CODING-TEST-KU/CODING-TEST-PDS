package src.java_ver.week1.week6;

import java.util.*;
import java.io.*;

public class bj14503 {

    static int n, m, r, c, d;
    static int count=0;
    static int[][] map;
    //{북, 동, 남, 서}
    static int[] dc = {0, 1, 0, -1};
    static int[] dr = {-1, 0, 1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        // map 입력 받기
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        while (true) {
            // 현재 칸 청소 0->-1
            if (map[r][c] == 0) {
                map[r][c] = -1;
                count++;
            }

            if (checkDirty(r, c)) {
                //청소할 칸 있는 경우
                for (int i = 0; i < 4; i++) {
                    //반시계방향으로 회전
                    d = (d + 3) % 4;
                    int nr =r+ dr[d];
                    int nc =c+ dc[d];
                    if(map[nr][nc]==0){
                        r=nr;
                        c=nc;
                        break;
                    }
                }
            } else {
                //청소할 칸 없는 경우
                int backDir = (d + 2) % 4;
                int backR = r + dr[backDir];
                int backC = c + dc[backDir];
                if (map[backR][backC] == 1) {
                    break;
                } else {
                    r = backR;
                    c = backC;
                }
            }
        }
        System.out.println(count);
    }

    static boolean checkDirty(int nr, int nc) {
        for (int i = 0; i < 4; i++) {
            if (map[nr + dr[i]][nc + dc[i]] == 0) return true;
        }
        return false;
    }

}
