package Jump_to_Java;

// ��
public class JTJ_03_02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean isSuccess = true;
		boolean isTest = false;
		
		System.out.println(isSuccess);
		System.out.println(isTest);
		
		System.out.println(2 > 1);
		System.out.println(1 == 2);            // ����
		System.out.println(3 % 2 == 1);        // �� (3�� 2�� ���� �������� 1�̹Ƿ� ���̴�.)
		System.out.println("3".equals("2"));   // ���� 
		
		// �� ������ ����Ͽ� ���ǹ� �ǽ��غ���
		int base = 100;
		int height = 185;
		boolean isTall = height > base;
		
		if (isTall) {
			System.out.println("Ű�� Ů�ϴ�.");
		}
		
		int i = 3;
		boolean isOdd = i % 2 == 1;
		System.out.println(isOdd);
		
	}

}
