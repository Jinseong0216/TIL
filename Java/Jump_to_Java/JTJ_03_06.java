package Jump_to_Java;

// 배열
public class JTJ_03_06 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] odds = {1, 3, 5, 7, 9};
//		String[] days = {"월", "화", "수", "목", "금", "토", "일"};
		String[] days = new String[7];
		
		// length는 배열의 길이를 구하는 메서드
		for (int i = 0; i < days.length; i++) {
			System.out.println(days[i]);
		}
	}

}
