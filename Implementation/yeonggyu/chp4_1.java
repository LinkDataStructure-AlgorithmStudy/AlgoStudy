// �ð� ���⵵ O(n)
import java.util.Scanner;

public class chp4_1 {

	public static void main(String[] args) {
		// input
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		// ���๮�� ����
		in.nextLine();
		String inp = in.nextLine();
		
		// ���� ����
				int[] arr = {1, 1};
		
		// input ���ڿ� split
		String[] strArr = inp.split(" ");
		
		for(int i=0; i<strArr.length; i++) {
			switch(strArr[i]) {
				case "L":
					if(arr[1]==1) {break;}
					else {
						arr[1] -= 1;
					}
					break;
				case "R":
					if(arr[1]==n) {break;}
					else {
						arr[1] = arr[1] + 1;
					}
					break;
				case "U":
					if(arr[0]==1) {break;}
					else {
						arr[0] -=1;
						break;
					}
					
				case "D":
					if(arr[0]==n) {break;}
					else {
						arr[0] +=1;
					}
					break;
				default:
					System.out.println("Error : �߸��� String �迭");
					break;
			}
		}
		
		System.out.println(arr[0] + " " + arr[1]);
		
		in.close();
	}
}
