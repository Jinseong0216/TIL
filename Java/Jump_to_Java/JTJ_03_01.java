package Jump_to_Java;

public class JTJ_03_01 {
	
	// �ڹٿ����� ���� ǥ��
	int age = 10;	// �ڹٿ����� ������ ����Ʈ�� int �ڷ�����!!!
	long countOfStar = 8764827384923849L;	// int�� �ִ� ũ�� �Ѿ�°��(2^31 -1) long �ڷ����� L �ٿ��� ��
	
	// �ڹٿ����� �Ǽ� ǥ��
	double morePi = 3.14159265358979323846;	// �ڹٿ����� �Ǽ��� ����Ʈ�� double �ڷ�����!!!
	// double�� ���. ǥ�������� ���� ŭ.
	float pi = 3.14F;	// float �ڷ����� F �ٿ��� ��
	
	// �Ǽ��� ���� ǥ�������� ����ϱ�
	double d1 = 123.4;
	double d2 = 1.234e2;
	
	// 8������ 16����
	// 8������ 16������ int �ڷ����� �����
	// 0(����)���� �����ϸ� 8����, 0x�� �����ϸ� 16����
	int octal = 023;
	int hex = 0xC3;
	
	// �ڹٿ����� ����
	public static void main(String[] args) {
		
		// ���� ����
		int a = 10;
		int b = 6;
		System.out.println(a+b);	// ���ϱ�
		System.out.println(a-b);	// ����
		System.out.println(a/b);	// ������
		System.out.println(a*b);	// ����
		System.out.println(a%b);	// ������ ����
		// �ڹٴ� �� ������ ���� ��� �Ʒ��� ���� �� �� ����
		int c = a/b;
		System.out.println(c);
		
		
		// ���� ����
		int i = 0;
		int j = 10;
		System.out.println(i);
		i++;	// 1 ����
		System.out.println(i);
		System.out.println(j);
		j--;	// 1 ����
		System.out.println(j);
		
		// ���� ���� ���ǻ���
		// ����+���������ڵ��� ���, �ش� �ڵ尡 ����Ǵ� ���� ���� ����Ǵ� �� �ƴ�
		// i++�� ���� ������ ����� ���Ŀ� i ���� �����ϴ� ��! 
		System.out.println(i++);
		System.out.println(i);
		System.out.println(--i);
		System.out.println(i);
	}
	
	
}	
