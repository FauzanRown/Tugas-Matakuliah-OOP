// Kelas Main.java
public class Main {
    public static void main(String[] args) {
        // Membuat 3 objek NovelDetektif
        NovelDetektif novel1 = new NovelDetektif("Pembunuhan di Orient Express", "Agatha Christie", 1934, 120000);
        NovelDetektif novel2 = new NovelDetektif("Sherlock Holmes: A Study in Scarlet", "Arthur Conan Doyle", 1887, 95000);
        NovelDetektif novel3 = new NovelDetektif("Detective Conan Vol.1", "Gosho Aoyama", 1994, 70000);

        // Menampilkan informasi setiap novel
        novel1.tampilkanInfo();
        novel2.tampilkanInfo();
        novel3.tampilkanInfo();

        // Menghitung total harga beli dan harga jual semua buku
        double totalBeli = novel1.getHargaBeli() + novel2.getHargaBeli() + novel3.getHargaBeli();
        double totalJual = novel1.hitungHargaJual() + novel2.hitungHargaJual() + novel3.hitungHargaJual();

        // Menampilkan hasil total
        System.out.println("Total Harga Beli Semua Buku: Rp" + totalBeli);
        System.out.println("Total Harga Jual Semua Buku: Rp" + totalJual);
    }
}
