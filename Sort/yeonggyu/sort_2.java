// 2. 성적이 낮은 순서로 학생 출력하기
import java.util.*;
import java.io.*;

class Student implements Comparable<Student>{
    private final String name;
    private final int score;

    Student(String name, int score){
        this.name = name;
        this.score = score;
    }
    public String getName(){
        return this.name;
    }
    // 객체 비교
    @Override
    public int compareTo(Student s){
        return this.score- s.score;
    }
}

public class sort_2 {
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Student> arr = new ArrayList<>();
        // n
        Integer n = Integer.parseInt(br.readLine());

        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            Integer score = Integer.parseInt(st.nextToken());
            arr.add(new Student(name, score));
        }

        Collections.sort(arr);

        for(Student s : arr){
            System.out.print(s.getName() + " ");
        }
    }
}
