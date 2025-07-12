package src.week2;

import java.util.*;
import java.io.*;

public class bj14891_ver2 {

    private static int[][] coqwheel = new int[4][8];
    //index:톱니바퀴번호, value:오른쪽 위치 톱니바퀴(왼쪽은 (오른쪽 +4)%8)
    private static int[] pointer = new int[]{2, 2, 2, 2};
    private static boolean[] connection;


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
        int[] dirArr = new int[4];        // 각 기어의 최종 회전 방향
        dirArr[wheelNum] = dir;           // 시작 기어는 무조건 회전

        // 오른쪽 전파
        for (int i = wheelNum; i < 3 && connection[i]; i++)
            dirArr[i + 1] = -dirArr[i];

        // 왼쪽 전파
        for (int i = wheelNum; i > 0 && connection[i - 1]; i--)
            dirArr[i - 1] = -dirArr[i];

        // pointer 갱신
        for (int i = 0; i < 4; i++) {
            if (dirArr[i] == 0) continue;          // 회전 안 함
            pointer[i] = (pointer[i] + (dirArr[i] == 1 ? 7 : 1)) % 8;
        }
    }

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
