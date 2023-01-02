import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Input
 * N : 떡의 개수(1~1,000,000)
 * M : 요청한 떡의 길이(1~2,000,000,000)
 * 절단기로 떡을 자름 남은 길이
 * 배열 오름차순 정렬 -> start=[0], end[n] -> (mid >= M)? return mid : start,end 조정 후 반복(단, start == end -> return mid)
 */

public class Binary_Search_03 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // Input
        int n = Integer.parseInt(st.nextToken());
        long m = Long.parseLong(st.nextToken());
        st = new StringTokenizer(br.readLine());
        List<Integer> arr = new ArrayList<>();
        for(int i=0; i<n; i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }
        System.out.println("input n, m: "+ n + " " + m);
        System.out.println("arr: "+ arr);

        // Main Logic
        Collections.sort(arr); // 정렬
        int start = 0;
        int end = arr.get(arr.size()-1);
        int mid;
        int result=0;
        while(start<=end){
            mid = (start+end)/2;
            System.out.println("------");
            System.out.println("start: "+start);
            System.out.println("mid: " + mid);
            System.out.println("end: "+end);
            int total = 0;
            for(Integer a : arr){
                if(a>mid){
                    total += a-mid;
                }
            }
            if (total>=m) {
                result = mid;
                start=mid+1;
            } else{
                end = mid-1;
            }
        }

        System.out.println(result);
    }
}
