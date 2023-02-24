public class DecimalToGray {
    public static void main(String[] args) {
        int decimal = 7;
        int gray = decimal ^ (decimal >> 1);
        System.out.println("The gray code of " + decimal + " is " + gray);
    }
}

  