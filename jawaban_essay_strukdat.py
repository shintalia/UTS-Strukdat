from fpdf import FPDF

# Fungsi untuk menghapus karakter yang tidak bisa diencode ke latin-1
def bersihkan_teks(teks):
    return teks.encode('latin-1', 'ignore').decode('latin-1')

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=12)

# Judul
pdf.set_font("Times", "B", 16)
pdf.cell(200, 10, txt="UTS - Struktur Data", ln=True, align="C")
pdf.ln(10)

# Kembali ke font isi
pdf.set_font("Times", size=12)

isi = [
    "1. Pengertian Struktur Data :",
    "Struktur data adalah metode atau teknik untuk mengorganisir, menyimpan, dan mengelola data dalam",
    "komputer agar dapat diperlakukan efisien. Struktur data memungkinkan kita untuk memanipulasi dan mengakses",
    "data dalam suatu cara yang lebih struktur dan sistematis, sehingga kebingungan ketika mengerjakan",
    "algoritma serta aplikasi berkurang.",
    "",

    "2. Kegunaan Struktur Data :",
    "A). Pengorganisasian Data : Struktur data berfungsi untuk mengorganisir",
    "data dalam cara yang teratur sehingga mempermudah penyimpanan dan penangkapan informasi.",
    "B). Efisiensi Akses dan Manipulasi Data : Struktur data yang tepat memungkinkan akses",
    "dan manipulasi data lebih cepat.",
    "C). Manajemen Memori : Struktur data menyokong pengelolaan memori dengan lebih efisien.",
    "Beberapa struktur data, seperti daftar yang terhubung, menyokong penggunaan memori dinamis,",
    "di mana memori dapat diaktifkan dan dibebaskan tergantung pada keperluan.",
    "D). Implementasi Algoritma : sebagian besar algoritma tergantung pada struktur data yang tepat",
    "agar dapat berjalan efektif. Contohnya, pencarian dan pengurutan menggunakan struktur data",
    "seperti array, tree, atau graph untuk menyebabkan hasil yang optimal.",
    "E). Mewakili Hubungan : Struktur data seperti grafik digunakan untuk merepresentasikan hubungan",
    "kompleks antara data, seperti jaringan sosial, peta, atau sistem transportasi.",
    "Ini memungkinkan analisis dan pemodelan yang lebih baik terhadap hubungan tersebut.",
    "",
    
    "3. Jenis-jenis struktur data dan jelaskan :",
    "A). Array susunan adalah kumpulan data yang berisi beberapa elemen dengan tipe data",
    "serupa dan disimpan dalam memori dengan cara yang mudah dipahami.",
    "B). Daftar tertaut adalah kumpulan elemen (juga disebut simpul) yang terhubung",
    "satu sama lain secara terus-menerus melalui sebuah penunjuk.",
    "C). Stack menggunakan prinsip Last In, First Out (LIFO), yaitu data yang dimasukkan terakhir akan diakses lebih dulu.",
    "D). Antrean menggunakan prinsip First In, First Out (FIFO), yaitu data yang masuk lebih awal diproses lebih dulu.",
    "E). Pohon adalah struktur data hierarkis yang terdiri dari node, dengan satu node sebagai akar dan lainnya sebagai anak/cabang.",
    "",
    "4. Apa itu array dan kegunaannya :",
    "Array adalah kumpulan data yang memiliki tipe data sama dan disimpan secara berurutan dalam memori.",
    "Kegunaan: Menyimpan Banyak Data Sekaligus, Mengakses Data dengan Indeks, Mempermudah Pengulangan,",
    "Mengelompokkan Data Berkaitan.",
    "",

    "5. Contoh array :",
    "- Jadwal Mata kuliah",
    "- Nilai Ujian",
    "- Daftar Tugas",
    "",

    "6. Program :",
    "# Daftar mobil dan harganya (dalam juta Rupiah)",
    "mobil = {",
    '    "BMW": 1500,        # Rp 1.500.000.000',
    '    "Ferrari": 4000,    # Rp 4.000.000.000',
    '    "Lamborghini": 6000,# Rp 6.000.000.000',
    '    "Mercedes": 2000    # Rp 2.000.000.000',
    "}",
    "# Menampilkan semua mobil dan harganya",
    'print("Daftar Mobil dan Harganya:")',
    "for nama, harga in mobil.items():",
    '    print(f"{nama}: Rp {harga:,} juta")',
]

for baris in isi:
    pdf.multi_cell(0, 10, txt=bersihkan_teks(baris))

pdf.output("Jawaban_UTS_Essay-Deshinta_Pracilia.pdf")
print("Jawaban_UTS_Essay-Deshinta_Pracilia.pdf berhasil dibuat.")