import java.math.BigInteger;
import java.util.Scanner;

public class Math_B {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        double N =in.nextInt();
        if(N==0){
            System.out.println(0);
            return;
        }
        // i jadi pecahan (50/100 -> 0.5)
        double i = N/100;
        // berapa kali i untuk sampe 1, jadi 1/i
        i = 1/i;

        //i itu banyaknya ganjil, diantara 2 ganjil kan ada 1 genap
        // diantara 3 ganjil ada 2 genap dst.
        //jadi ini print (ganjil/(genap+ganjil))
        System.out.println((i/(2*i-1)));

    }
}
