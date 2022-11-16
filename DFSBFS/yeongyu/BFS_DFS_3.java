// BFS로 구현

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.awt.Point;

public class BFS_DFS_3 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        boolean[][] vis = new boolean[n][m];

        for(int i=0; i<n; i++){
            String str = br.readLine();
            for(int j=0; j<m; j++){
                board[i][j] = str.charAt(j)-'0';
            }
        }

        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};


        
        //아이스크림 개수
        int num =0;
        
        // BFS 시작
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(board[i][j]==0 || vis[i][j]) continue;
                num++;
                Queue<Point> q = new LinkedList<>();
                vis[i][j] = true;
                q.add(new Point(i, j));

                while(!q.isEmpty()){
                    Point cur = (q.peek());
                    q.poll();

                    for(int dir=0; dir<4; dir++){
                        int nx = cur.x + dx[dir];
                        int ny = cur.y + dy[dir];
                        if(nx <0 || nx >= n|| ny <0 || ny >= m) continue;
                        if(vis[nx][ny] || board[nx][ny] != 1) continue;
                        vis[nx][ny] = true;
                        q.add(new Point(nx,ny));
                    }
                }
            }
        }

        System.out.println(num);
    }
}
