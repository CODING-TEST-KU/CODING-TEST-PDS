package src.java_ver.week1.week8;

import java.util.*;

public class 수식최대화 {

    public long solution(String expression) {

        List<Long> baseNums = new ArrayList<>();
        List<Character> baseOps = new ArrayList<>();
        parser(expression, baseNums, baseOps);

        char[][] orders = {
                {'+', '-', '*'},
                {'+', '*', '-'},
                {'-', '+', '*'},
                {'-', '*', '+'},
                {'*', '+', '-'},
                {'*', '-', '+'}
        };

        long answer = 0;
        for (char[] order : orders) {
            List<Long> nums = new ArrayList<>(baseNums);
            List<Character> ops = new ArrayList<>(baseOps);

            for (char op : order) {
                for (int i = 0; i < ops.size(); ) {
                    if (ops.get(i) == op) {
                        long a = nums.get(i);
                        long b = nums.get(i + 1);
                        long r = calc(a, b, op);
                        nums.set(i, r);
                        nums.remove(i + 1);
                        ops.remove(i);
                    } else {
                        i++;
                    }
                }
            }
            answer = Math.max(answer, Math.abs(nums.get(0)));
        }
        return answer;

    }

    private void parser(String expr, List<Long> nums, List<Character> ops) {
        long cur = 0;
        for (int i = 0; i < expr.length(); i++) {
            char c = expr.charAt(i);
            if (c >= '0' && c <= '9') {
                cur = cur * 10 + (c - '0');
            } else {//ops인 경우
                nums.add(cur);
                cur = 0;
                ops.add(c);
            }
        }
        nums.add(cur);
    }

    private long calc(long a, long b, char op) {
        return switch (op) {
            case '+' -> a + b;
            case '-' -> a - b;
            case '*' -> a * b;
            default -> throw new IllegalArgumentException();
        };
    }

}
