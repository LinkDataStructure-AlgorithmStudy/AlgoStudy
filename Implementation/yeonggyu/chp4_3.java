// 시간복잡도 O(1)
import java.util.Scanner;
public class chp4_3 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String n = in.nextLine();
		char a = n.charAt(0);
		char num = n.charAt(1);
		
		int count = 8;
		if(a =='a') count -=3;
		if(a =='b') count -=2;
		if(a =='g') count -=2;
		if(a =='h') count -=3;
		if(num=='2')count -=2;
		if(num=='1')count -=3;
		if(num=='7')count -=2;
		if(num=='8')count -=3;
		
		System.out.println(count);
		
		in.close();
	}
}
