package src.java_ver.week1.week8;

import java.util.*;

public class 보석쇼핑 {

    public int[] solution(String[] gems) {
        // 1) 전체 보석 종류 수 k
        Set<String> types = new HashSet<>(Arrays.asList(gems));
        int k = types.size();

        //2) 투포인터 +빈도 맵
        Map<String, Integer> count = new HashMap<>();
        int left = 0, right = 0;
        int bestL = 0, bestR = gems.length - 1;
        int formed = 0;// 현재 선반이 포함한 서로 다른 종류 수

        while (true) {
            if (formed < k) {
                if (right == gems.length) break;// 더 확장
                String g = gems[right++];
                int c = count.getOrDefault(g, 0);
                if (c == 0) formed++;
                count.put(g, c + 1);
            } else {
                int currLen = right - left;
                int bestLen = bestR - bestL + 1;
                if (currLen < bestLen || (currLen == bestLen && left < bestL)) {
                    bestL = left;
                    bestR = right - 1;
                }
                String g = gems[left++];
                int c = count.get(g) - 1;
                if (c == 0) {
                    count.remove(g);
                    formed--;
                } else {
                    count.put(g, c);
                }
            }
        }

        return new int[]{bestL + 1, bestR + 1};
    }
}
