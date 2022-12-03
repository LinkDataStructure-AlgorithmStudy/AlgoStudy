// 두 배열의 원소 교체
import java.util.*;
import java.io.*;

public class sort_3 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer n = Integer.parseInt(st.nextToken());
        Integer k = Integer.parseInt(st.nextToken());
        ArrayList<Integer> arr1 = new ArrayList<>();
        ArrayList<Integer> arr2 = new ArrayList<>();

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr1.add(Integer.parseInt(st1.nextToken()));
            arr2.add(Integer.parseInt(st2.nextToken()));
        }

        Collections.sort(arr1);
        Collections.sort(arr2, Collections.reverseOrder());

        for(int i=0; i<k; i++){
            arr1.set(i, arr2.get(i));
        }
        Integer sum =0;
        for(int i=0; i<n; i++){
            sum += arr1.get(i);
        }
        System.out.println(sum);

    }
}
