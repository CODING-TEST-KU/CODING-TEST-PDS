package src.week2;

import java.util.*;
import java.io.*;

public class bj1058 {

    private static boolean[][] friends;
    private static Set<Integer>[] friendsSet;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        friends = new boolean[n][n];
        friendsSet = new HashSet[n];

        // Y이면 true, N이면 false
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                friends[i][j] = line.charAt(j) == 'Y' ? true : false;
            }
            friendsSet[i] = new HashSet<>();
        }
        //친구인사람 수 세기
        firstStepFriends();
        secondStepFriends();
        int max = 0;
        for (Set<Integer> person : friendsSet) {
            int count = person.size();
            if (max < count) max = count;
        }

        System.out.println(max);

    }

    private static void firstStepFriends() {
        int length = friends.length;
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                if (i != j && friends[i][j]) friendsSet[i].add(j);
            }
        }
    }

    private static void secondStepFriends() {
        int length = friends.length;
        //A의 모든 친구들은 서로 친구가 된다.
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                if (friends[i][j]) {
                    for (int k = 0; k < length; k++) {
                        if (i != k && friends[j][k]) friendsSet[i].add(k);
                    }
                }
            }
        }
    }


}
