package Jump_to_Java;

// StringBuffer�� ���ڿ��� �߰��ϰų� ������ ��, �ַ� ����ϴ� �ڷ���.
// �Ʒ��� StringBuffer�� ���� �޼���
public class JTJ_03_05 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuffer sb = new StringBuffer();
		sb.append("hello");
		sb.append(" ");
		sb.append("jump to java");
		String result = sb.toString();
		System.out.println(result);
		
		String result_2 = "";
		result_2 += "hello";
		result_2 += " ";
		result_2 += "jump to java";
		System.out.println(result_2);
		
		// StringBuffer�� String���� ���ſ�+����.
		// ���ڿ��� �߰��ϰų� �����ϴ� �۾��� ������ StringBuffer��, ������ String ���
		
		//StringBuffer�� ��Ƽ ������ ȯ�濡�� �����ϰ�, 
		// StringBuilder�� StringBuffer���� ������ ����ϴٴ� ������ �ִ�. 
		// ���� ����ȭ�� ����� �ʿ䰡 ���� ��Ȳ������ 
		// StringBuffer���� StringBuilder�� ����ϴ� ���� �����ϴ�.
		// StringBuffer�� StringBuilder�� ������ ����.
	}

}
