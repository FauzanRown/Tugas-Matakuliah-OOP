public class NilaiArray {
    public static void main(String[] args) {
        int[] angka = {12, 45, 7, 23, 89}; // array berisi 5 angka

        int terbesar = angka[0];
        int terkecil = angka[0];

        // perulangan untuk mencari nilai terbesar dan terkecil
        for (int i = 1; i < angka.length; i++) {
            if (angka[i] > terbesar) {
                terbesar = angka[i];
            }
            if (angka[i] < terkecil) {
                terkecil = angka[i];
            }
        }

        System.out.println("Nilai terbesar: " + terbesar);
        System.out.println("Nilai terkecil: " + terkecil);
    }
}
