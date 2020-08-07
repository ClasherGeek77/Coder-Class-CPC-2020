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
        double i = N/100;
        i = 1/i;

        System.out.println((i/(2*i-1)));

    }
}
