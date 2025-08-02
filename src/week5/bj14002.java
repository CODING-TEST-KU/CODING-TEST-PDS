package src.week5;

import java.util.*;
import java.io.*;


public class bj14002 {

    /*
     * dp: 해당 숫자를 마지막으로 하는 최장 수열의 길이
     * 점화식: dp[i]=자신보다 작은 수가 나올때까지 서치
     *
     *
     * */

    static int[] dp; //
    static int[] nums;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        dp = new int[n];
        nums = new int[n];
        Arrays.fill(dp, 1);
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        //모든 n개의 숫자에 대해 스캔
        for (int i = 0; i < n; i++) {
            //해당 숫자 이전의 숫자에 대해 스캔
            for (int j = 0; j < i; j++) {
                if (dp[j] + 1 > dp[i] && nums[j] < nums[i]) {
                    dp[i] = dp[j] + 1;
                }
            }
        }

        int max_index = 0;

        for (int i = 0; i < n; i++) {
            if (dp[max_index] < dp[i]) {
                max_index = i;
            }
        }

        System.out.println(dp[max_index]);

        Stack<Integer> answer = new Stack<>();
        answer.push(nums[max_index]);

        // 역순으로 스캔하며 문자열 추적
        for (int i = max_index; i >= 0; i--) {
            if (nums[i] < nums[max_index] && dp[i] + 1 == dp[max_index]) {
                max_index = i;
                answer.push(nums[max_index]);
            }
        }

        while(!answer.isEmpty()){
            System.out.print(answer.pop()+" ");
        }


    }
}
