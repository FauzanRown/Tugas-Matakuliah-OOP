class PersegiPanjang {
    int panjang;
    int lebar;

    // Constructor
    PersegiPanjang(int p, int l) {  //! ✅ Nama constructor WAJIB sama dengan nama class
        panjang = p;
        lebar = l;
    }

    void CetakPerhitungan(){
        System.out.println("Luas Persegi Panjang: " + (panjang * lebar));
        System.out.println("Keliling Persegi Panjang " + panjang * 2 + lebar * 2);
        System.out.println("-------------------------");
    }
}

class Persegi {
    int sisi;

    // Constructor
    Persegi(int s) {
        sisi = s;
    }

    void CetakPerhitungan(){
        System.out.println("Luas Persegi: " + (sisi * sisi));
        System.out.println("Keliling Persegi: " + (sisi * 4));
        System.out.println("-------------------------");
    }
}

class Segitiga {
    int alas;
    int tinggi;

    // Constructor
    Segitiga(int a, int t) {
        alas = a;
        tinggi = t;
    }

    void CetakPerhitungan(){
        System.out.println("Luas Segitiga: " + (0.5 * alas * tinggi));
        System.out.println("Keliling Segitiga: " + (alas + tinggi + Math.sqrt(alas*alas + tinggi*tinggi)));
        System.out.println("-------------------------");
    }
}

class JajarGenjnagg {
    int panjang;
    int lebar;
    int tinggi;

    // Constructor
    JajarGenjnag(int p, int l, int t) {
        panjang = p;
        lebar = l;
        tinggi = t;
    }

    void CetakPerhitungan(){
        System.out.println("Luas Jajar Genjang: " + (panjang * tinggi));
        System.out.println("Keliling Jajar Genjang: " + (2 * (panjang + lebar)));
        System.out.println("-------------------------");
    }
}

class kubus {
    int sisi;

    // Constructor
    kubus(int s) {
        sisi = s;
    }

    void CetakPerhitungan(){
        System.out.println("Luas Kubus: " + (6 * sisi * sisi));
        System.out.println("Volume Kubus: " + (sisi * sisi * sisi));
        System.out.println("-------------------------");
    }
}

public class CetakHasil {
    public static void main(String[] args) {
        // 🔹 Constructor dipanggil secara otomatis saat membuat objek baru
        PersegiPanjang bentuk1 = new PersegiPanjang(10,40);
        bentuk1.CetakPerhitungan();

        Persegi bentuk2 = new Persegi(10);
        bentuk2.CetakPerhitungan();

        Segitiga bentuk3 = new Segitiga(10,40);
        bentuk3.CetakPerhitungan();

        JajarGenjnagg bentuk4 = new JajarGenjnagg(10,40,20);
        bentuk4.CetakPerhitungan();

        kubus bentuk5 = new kubus(10);
        bentuk5.CetakPerhitungan();
    }
}
