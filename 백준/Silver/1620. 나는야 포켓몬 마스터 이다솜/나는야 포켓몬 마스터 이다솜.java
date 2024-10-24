import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		HashMap<String, Integer> pokemonName = new HashMap<>();
		HashMap<Integer, String> pokemonNum = new HashMap<>();
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i <= N; i++) {
			String name = br.readLine();
			pokemonName.put(name, i);
			pokemonNum.put(i, name);
		}
		
		for (int i = 0; i < M; i++) {
			String str = br.readLine();
			String result = "";
			
			if (str.matches("[+-]?\\d*(\\.\\d+)?")) {
				int num = Integer.parseInt(str);
				
				result = pokemonNum.get(num);
			} else {
				result = String.valueOf(pokemonName.get(str));
			}
			
			bw.write(result);
			bw.newLine();
		}
		bw.flush();
	}
}
