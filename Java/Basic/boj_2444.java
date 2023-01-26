import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_2444 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());

        for(int i = 1; i <= n; i++){
            for(int j = 0; j < n-i; j++)
                System.out.print(" ");
            for(int j = 0; j < 2*i-1; j++)
                System.out.print("*");
            System.out.println();
        }
        for(int i = n-1; i > 0; i--){
            for(int j = 0; j < n-i; j++)
                System.out.print(" ");
            for(int j = 0; j < 2*i-1; j++)
                System.out.print("*");
            System.out.println();

        }
    }
}
