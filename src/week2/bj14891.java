package src.week2;

import java.util.*;
import java.io.*;

public class bj14891 {

    //왜 안되는지 모르겠는 코드

    private static int[][] coqwheel = new int[4][8];
    //index:톱니바퀴번호, value:오른쪽 위치 톱니바퀴(왼쪽은 (오른쪽 +4)%8)
    private static int[] pointer = new int[]{2, 2, 2, 2};
    private static boolean[] connection;

    //회전방향{반시계, 안씀, 시계}
    private static int[] dr = {1, 0, 7};
    //이웃한 톱니바퀴 리버스 회전방향
    private static int[] reverseDr = {7, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //톱니바퀴 입력받기
        for (int f = 0; f < 4; f++) {
            String line = br.readLine();
            for (int i = 0; i < 8; i++) {
                coqwheel[f][i] = line.charAt(i) - '0';
            }
        }

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int wheelNum = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());
            //todo 어느 point가 이어져있는지 반환하는 메서드 findConnection
            findConnection(wheelNum);
            //todo 시작 톱니바퀴를 기준으로 연쇄적으로 회전 rotate()
            rotate(wheelNum, dir);
            for (int ii=0;ii<4;ii++) {
                System.out.print(pointer[ii]);
                System.out.print(connection[ii]);
            }
            System.out.println();
        }


        //점수 계산
        System.out.println(score());

    }

    public static void findConnection(int wheelNum) {
        int nowWheel = wheelNum;
        connection = new boolean[4];
        //오른쪽 연결검사
        while (nowWheel < 3) {
            int leftWheel = coqwheel[nowWheel][pointer[nowWheel]];
            int rightWheel = coqwheel[nowWheel + 1][(pointer[nowWheel + 1] + 4) % 8];
            if (leftWheel != rightWheel) {
                connection[nowWheel] = true;
            } else {
                break;
            }
            nowWheel++;
        }

        //왼쪽 연결검사
        nowWheel = wheelNum;
        while (nowWheel > 0) {
            int rightWheel = coqwheel[nowWheel][(pointer[nowWheel] + 4) % 8];
            int leftWheel = coqwheel[nowWheel - 1][pointer[nowWheel - 1]];
            if (leftWheel != rightWheel) {
                connection[nowWheel - 1] = true;
            } else {
                break;
            }
            nowWheel--;
        }

    }

    public static void rotate(int wheelNum, int dir) {
        for (int i = 0; i < 4; i++) {
            if (i == wheelNum) {
                pointer[i] = (pointer[i] + dr[dir + 1]) % 8;
            } else if ((i + wheelNum) % 2 == 0 && connection[i]) {
                pointer[i] = (pointer[i] + dr[dir + 1]) % 8;
            } else if ((i + wheelNum) % 2 == 1 && connection[i]) {
                pointer[i] = (pointer[i] + reverseDr[dir + 1]) % 8;
            }

        }
    }
//    //회전방향{반시계, 안씀, 시계}
//    private static int[] dr = {1, 0, 7};
//    //이웃한 톱니바퀴 리버스 회전방향
//    private static int[] reverseDr = {7, 0, 1};

    public static int score() {
        int score = 0;
        for (int i = 0; i < 4; i++) {
            int top = coqwheel[i][(pointer[i] + 6) % 8];
            if (top == 1) {
                score += (1 << i);
            }
        }
        return score;
    }

}
