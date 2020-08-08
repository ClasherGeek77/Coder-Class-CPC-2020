import java.math.BigInteger;
import java.util.Scanner;

public class Math_D {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long N =in.nextInt();
        long K =in.nextInt();

        long prime = 1;
        boolean isprime = false;
        int j=0;

        for(int i = 1; i<=(N-1)*K+1;i++){
            //looping cari prime ke-i
            while(!isprime){
                prime++;
                isprime=true;
                for(long k=2; k*k<=prime; k++){
                    if(prime%k == 0){
                        isprime=false;
                        break;
                    }
                }
            }
            //print prime ke-i sesuai keinginan soal
            if(i == j*K+1){
                System.out.println(prime);
                j++;
            }
            isprime = false;
        }
    }
}
