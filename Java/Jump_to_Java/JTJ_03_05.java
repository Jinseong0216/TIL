package Jump_to_Java;

// StringBuffer는 문자열을 추가하거나 변경할 때, 주로 사용하는 자료형.
// 아래는 StringBuffer에 대한 메서드
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
		
		// StringBuffer는 String보다 무거움+느림.
		// 문자열을 추가하거나 변경하는 작업이 많으면 StringBuffer를, 적으면 String 사용
		
		//StringBuffer는 멀티 스레드 환경에서 안전하고, 
		// StringBuilder는 StringBuffer보다 성능이 우수하다는 장점이 있다. 
		// 따라서 동기화를 고려할 필요가 없는 상황에서는 
		// StringBuffer보다 StringBuilder를 사용하는 것이 유리하다.
		// StringBuffer와 StringBuilder의 사용법은 같음.
	}

}
