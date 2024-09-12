package Jump_to_Java;

// 불
public class JTJ_03_02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean isSuccess = true;
		boolean isTest = false;
		
		System.out.println(isSuccess);
		System.out.println(isTest);
		
		System.out.println(2 > 1);
		System.out.println(1 == 2);            // 거짓
		System.out.println(3 % 2 == 1);        // 참 (3을 2로 나눈 나머지는 1이므로 참이다.)
		System.out.println("3".equals("2"));   // 거짓 
		
		// 불 연산을 사용하여 조건문 실습해보기
		int base = 100;
		int height = 185;
		boolean isTall = height > base;
		
		if (isTall) {
			System.out.println("키가 큽니다.");
		}
		
		int i = 3;
		boolean isOdd = i % 2 == 1;
		System.out.println(isOdd);
		
	}

}
