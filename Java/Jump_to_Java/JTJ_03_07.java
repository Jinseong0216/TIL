package Jump_to_Java;

// ArrayList를 사용하기 위함
import java.util.ArrayList;
import java.util.Arrays;


// 리스트
// ArrayList, Vector, LinkedList등의 자료형이 있음.	
public class JTJ_03_07 {
	public static void main(String[] args) {
		ArrayList pitches = new ArrayList();
		pitches.add("111");
		pitches.add("222");
		pitches.add("333");
		pitches.add("444");
		System.out.println(pitches.get(0));
		System.out.println(pitches.get(1));
		System.out.println(pitches.get(2));
		System.out.println(pitches.get(3));
		
		// 사이에 추가되면서 알아서 사이즈 커짐
		pitches.add(1, "changed");
		
		System.out.println(pitches.size());
		System.out.println(pitches.get(0));
		System.out.println(pitches.get(1));
		System.out.println(pitches.get(2));
		System.out.println(pitches.get(3));
		System.out.println(pitches.get(4));
		
		// in의 역할
		System.out.println(pitches.contains("111"));
		
		// 삭제
		System.out.println(pitches.remove("111"));  // 111를 리스트에서 삭제하고, true를 리턴한다.

		pitches.add(5);
		System.out.println(pitches.get(4));
		
		// 정수형 자료를 어레이리스트에서 삭제하는 방법
		System.out.println(pitches);
		pitches.remove(Integer.valueOf(5));
		System.out.println(pitches);
		
		
		String pitch = (String) pitches.get(0);
		System.out.println(pitch);
		
		
		// 제네릭스!!!!
		ArrayList<String> colors = new ArrayList<>();
		colors.add("Blue");
		System.out.println(colors);
//		colors.add(5); 에러 발생!
		
		String color = colors.get(0);
		System.out.println(color);
		
		
		// 다양한 방법으로 어레이리스트 만들기
		String[] data = {"138", "129", "142"};
		ArrayList<String> speeds = new ArrayList<>(Arrays.asList(data));
		System.out.println(speeds);
		
		// 혹은 
		ArrayList<String> speeds_2 = new ArrayList<>(Arrays.asList("111", "222", "333"));
		System.out.println(speeds_2);
		
		
	}

}
