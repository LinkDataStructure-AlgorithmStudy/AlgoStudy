// 시간 복잡도 O(n)
import java.util.Scanner;

public class chp4_1 {

	public static void main(String[] args) {
		// input
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		// 개행문자 방지
		in.nextLine();
		String inp = in.nextLine();
		
		// 시작 지점
				int[] arr = {1, 1};
		
		// input 문자열 split
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
					System.out.println("Error : 잘못된 String 배열");
					break;
			}
		}
		
		System.out.println(arr[0] + " " + arr[1]);
		
		in.close();
	}
}
