package Tree.P9372;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


/*
 *      Solution code for "BaekJoon 상근이의 여행".
 *
 *      - Problem link: https://www.acmicpc.net/problem/9372
 * */
public class Main {

    static int tesCount; // T ≤ 100
    static int nodeCount; // 2 ≤ N ≤ 1 000
    static int edgeCount; // 1 ≤ M ≤ 10 000

    static BufferedReader br;
    static StringBuffer sb;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException  {
        // System.setIn(new FileInputStream("./src/Tree/P9372/9372.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuffer();

        tesCount = Integer.parseInt(br.readLine());

        for (int i = 0; i < tesCount; i++) {
            testRun();
        }
    }

    public static void testRun() throws IOException {
        st = new StringTokenizer(br.readLine());

        nodeCount = Integer.parseInt(st.nextToken());
        edgeCount = Integer.parseInt(st.nextToken());

        for (int i = 0; i < edgeCount; i++) {
            br.readLine();
        }

        System.out.println(nodeCount - 1);
    }
}
