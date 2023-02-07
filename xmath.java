public class xmath {
    private static final double Eplison = 0.000001;

    public static double add(double x, double y) {
        return x + y;
    }

    public static double minus(double x, double y) {
        return x - y;
    }

    public static double multiply(double x, double y) {
        return x * y;
    }

    public static double divide(double x, double y) {
        return x / y;
    }

    public static double power(double x, double y) {
        return Math.pow(x, y);
    }

    public static double root(double x, double y) {
        return Math.pow(x, 1 / y);
    }

    public static double bigger(double x, double y) {
        if (x > y) {
            return x;
        } else {
            return y;
        }
    }

    public static double smaller(double x, double y) {
        if (x < y) {
            return x;
        } else {
            return y;
        }
    }

    public static boolean isEqual(double x, double y) {
        if (x - y < Eplison && y - x < Eplison) {
            return true;
        } else {
            return false;
        }
    }

    
    public static long factorial(int num) {
        long result;
        if (num > 1) {
            result = num * factorial(num - 1);
        } else {
            result = 1;
        }
        return result;
    }
}