package clase.pkg4.tipos.primitivos;
public class Clase4TiposPrimitivos {
    public static void main(String[] args) {
        byte numEnteroByte = (byte)127;
        System.out.println("Valor minimo del Byte "+Byte.MIN_VALUE);
        System.out.println("Valor máximo del Byte "+Byte.MAX_VALUE);
        System.out.println("NumEnterobyte :"+numEnteroByte);
        
        Short numEnteroShort=32767;
        System.out.println("numEnteroShort = "+numEnteroShort);
        System.out.println("valor mínimo de Short "+Short.MAX_VALUE);
        System.out.println("valor máximo de Short "+Short.MIN_VALUE);
        
        int numEnteroInt=2147483647;
        System.out.println("numEnteroInt = "+numEnteroInt);
        System.out.println("valor máximo de int "+Integer.MAX_VALUE);
        System.out.println("valor mínimo de int "+Integer.MIN_VALUE);
        
        long numEnteroLong=9223372036854775807L;
        System.out.println("numEnteroLong = "+numEnteroLong);
        System.out.println("valor máximo de long "+Long.MAX_VALUE);
        System.out.println("valor mínimo de long "+Long.MIN_VALUE);
        
        float numFloat= 10.2F;
        System.out.println("numFloat = "+numFloat);
        System.out.println("valor máximo de float "+Float.MAX_VALUE);
        System.out.println("valor mínimo de float "+Float.MIN_VALUE);
        
        double numDouble = 1.7976931348623157E308;
        System.out.println("numDouble = "+numDouble);
        System.out.println("valor máximo de double "+Double.MAX_VALUE);
        System.out.println("valor mínimo de double "+Double.MIN_VALUE);
    }
    
}
