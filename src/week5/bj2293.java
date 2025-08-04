package src.week5;

import java.util.*;
import java.io.*;


public class bj2293 {

    /*
    dp[i]: 주어진 동전으로 i를 만들 수 있는 경우의 수
    * */

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] coins = new int[n];
        int[] dp = new int[k + 1];
        dp[0] = 1; // 0원을 만드는 방법 1가지

        //동전 입력받기
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        //dp 채우기
        //**순서 고려하지 않기 위해 동전 기준으로 먼저 loop를 돌려야 한다.
        for (int coin : coins) {
            //모든 coin에 대해 dp[(목적 숫자 -코인 크기)]을 더한다.
            for (int i = 1; i <= k; i++) {
                if (i >= coin) {
                    dp[i] += dp[i - coin];
                }
            }
        }
        System.out.println(dp[k]);

    }
}
