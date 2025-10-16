class Pecahan {
    int pembilang;
    int penyebut;

    // Constructor 
    Pecahan(int pembilang, int penyebut) { // ! mengacu pada parameter
        this.pembilang = pembilang;
        this.penyebut = penyebut;
    }

    // Menampilkan pecahan
    void tampilkan() {
        System.out.println(pembilang + "/" + penyebut);
    }
    
}


// Class OperasiPecahan
class OperasiPecahan {

    Pecahan tambah(Pecahan a, Pecahan b) { // ! Pecahan Nama class a, b sebagai nama objek
        int pembilangBaru = (a.pembilang * b.penyebut) + (b.pembilang * a.penyebut);
        int penyebutBaru = a.penyebut * b.penyebut;
        return new Pecahan(pembilangBaru, penyebutBaru);
    }

    Pecahan kurang(Pecahan a, Pecahan b) {
        int pembilangBaru = (a.pembilang * b.penyebut) - (b.pembilang * a.penyebut);
        int penyebutBaru = a.penyebut * b.penyebut;
        return new Pecahan(pembilangBaru, penyebutBaru);
    }

    Pecahan kali(Pecahan a, Pecahan b) {
        int pembilangBaru = a.pembilang * b.pembilang;
        int penyebutBaru = a.penyebut * b.penyebut;
        return new Pecahan(pembilangBaru, penyebutBaru);
    }

    Pecahan bagi(Pecahan a, Pecahan b) {
        int pembilangBaru = a.pembilang * b.penyebut;
        int penyebutBaru = a.penyebut * b.pembilang;
        return new Pecahan(pembilangBaru, penyebutBaru);
    }
}

// Class Main (Program Utama)
public class HasilPecahan {
    public static void main(String[] args) {
        Pecahan p1 = new Pecahan(1, 2);
        Pecahan p2 = new Pecahan(3, 4);
        OperasiPecahan op = new OperasiPecahan();

        System.out.print("P1 = ");
        p1.tampilkan();
        System.out.print("P2 = ");
        p2.tampilkan();

        System.out.println("\nHasil Operasi:");
        op.tambah(p1, p2).tampilkan(); // Tambah
        op.kurang(p1, p2).tampilkan(); // Kurang
        op.kali(p1, p2).tampilkan();   // Kali
        op.bagi(p1, p2).tampilkan();   // Bagi
    }
}

