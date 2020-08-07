import java.math.BigInteger;
import java.util.Scanner;

public class Math_C {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger A =new BigInteger(in.next());
        BigInteger B =new BigInteger(in.next());
        //print A*B/gcd(A,B)
        System.out.println(A.multiply(B).divide(A.gcd(B)));
    }
}
