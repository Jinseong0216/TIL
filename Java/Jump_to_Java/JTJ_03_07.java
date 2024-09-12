package Jump_to_Java;

// ArrayList�� ����ϱ� ����
import java.util.ArrayList;
import java.util.Arrays;


// ����Ʈ
// ArrayList, Vector, LinkedList���� �ڷ����� ����.	
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
		
		// ���̿� �߰��Ǹ鼭 �˾Ƽ� ������ Ŀ��
		pitches.add(1, "changed");
		
		System.out.println(pitches.size());
		System.out.println(pitches.get(0));
		System.out.println(pitches.get(1));
		System.out.println(pitches.get(2));
		System.out.println(pitches.get(3));
		System.out.println(pitches.get(4));
		
		// in�� ����
		System.out.println(pitches.contains("111"));
		
		// ����
		System.out.println(pitches.remove("111"));  // 111�� ����Ʈ���� �����ϰ�, true�� �����Ѵ�.

		pitches.add(5);
		System.out.println(pitches.get(4));
		
		// ������ �ڷḦ ��̸���Ʈ���� �����ϴ� ���
		System.out.println(pitches);
		pitches.remove(Integer.valueOf(5));
		System.out.println(pitches);
		
		
		String pitch = (String) pitches.get(0);
		System.out.println(pitch);
		
		
		// ���׸���!!!!
		ArrayList<String> colors = new ArrayList<>();
		colors.add("Blue");
		System.out.println(colors);
//		colors.add(5); ���� �߻�!
		
		String color = colors.get(0);
		System.out.println(color);
		
		
		// �پ��� ������� ��̸���Ʈ �����
		String[] data = {"138", "129", "142"};
		ArrayList<String> speeds = new ArrayList<>(Arrays.asList(data));
		System.out.println(speeds);
		
		// Ȥ�� 
		ArrayList<String> speeds_2 = new ArrayList<>(Arrays.asList("111", "222", "333"));
		System.out.println(speeds_2);
		
		
	}

}
