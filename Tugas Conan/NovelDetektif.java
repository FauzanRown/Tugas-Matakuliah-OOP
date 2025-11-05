// Kelas NovelDetektif.java
public class NovelDetektif {
    // Atribut privat (enkapsulasi)
    private String judul;
    private String pengarang;
    private int tahunTerbit;
    private double hargaBeli;

    // Constructor
    public NovelDetektif(String judul, String pengarang, int tahunTerbit, double hargaBeli) {
        this.judul = judul;
        this.pengarang = pengarang;
        this.tahunTerbit = tahunTerbit;
        this.hargaBeli = hargaBeli;
    }

    // Getter dan Setter
    public String getJudul() {
        return judul;
    }

    public void setJudul(String judul) {
        this.judul = judul;
    }

    public String getPengarang() {
        return pengarang;
    }

    public void setPengarang(String pengarang) {
        this.pengarang = pengarang;
    }

    public int getTahunTerbit() {
        return tahunTerbit;
    }

    public void setTahunTerbit(int tahunTerbit) {
        this.tahunTerbit = tahunTerbit;
    }

    public double getHargaBeli() {
        return hargaBeli;
    }

    public void setHargaBeli(double hargaBeli) {
        this.hargaBeli = hargaBeli;
    }

    // Method untuk menghitung harga jual
    public double hitungHargaJual() {
        return hargaBeli - (0.2 * hargaBeli); // harga jual = harga beli - 20%
    }

    // Method untuk menampilkan informasi novel
    public void tampilkanInfo() {
        System.out.println("Judul       : " + judul);
        System.out.println("Pengarang   : " + pengarang);
        System.out.println("Tahun Terbit: " + tahunTerbit);
        System.out.println("Harga Beli  : Rp" + hargaBeli);
        System.out.println("Harga Jual  : Rp" + hitungHargaJual());
        System.out.println("-----------------------------------");
    }
}
