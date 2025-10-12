public class Lingkaran {
    private double r; // atribut jari-jari

    // Constructor
    public Lingkaran(double r) {
        this.r = r;
    }

    // Method untuk menghitung luas
    public double hitungLuas() {
        return Math.PI * r * r;
    }

    // Method untuk menghitung keliling
    public double hitungKeliling() {
        return 2 * Math.PI * r;
    }

    // Method untuk menampilkan hasil
    public void tampilkanHasil() {
        System.out.println("Jari-jari lingkaran = " + r);
        System.out.println("Luas lingkaran      = " + hitungLuas());
        System.out.println("Keliling lingkaran  = " + hitungKeliling());
    }
}
