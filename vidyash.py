import java.util.*; 
import java.math.*; 
public class GFG{ 
  
     public static void main(String []args){ 
        String str="7777555511111111"; 
        String str1="3332222221111"; 
          
        BigInteger a=new BigInteger(str); // creating obj of biginteger and pass str in it 
        BigInteger b=new BigInteger(str1); // creating obj of biginteger and pass str1 in it 
         
        System.out.println(a.add(b));
