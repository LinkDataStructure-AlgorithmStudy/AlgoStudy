import java.io.*;
import java.util.*;
import java.awt.Point;

// BFS
public class BFS_DFS_4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 판
        int[][] board = new int[n][m];
        // 거리
        int[][] dist = new int[n][m];
        // 거리 -1로 초기화
        for(int i=0; i<n; i++){
            Arrays.fill(dist[i], -1);
        }

        int[] dx = {1,0,-1,0};
        int[] dy = {0,1, 0,-1};

        for(int i=0; i<n; i++){
            String str = br.readLine();
            for(int j=0; j<m; j++){
                board[i][j] = str.charAt(j)-'0';
            }
        }
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0,0));
        dist[0][0] =0;
        while(!q.isEmpty()){
            Point cur = q.peek();
            q.poll();
            for(int dir=0; dir<4; dir++){
                int nx = cur.x + dx[dir];
                int ny = cur.y + dy[dir];
                if(nx < 0 || nx >=n || ny<0 || ny >=m) continue;
                if(dist[nx][ny]>=0 || board[nx][ny] != 1) continue;
                dist[nx][ny] = dist[cur.x][cur.y]+1;
                q.add(new Point(nx, ny));
            }
        }

        System.out.println(dist[n-1][m-1]+1);
    }
}
