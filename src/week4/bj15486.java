package src.week4;

import java.util.*;
import java.io.*;


public class bj15486 {

    static int[][] schedule;
    static int[] dp; //dp[i]: i번째 날까지 벌 수 있는 최대 수익


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        schedule = new int[n + 2][2];
        dp = new int[n + 2];

        // 스케줄 입력받기
        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            schedule[i][0] = Integer.parseInt(st.nextToken());
            schedule[i][1] = Integer.parseInt(st.nextToken());
        }

        //dp 채우기 : 일별 최대 수익 계산
        for (int i = 1; i < n + 1; i++) {
            dp[i]=Math.max(dp[i],dp[i-1]);///이전 날짜의 최대수익 유지***
            int dur=schedule[i][0];

            //i + dur - 1: 상담이 끝나는 날
            //상담이 끝나는 날은 근무일 범위내에 있어야함
            if(i+dur-1<=n)dp[i+dur]=Math.max(dp[i+dur],dp[i]+schedule[i][1]);
        }

        // 마지막 날까지의 최대 수익 구하기(최종 스캔하여 dp중 최댓값 출력)
        int max = 0;
        for (int i = 1; i <= n + 1; i++) {
            max = Math.max(max, dp[i]);
        }

        System.out.println(max);
    }
}
