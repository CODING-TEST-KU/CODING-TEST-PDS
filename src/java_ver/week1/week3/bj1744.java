package src.java_ver.week1.week3;

import java.util.*;
import java.io.*;

public class bj1744 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> positive = new ArrayList<>();
        List<Integer> negative = new ArrayList<>();
        int zero = 0;
        int one = 0;

        // 수 저장: 1,0,양수, 음수 따로 나누어 저장
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num > 1) positive.add(num);
            else if (num == 1) one++;
            else if (num == 0) zero++;
            else negative.add(num);
        }

        //양수는 내림차순 정렬
        Collections.sort(positive, Collections.reverseOrder());
        //음수는 오름차순 정렬
        Collections.sort(negative);

        int result = 0;

        //양수 더하기
        /// i+1이 OOI나므로 i가 아닌 i+1을 체크해주어야함
        for (int i = 0; i + 1 < positive.size(); i += 2) {
            result += positive.get(i) * positive.get(i + 1);
        }
        //양수가 홀수개일 경우
        if (positive.size() % 2 == 1) result += positive.get(positive.size() - 1);

        //음수 더하기
        for (int i = 0; i + 1 < negative.size(); i += 2) {
            result += negative.get(i) * negative.get(i + 1);
        }
        //음수가 홀수개일 경우
        //곱해줄 0이 없으면 더하기
        if (zero == 0 && negative.size() % 2 == 1) result += negative.get(negative.size() - 1);


        //1은 그냥 더하기
        result += one;

        System.out.println(result);
    }
}
