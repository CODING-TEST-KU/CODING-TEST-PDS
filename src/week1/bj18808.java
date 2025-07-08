package src.week1;

import java.util.*;

public class bj18808 {

    static int n, m;
    static int[][] laptop;

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        n = scan.nextInt();
        m = scan.nextInt();
        int k = scan.nextInt();

        laptop = new int[n][m];

        List<int[][]> stickers = new ArrayList<>(k);

        //sticker 입력받기
        for (int i = 0; i < k; i++) {
            int row = scan.nextInt();
            int col = scan.nextInt();
            int[][] sticker = new int[row][col];
            for (int j = 0; j < row; j++) {
                for (int q = 0; q < col; q++) {
                    sticker[j][q] = scan.nextInt();
                }
            }
            stickers.add(sticker);
        }

        //laptop에 스티커 붙일 수 있는지 탐색
        for (int[][] sticker : stickers) {
            for (int i = 0; i < 4; i++) {
                //todo placeSticker
                boolean success = placeSticker(sticker);

                //todo rotate
                if (!success) sticker = rotate(sticker);
                else break;
            }
        }

        //laptop에 붙여진 스티커 칸 수 세기
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                count += laptop[i][j];
            }
        }
        System.out.println(count);

    }

    //스티커를 노트북에 붙여보기 안되면 rotate해야하니 boolean 반환
    private static boolean placeSticker(int[][] sticker) {
        int row = sticker.length;
        int col = sticker[0].length;

        // 2차원 배열을 다룰 때는 outOfRange를 늘 고려해야한다.
        for (int i = 0; i <= n - row; i++) {
            for (int j = 0; j <= m - col; j++) {
                if (canAttach(i, j, sticker)) {
                    attach(i, j, sticker);
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean canAttach(int x, int y, int[][] sticker) {
        int row = sticker.length;
        int col = sticker[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (sticker[i][j] == 1 && laptop[x + i][y + j] == 1) return false;
            }
        }
        return true;
    }

    private static void attach(int x, int y, int[][] sticker) {
        int row = sticker.length;
        int col = sticker[0].length;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (sticker[i][j] == 1) laptop[x + i][y + j] = 1;
            }
        }
    }

    private static int[][] rotate(int[][] sticker) {
        int row = sticker.length;
        int col = sticker[0].length;
        int[][] rotatedSticker = new int[col][row];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                rotatedSticker[j][row-i-1]=sticker[i][j];
            }
        }
        return rotatedSticker;
    }

}
