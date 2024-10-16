import java.util.*;
// ��� �Ǵ���...
//import java.io.FileInputStream;


public class SWEA_2105 {
    static int ans = 0;
    static int[][] grid;
    static boolean[] ate;
    static int[][] dij = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
    static int N;

    public static void main(String[] args) {
    	// ��ĳ�� �����ϰ� ����
        Scanner sc = new Scanner(System.in);
        // �׽�Ʈ ���̽��� ��
        int T = sc.nextInt();
        // �׽�Ʈ ���̽��� �ݺ�
        for (int t = 1; t <= T; t++) {
        	// �׸����� ũ��
            N = sc.nextInt();
            // �׸��� ����(������ NxN)
            grid = new int[N][N];
            // �׸��忡 ������ �޾ƿ�
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    grid[i][j] = sc.nextInt();
                }
            }
            // ����Ʈ ���� ���� üũ�� ���� �迭
            ate = new boolean[101];
            // ���� �ʱⰪ
            ans = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                	// �Լ� ȣ��
                    solution(new int[] {i, j}, new int[]{i, j}, 0, 0);
                }
            }

            if (ans == 0) {
                System.out.println("#" + t + " " + "-1");
            } else {
                System.out.println("#" + t + " " + ans);
            }
        }
        // ��ĳ�� �ݱ�
        sc.close();
    }
    
    // ���� �ذ��� ���� solution function ����
    private static void solution(int[] start, int[] now, int dij_idx, int number_of_desert) {
    // Ż������ ������Ʈ
    	// ������ �����̸鼭, ó�� ������ġ�� ����´ٸ� �Լ��� �����
        if (dij_idx == 3 && Arrays.equals(start, now)) {
        	// ���� ��ο��� ã�� ����Ʈ�� ������ �������� ���ٸ� ������Ʈ�� ������
        	if (ans < number_of_desert) {
        		ans = number_of_desert;
        	}
        	// ������Ʈ ���� �ʴ��� �ᱹ �Լ��� �����
            return;
        }

    // Case1) ���⼺�� �����ϸ�, �� ĭ �̵�
        // ��Ÿ �޾ƿ���
        int di = dij[dij_idx][0];
        int dj = dij[dij_idx][1];
        // ��Ÿ�� �̿���, ���� ��ġ ����
        int ni = now[0] + di;
        int nj = now[1] + dj;
        // out of range ���ϱ�
        if (0 <= ni && ni < N && 0 <= nj && nj < N) {
        	// ���� ��ġ�� ����Ʈ ��ȣ �޾ƿ���
            int desert = grid[ni][nj];
            // ���� �������� ����Ʈ���
            if (!ate[desert]) {
            	// ���� üũ
                ate[desert] = true;
                // �Լ� ȣ��0
                solution(start, new int[]{ni, nj}, dij_idx, number_of_desert + 1);
                // ���� ����
                ate[desert] = false; 
            }
        }
    // Case2) ���⼺ ����X, �� ĭ �̵�   
        // ������ ������ �ƴ� ��쿡�� ����
        if (dij_idx < 3) {
        	// ��Ÿ �޾ƿ���
            di = dij[dij_idx + 1][0];
            dj = dij[dij_idx + 1][1];
            // ��Ÿ�� �̿���, ���� ��ġ ����
            ni = now[0] + di;
            nj = now[1] + dj;
            // out of range ���ϱ�
            if (0 <= ni && ni < N && 0 <= nj && nj < N) {
            	// ���� ��ġ�� ����Ʈ ��ȣ �޾ƿ���
                int desert = grid[ni][nj];
            	// ���� �������� ����Ʈ���
                if (!ate[desert]) {
                	// ���� üũ
                    ate[desert] = true;
                    // �Լ� ȣ��
                    solution(start, new int[]{ni, nj}, dij_idx + 1, number_of_desert + 1);
                    // ���� ����
                    ate[desert] = false; // backtrack
                }
            }
        }
    }
}
