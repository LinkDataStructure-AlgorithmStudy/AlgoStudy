// 1. 위에서 아래로
import java.util.*;
import java.io.*;

public class sort_1 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        Integer arr[] = new Integer[n];
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr, Collections.reverseOrder());

        for(int i =0; i<n; i++){
            System.out.print(arr[i]+ " ");
        }
    }
}
