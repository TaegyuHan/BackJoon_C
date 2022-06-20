package Tree.P4256;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/*
 *      Solution code for "BaekJoon 트리".
 *
 *      - Problem link: https://www.acmicpc.net/problem/4256
 * */
class Main {

    static int[] preOrder = new int[1001];
    static int[] inOrder = new int[1001];
    static int N;
    static int TestCase;

    public static void main(String[] args) throws IOException {
        // 입력 파일
        // System.setIn(new FileInputStream("./src/Tree/P4256/4256.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        StringTokenizer st;

        TestCase = Integer.parseInt(br.readLine());

        // 테스트 케이스
        for (int t = 0; t < TestCase; t++) {
            N = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < N; i++) {
                preOrder[i] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine(), " ");
            for (int i = 0; i < N; i++) {
                inOrder[i] = Integer.parseInt(st.nextToken());
            }

            tree(0, 0, N, sb);
            sb.append('\n');
        }

        System.out.println(sb);
    }

    /*
     * 트리
     * */
    public static void tree(int root, int start, int end, StringBuffer sb) {
        for (int i = start; i < end; i++) {
            if (inOrder[i] == preOrder[root]) {
                tree(root + 1, start, i, sb);
                tree(root + 1 + i - start, i + 1, end, sb);
                sb.append(preOrder[root]).append(' ');
            }
        }
    }
}