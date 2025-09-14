package src.java_ver.week1.week4;

import java.io.*;

public class bj9095 {
    //dp[i]: i의 수를 만드는 경우의 수
    static int[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            doDP(num);
        }
    }

    public static void doDP(int num) {

        dp = new int[num + 4];//num+1 크기로 생성 시 num이 1이나 2일경우 outOfBound가 발생함
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        // dp 수 채우기
        for (int i = 4; i < num + 1; i++) {
            dp[i] += dp[i - 1] + dp[i - 2] + dp[i - 3];
        }
        //출력
        System.out.println(dp[num]);
    }
}
