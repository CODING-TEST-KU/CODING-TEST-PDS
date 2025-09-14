package src.java_ver.week1;

import java.util.*;
import java.io.*;


public class bj10815_BufferedReader {
    static int[] numbers;

    public static void main(String[] args) throws IOException {

        // Scanner scan = new Scanner(System.in);
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb =new StringBuilder();


        int n = Integer.parseInt(br.readLine());
        numbers = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numbers);

        int m = Integer.parseInt(br.readLine());
        int[] targets = new int[m];
        st= new StringTokenizer(br.readLine());

        for (int i = 0; i < m; i++) {
            targets[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < targets.length; i++) {
            sb.append(search(targets[i]));
            if (i != targets.length - 1) sb.append(" ");

        }

        System.out.println(sb);

    }

    private static int search(int target) {
        int start = 0;
        int end = numbers.length - 1;

        while (end >= start) {
            int mid = (start + end) / 2;
            if (numbers[mid] == target) {
                return 1;
            } else if (numbers[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }
        return 0;
    }
}
