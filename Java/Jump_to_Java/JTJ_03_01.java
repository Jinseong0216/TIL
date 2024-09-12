package Jump_to_Java;

public class JTJ_03_01 {
	
	// 자바에서의 정수 표현
	int age = 10;	// 자바에서의 정수는 디폴트가 int 자료형임!!!
	long countOfStar = 8764827384923849L;	// int의 최대 크기 넘어가는경우(2^31 -1) long 자료형은 L 붙여야 함
	
	// 자바에서의 실수 표현
	double morePi = 3.14159265358979323846;	// 자바에서의 실수는 디폴트가 double 자료형임!!!
	// double의 경우. 표현범위가 아주 큼.
	float pi = 3.14F;	// float 자료형은 F 붙여야 함
	
	// 실수를 지수 표현식으로 사용하기
	double d1 = 123.4;
	double d2 = 1.234e2;
	
	// 8진수와 16진수
	// 8진수와 16진수는 int 자료형을 사용함
	// 0(숫자)으로 시작하면 8진수, 0x로 시작하면 16진수
	int octal = 023;
	int hex = 0xC3;
	
	// 자바에서의 연산
	public static void main(String[] args) {
		
		// 숫자 연산
		int a = 10;
		int b = 6;
		System.out.println(a+b);	// 더하기
		System.out.println(a-b);	// 빼기
		System.out.println(a/b);	// 나누기
		System.out.println(a*b);	// 곱셈
		System.out.println(a%b);	// 나머지 연산
		// 자바는 몫 연산이 없음 대신 아래와 같이 할 수 있음
		int c = a/b;
		System.out.println(c);
		
		
		// 증감 연산
		int i = 0;
		int j = 10;
		System.out.println(i);
		i++;	// 1 증가
		System.out.println(i);
		System.out.println(j);
		j--;	// 1 감소
		System.out.println(j);
		
		// 증감 연산 주의사항
		// 변수+증감연산코드의 경우, 해당 코드가 실행되는 순간 값이 변경되는 게 아님
		// i++와 같은 문장이 실행된 이후에 i 값이 증가하는 것! 
		System.out.println(i++);
		System.out.println(i);
		System.out.println(--i);
		System.out.println(i);
	}
	
	
}	
