import java.util.Scanner;
import java.math.BigInteger;

public class Math_A {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BigInteger N =new BigInteger(in.next());
        BigInteger A =new BigInteger(in.next());
        BigInteger B =new BigInteger(in.next());
        if(A.mod(B).toString().equals("0") ) System.out.println(N.divide(B));
        else if (B.mod(A).toString().equals("0") ) System.out.println(N.divide(A));
        else System.out.println(N.divide(A).add(N.divide(B)).subtract(N.divide(A.multiply(B))));
    }
}
