import java.util.*;
// 없어도 되더라...
//import java.io.FileInputStream;


public class SWEA_2105 {
    static int ans = 0;
    static int[][] grid;
    static boolean[] ate;
    static int[][] dij = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};
    static int N;

    public static void main(String[] args) {
    	// 스캐너 정의하고 생성
        Scanner sc = new Scanner(System.in);
        // 테스트 케이스의 수
        int T = sc.nextInt();
        // 테스트 케이스별 반복
        for (int t = 1; t <= T; t++) {
        	// 그리드의 크기
            N = sc.nextInt();
            // 그리드 정의(사이즈 NxN)
            grid = new int[N][N];
            // 그리드에 정보를 받아옴
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    grid[i][j] = sc.nextInt();
                }
            }
            // 디저트 종류 먹음 체크를 위한 배열
            ate = new boolean[101];
            // 정답 초기값
            ans = 0;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                	// 함수 호출
                    solution(new int[] {i, j}, new int[]{i, j}, 0, 0);
                }
            }

            if (ans == 0) {
                System.out.println("#" + t + " " + "-1");
            } else {
                System.out.println("#" + t + " " + ans);
            }
        }
        // 스캐너 닫기
        sc.close();
    }
    
    // 문제 해결을 위한 solution function 정의
    private static void solution(int[] start, int[] now, int dij_idx, int number_of_desert) {
    // 탈출조건 지정파트
    	// 마지막 방향이면서, 처음 시작위치로 돌라온다면 함수는 종료됨
        if (dij_idx == 3 && Arrays.equals(start, now)) {
        	// 만약 경로에서 찾은 디저트의 개수가 기존보다 많다면 업데이트를 진행함
        	if (ans < number_of_desert) {
        		ans = number_of_desert;
        	}
        	// 업데이트 하지 않더라도 결국 함수는 종료됨
            return;
        }

    // Case1) 방향성을 유지하며, 한 칸 이동
        // 델타 받아오기
        int di = dij[dij_idx][0];
        int dj = dij[dij_idx][1];
        // 델타를 이용한, 다음 위치 설정
        int ni = now[0] + di;
        int nj = now[1] + dj;
        // out of range 피하기
        if (0 <= ni && ni < N && 0 <= nj && nj < N) {
        	// 다음 위치의 디저트 번호 받아오기
            int desert = grid[ni][nj];
            // 아직 먹지않은 디저트라면
            if (!ate[desert]) {
            	// 먹음 체크
                ate[desert] = true;
                // 함수 호출0
                solution(start, new int[]{ni, nj}, dij_idx, number_of_desert + 1);
                // 먹음 해제
                ate[desert] = false; 
            }
        }
    // Case2) 방향성 유지X, 한 칸 이동   
        // 마지막 방향이 아닌 경우에만 적용
        if (dij_idx < 3) {
        	// 델타 받아오기
            di = dij[dij_idx + 1][0];
            dj = dij[dij_idx + 1][1];
            // 델타를 이용한, 다음 위치 설정
            ni = now[0] + di;
            nj = now[1] + dj;
            // out of range 피하기
            if (0 <= ni && ni < N && 0 <= nj && nj < N) {
            	// 다음 위치의 디저트 번호 받아오기
                int desert = grid[ni][nj];
            	// 아직 먹지않은 디저트라면
                if (!ate[desert]) {
                	// 먹음 체크
                    ate[desert] = true;
                    // 함수 호출
                    solution(start, new int[]{ni, nj}, dij_idx + 1, number_of_desert + 1);
                    // 먹음 해제
                    ate[desert] = false; // backtrack
                }
            }
        }
    }
}
