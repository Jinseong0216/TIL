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
		
		// �� ������(���̽�� ���̰� ����)
		System.out.println(a.equals(A));	// ���̽㿡���� == �� ����
		System.out.println(a == A);			// ���̽㿡���� is �� ����
		
		// ���ڿ� �޼���
		// indexOf: ���̽㿡���� index
		// contains: ���̽㿡���� in
		// charAt: ���̽㿡���� �迭�� �ε����ִ°Ͱ� ������
		// replaceAll: replace
		// substring: �����̽���
		// split: �߿���, ���ڿ��� ���ڿ� �迭�� ����
		
		String str = "a:b:c:d";
		String[] result = str.split(":");
		System.out.println(Arrays.asList(result));
		
		System.out.println(String.format("I eat %d apples.", 3));  // "I eat 3 apples." ���
		System.out.println(String.format("I eat %s apples.", "five"));  // "I eat five apples." ���
		int number = 3;
		System.out.println(String.format("I eat %d apples.", number));  // "I eat 3 apples." ���
		int number_2 = 10;
		String day = "three";
		System.out.println(String.format("I ate %d apples. so I was sick for %s days.", number_2, day));
		System.out.println(String.format("I have %s apples",  3));  // "I have 3 apples" ���
		System.out.println(String.format("rate is %s", 3.234));  // "rate is 3.234" ���

		
		System.out.println(String.format("I eat %d apples.", 3));
		System.out.printf("I eat %d apples.", 3);  // "I eat 3 apples." ���

	}

}
