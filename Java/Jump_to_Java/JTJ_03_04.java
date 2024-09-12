package Jump_to_Java;

import java.util.Arrays;

public class JTJ_03_04 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String a = "Happy Java";
		String b = "a";
		String c = "123";
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		
		String A = new String("Happy Java");
		String B = new String("a");
		String C = new String("123");
		System.out.println(A);
		System.out.println(B);
		System.out.println(C);
		
		// 비교 연산자(파이썬과 차이가 있음)
		System.out.println(a.equals(A));	// 파이썬에서의 == 와 같음
		System.out.println(a == A);			// 파이썬에서의 is 와 같음
		
		// 문자열 메서드
		// indexOf: 파이썬에서의 index
		// contains: 파이썬에서의 in
		// charAt: 파이썬에서의 배열에 인덱스넣는것과 유사함
		// replaceAll: replace
		// substring: 슬라이싱임
		// split: 중요함, 문자열을 문자열 배열로 리턴
		
		String str = "a:b:c:d";
		String[] result = str.split(":");
		System.out.println(Arrays.asList(result));
		
		System.out.println(String.format("I eat %d apples.", 3));  // "I eat 3 apples." 출력
		System.out.println(String.format("I eat %s apples.", "five"));  // "I eat five apples." 출력
		int number = 3;
		System.out.println(String.format("I eat %d apples.", number));  // "I eat 3 apples." 출력
		int number_2 = 10;
		String day = "three";
		System.out.println(String.format("I ate %d apples. so I was sick for %s days.", number_2, day));
		System.out.println(String.format("I have %s apples",  3));  // "I have 3 apples" 출력
		System.out.println(String.format("rate is %s", 3.234));  // "rate is 3.234" 출력

		
		System.out.println(String.format("I eat %d apples.", 3));
		System.out.printf("I eat %d apples.", 3);  // "I eat 3 apples." 출력

	}

}
