// 시간복잡도 O(n^3)
import java.util.Scanner;

public class chp4_2 {

	public static void main(String[] args) {
		// input
		Scanner in = new Scanner(System.in);
		String s; 
		int n = in.nextInt();
		int count = 0;
		
		// find "3"
		for(int i=0; i<=n; i++) {
			for(int j=0; j<60; j++) {
				for(int k=0; k<60; k++) {
					s= Integer.toString(i) + Integer.toString(j) + Integer.toString(k);
					if(s.indexOf("3")!= -1) {
						count++;
					}
				}
			}
		}
		
		// output
		System.out.println(count);
		in.close();
	}

}
