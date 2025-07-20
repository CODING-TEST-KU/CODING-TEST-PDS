package src.week3;

import java.util.*;
import java.io.*;

public class bj14499 {

    static int[][] map;
    //상(0),동(1),서(2),북(3),남(4),하(5)
    static int[] dice = {0,0,0,0,0,0};

    //동,서,북,남
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        // 지도 입력받기
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        //주사위 굴리기
        st = new StringTokenizer(br.readLine());
        //동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
        for (int i = 0; i < k; i++) {
            int diceDir = Integer.parseInt(st.nextToken());
            //todo bound 검사
            int nx = x + dx[diceDir-1];
            int ny = y + dy[diceDir-1];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                x = nx;
                y = ny;
                move(diceDir,x,y);
            }
        }
    }

    static void move(int diceDir,int x,int y) {

        //굴리는 방향과 무관한 면이 복사되도록 clone을 사용해야함
        int[] nextDice = dice.clone();
        //상(0),동(1),서(2),북(3),남(4),하(5)
        switch (diceDir) {
            //동(동->하,하->서,서->상,상->동)
            case 1:
                nextDice[5] = dice[1];
                nextDice[2] = dice[5];
                nextDice[0] = dice[2];
                nextDice[1] = dice[0];
                break;

            //서(서->하,하->동,동->상,상->서)
            case 2:
                nextDice[5] = dice[2];
                nextDice[1] = dice[5];
                nextDice[0] = dice[1];
                nextDice[2] = dice[0];
                break;

            //북(북->하,하->남,남->상,상->북)
            case 3:
                nextDice[5] = dice[3];
                nextDice[4] = dice[5];
                nextDice[0] = dice[4];
                nextDice[3] = dice[0];
                break;

            //남(남->하,하->북,북->상,상->남)
            case 4:
                nextDice[5] = dice[4];
                nextDice[3] = dice[5];
                nextDice[0] = dice[3];
                nextDice[4] = dice[0];
                break;

        }

        dice = nextDice;

        // 지도와 주사위 바닥면 값 복사
        if (map[x][y] == 0) {
            map[x][y] = dice[5];
        } else {
            dice[5] = map[x][y];
            map[x][y] = 0;
        }

        System.out.println(dice[0]);
    }
}
