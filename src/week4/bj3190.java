package src.week4;

import java.util.*;
import java.io.*;

public class bj3190 {
    static int n;
    static int[][] map; // 사과는 1
    static Queue<Integer[]> snake = new LinkedList<>();
    static String[][] changeDir;

    //{상, 우, 하 ,좌}
    static int nowDir = 1;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};


    static int count = 0;

    static Integer[] pos = new Integer[]{1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        n = Integer.parseInt(br.readLine());
        map = new int[n + 1][n + 1];

        //사과 위치 저장
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(st.nextToken());
            int col = Integer.parseInt(st.nextToken());
            map[row][col] = 1;
        }

        // 방향 전환 입력받기
        int l = Integer.parseInt(br.readLine());
        changeDir = new String[l][2];
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            changeDir[i][0] = st.nextToken();
            changeDir[i][1] = st.nextToken();
        }

        //(1,1)에서 시작
        snake.add(new Integer[]{1, 1});

        while (true){
            count++;
            //todo  사과 찾았는지 -> 꼬리 회수 유무
            if(!move()){
                break;
            }
            //todo 방향 전환
            checkDir(count);


        }
    }

    static int record = 0;

    public static void checkDir(int count) {
        String stringCount = String.valueOf(count);
        for (int i = record; i < changeDir.length; i++) {
            if (changeDir[i][0].equals(stringCount)) {
                //todo nowDir 변경;
                updateDir(changeDir[i][1]);
                record = i+1;
                break;
            }
        }
    }

    public static void updateDir(String dDir) {
        if (dDir.equals("D")) {
            nowDir = (nowDir + 1) % 4;
        } else {
            nowDir = (nowDir + 3) % 4;
        }
    }

    public static boolean move() {
        int nextRow = pos[0] + dr[nowDir];
        int nextCol = pos[1] + dc[nowDir];

        // 맵 밖을 나간 경우
        if (nextCol < 1 || nextCol > n || nextRow < 1 || nextRow > n) {
            System.out.println(count);
            return false;
        }

        // 뱀의 몸에 닿은 경우
        for (Integer[] body : snake) {
            if (body[0] == nextRow && body[1] == nextCol) {
                System.out.println(count);
                return false;
            }
        }

        //todo 사과 있는지 확인
        if (map[nextRow][nextCol] != 1) {
            snake.poll();
        }else {
            map[nextRow][nextCol] = 0; // 사과 제거
        }

        //머리 전진
        pos = new Integer[]{nextRow, nextCol};
        snake.add(pos);
        return true;
    }

}
