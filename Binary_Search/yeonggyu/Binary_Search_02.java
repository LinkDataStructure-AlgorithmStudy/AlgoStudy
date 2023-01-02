import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Binary_Search_02 {
    /**
     * N : 부품 개수
     * M : 부품 종류
     * output : Yes, no
     */
    public static void main(String args[]) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n, m;
        n= Integer.parseInt(br.readLine());
        List<Integer> arr1 = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr1.add(Integer.parseInt(st.nextToken()));
        }
        m= Integer.parseInt(br.readLine());
        List<Integer> arr2 = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<m; i++){
            arr2.add(Integer.parseInt(st.nextToken()));
        }

        // main logic
        Collections.sort(arr1);
        StringBuilder sb = new StringBuilder();
        String result;
        for(int i=0; i<m; i++){
            sb.append(search(arr1, arr2.get(i))).append(" ");
        }
        result = sb.toString();

        // output
        System.out.println(result);

    }

    public static String search(List<Integer> arr, Integer a){
        int index = Collections.binarySearch(arr, a);
        if(index < 0){
            return "no";
        }
        else{
            return "yes";
        }
    }
}