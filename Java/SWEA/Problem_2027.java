package SWEA;

import java.util.Scanner;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.Arrays;


public class Problem_2027
{
	public static void main(String args[]) throws Exception
	{
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        String dummy = sc.nextLine();

        for(int test_case = 1; test_case <= T; test_case++) {
            int cnt = 0;
            String[] seq = sc.nextLine().split(" ");
//            System.out.println(seq);
            
            ArrayList[] sequence = new ArrayList(Arrays.asList(seq)));
            System.out.println(sequence);
  //          for (int L == 1; L <= >)
//            System.out.println(Arrays.asList(seq));

		}
	}
}