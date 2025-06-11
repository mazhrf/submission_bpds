# Proyek Akhir: Menyelesaikan Permasalahan Human Resources

## Business Understanding

PT Jaya Jaya Maju adalah perusahaan berskala internasional yang telah beroperasi lebih dari dua dekade (sejak tahun 2000) dengan tenaga kerja lebih dari 1.000 orang yang tersebar di berbagai lokasi. Meskipun perusahaan telah mencapai pertumbuhan yang menggembirakan dengan cakupan operasi yang luas, saat ini mereka menghadapi masalah serius dalam manajemen SDM, terutama terkait tingkat pengunduran diri karyawan (attrition rate) yang cukup tinggi, yaitu melebihi 10%.

Tingginya angka pengunduran diri ini menimbulkan beberapa konsekuensi negatif, antara lain gangguan pada operasional perusahaan, penurunan produktivitas, serta pembengkakan biaya untuk merekrut dan melatih karyawan pengganti. Untuk mengatasi masalah ini dan mendukung strategi retensi serta pertumbuhan berkelanjutan, PT Jaya Jaya Maju perlu melakukan analisis komprehensif untuk mengidentifikasi faktor-faktor utama yang menyebabkan karyawan memilih meninggalkan perusahaan.

### Permasalahan Bisnis

Divisi Sumber Daya Manusia PT Jaya Jaya Maju saat ini menghadapi beberapa kendala signifikan dalam mengelola tingkat pengunduran diri karyawan, meliputi:
- Kesulitan mengidentifikasi akar masalah pengunduran diri: Departemen HR belum memiliki pemahaman yang jelas mengenai faktor-faktor kunci yang mendorong karyawan memutuskan untuk meninggalkan perusahaan.
- Kurangnya wawasan tentang tren pengunduran diri: Belum tersedianya analisis data yang menunjukkan pola atau karakteristik umum dari karyawan yang cenderung mengundurkan diri.
- Sistem pemantauan yang belum efektif: Ketidakmampuan dalam melakukan pengawasan secara aktif dan tepat waktu terhadap indikator-indikator risiko pengunduran diri karyawan.
- Pengambilan keputusan yang belum berbasis data: Kebijakan dan strategi HR masih banyak yang belum didukung oleh analisis data yang mendalam dan menyeluruh.
- Ketiadaan mekanisme prediksi: Belum adanya model yang dapat memprediksi karyawan dengan risiko tinggi untuk mengundurkan diri, sehingga upaya pencegahan dini tidak dapat dilaksanakan dengan optimal.

### Tujuan Proyek

Untuk menjawab permasalahan bisnis tersebut, proyek ini bertujuan untuk:
- Menemukan faktor-faktor utama penyebab pengunduran diri: Melaksanakan analisis komprehensif terhadap informasi karyawan untuk mengungkap variabel-variabel yang memiliki korelasi kuat dengan tingkat pengunduran diri.
- Mengembangkan sistem prediksi berbasis machine learning: Merancang model klasifikasi dengan teknologi machine learning yang dapat mengestimasi probabilitas pengunduran diri setiap karyawan.
- Menciptakan dashboard pemantauan data : Menghadirkan visualisasi data yang informatif bagi departemen HR untuk memantau tren pengunduran diri secara langsung dengan pendekatan berbasis data.
- Menyediakan analisis mendalam dan saran praktis: Mempresentasikan temuan-temuan kunci dari hasil analisis dan prediksi untuk mendukung pengembangan strategi mempertahankan karyawan yang lebih efektif.

### Cakupan Proyek

Proyek ini akan mencakup tahapan-tahapan berikut:

1. **Data Understanding**   
   Mengumpulkan dan mempelajari data karyawan yang relevan untuk memahami struktur, sumber, dan potensi permasalahan kualitas data. Tahap ini bertujuan membangun pemahaman komprehensif mengenai konteks data yang akan dianalisis.

2. **Data Preparation**   
   Membersihkan data dari nilai hilang (*missing values*), pencilan (*outliers*), dan inkonsistensi.

3. **Exploratory Data Analysis (EDA)**   
   Menjalankan analisis statistik deskriptif dan membuat visualisasi untuk mengidentifikasi pola, kecenderungan, dan korelasi antar variabel. Fokus utama tahap ini adalah menemukan faktor-faktor yang berpotensi mempengaruhi *attrition*.

4. **Modelling**   
   Memisahkan dataset menjadi data untuk pelatihan dan pengujian. Menyeleksi algoritma yang tepat, melatih model dengan data pelatihan, dan melakukan optimasi parameter bila diperlukan untuk meningkatkan kinerja model.

5. **Evaluasi**   
   Menganalisis performa model menggunakan data pengujian dengan berbagai metrik evaluasi seperti akurasi, precision, recall, dan F1-score, untuk menentukan model terbaik dalam memprediksi risiko *attrition*.

6. **Pengembangan Dashboard**   
   Merancang dan mengembangkan panel pemantauan interaktif yang memudahkan tim HR untuk mengawasi indikator penting terkait pengunduran diri, mengeksplorasi faktor risiko utama, dan melihat hasil prediksi model secara langsung.

7. **Dokumentasi Laporan dan Rekomendasi**   
   Mendokumentasikan seluruh tahapan proyek, dari analisis hingga implementasi. Menyajikan temuan utama dan memberikan saran berbasis data yang dapat diterapkan oleh manajemen untuk mengurangi tingkat *attrition*.

### Persiapan

Sumber data: [Dataset Karyawan Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

**1. Run `notebook.ipynb`:**

  * **Instal Dependensi:** Pada terminal proyek, jalankan perintah berikut.
    ```
    pip install -r requirements.txt
    ```

  * **Jalankan Notebook:** Gunakan `jupyter notebook`, `jupyter lab` (lokal) atau unggah ke Google Colab dan jalankan semua sel.

**2. Run `prediction.py`:**

  * **Verifikasi dir. model:** Pastikan path model dan encoder di `prediction.py` sudah benar (Ubah jika perlu).
    ```
    model = joblib.load("model/model.pkl")
    encoder = joblib.load("model/encoder.pkl")
    ```
  
  * **Instal Dependensi (jika library belum terinstall):** 
    ```
    pip install pandas joblib scikit-learn
    ```
  
  * **Jalankan Skrip:** Pada terminal proyek, jalankan 
    ```
    python predict.py
    ```
    Hasil prediksi akan tampil sebagai output.

**3. Jalankan Dashboard (Metabase w/ Docker):**

  * **Instal Docker Desktop:** Unduh dan instal dari [www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
  * **Pindahkan Database:** Taruh `metabase.db.mv.db` pada direektori kerja.
  * **Tarik Image:** Pada terminal, jalankan 
    ```
    docker pull metabase/metabase:latest
    ```
  * **Jalankan Container:** Ganti `/path/into/your/dir` dengan path absolut menuju direktori `metabase.db.mv.db`:
    ```
    docker run -d -p 3000:3000 --name metabase -v /path/into/your/dir:/metabase-data metabase/metabase
    ```
  * **Akses Metabase:** Buka `http://localhost:3000` di browser.
  * **Login:** Email: `root@mail.com`, Password: `root123`.
  * **Hubungkan Database:** Tambahkan database H2. Path database di container: `/metabase-data/metabase.db.mv.db`.

## Business Dashboard

![Dashboard 1](<ririee-dashboard1.png>)
![Dashboard 2](<ririee-dashboard2.png>)

Dashboard ini dirancang untuk menampilkan visualisasi yang jelas dan informatif tentang berbagai aspek yang berkontribusi terhadap pengunduran diri karyawan di perusahaan Jaya Jaya Maju, sekaligus menyajikan prediksi mengenai karyawan yang berpotensi meninggalkan perusahaan.

**Komponen Utama Dashboard:**

1.  **Metriks Awal:**
    * **1,058 Total Karyawan:** Menunjukkan jumlah total karyawan saat ini dalam perusahaan, baik yang masih aktif bekerja maupun yang sudah resign.
    * **879 Total Karyawan yang Masih Bekerja:** Jumlah karyawan yang aktif bekerja.
    * **179 Total Karyawan yang Keluar:** Jumlah karyawan yang resign.
    * **Distribusi Employee berdasarkan Attrition:** Memvisualisasikan proporsi karyawan yang masih bekerja dan yang resign dari keseluruhan karyawan.
    * **252 Total Karyawan yang Berpotensi Keluar (>0.5):** Jumlah karyawan dengan potensi untuk keluar.
    * **22 Total Karyawan yang Berpotensi Tinggi Keluar (>0.6):** Jumlah karyawan yang memiliki chance/kemungkinan tinggi untuk keluar. Ini adalah kelompok yang perlu mendapatkan perhatian lebih.

2.  **Faktor-Faktor Penyebab Karyawan Keluar:**
    * Menampilkan 10 fitur atau faktor teratas yang paling berpengaruh terhadap keputusan karyawan untuk keluar. Berdasarkan visualisasi ini, **MonthlyIncome** (Gaji Bulanan) menjadi faktor yang paling signifikan, diikuti oleh **Age** (Usia) dan **TotalWorkingYears** (Total Tahun Bekerja).

3.  **Penyajian Data Berbagai Faktor:**
    * **Distribusi Monthly Income berdasarkan Attrition:** Distribusi gaji bulanan karyawan yang masih bekerja dan resign. Terlihat bahwa karyawan dengan rentang gaji yang rendah cenderung memilih resign dari perusahaan.
    * **Distribusi Age berdasarkan Attrition:** Distribusi usia karyawan yang masih bekerja dan resign. Faktor-U dapat menjadi insight bagi perusahaan.
    * **Distribusi TotalWorkingYears berdasarkan Attrition:** Distribusi pengabdian karyawan (dalam tahun) yang masih bekerja dan resign. Terlihat kecenderungan karyawan pada masa awal bekerja memiliki tingkat attrition yang lebih tinggi.
    * **Distribusi YearsAtCompany berdasarkan Attrition:** Distribusi lama bekerja karyawan (dalam tahun) yang masih bekerja dan resign. Terlihat kecenderungan karyawan pada masa awal bekerja memiliki tingkat attrition yang lebih tinggi.
    * **Distribusi OverTime berdasarkan Attrition:** Distribusi jumlah karyawan yang masih bekerja dan resign berdasarkan kebiasaan/tradisi perusahaan (lembur). Terlihat bahwa karyawan yang sering kena shift lembur cenderung memilih resign dibandingkan dengan yang tidak.
    * **Distribusi Gender berdasarkan Attrition:** Distribusi jumlah karyawan yang masih bekerja dan resign berdasarkan jenis kelamin. Terlihat bahwa proporsi pria lebih banyak daripada wanita.

## Conclusion

Proyek ini difokuskan untuk mengenali penyebab utama tingginya angka attrition karyawan di Jaya Jaya Maju dan menyediakan dashboard interaktif sebagai alat bantu visualisasi serta prediksi karyawan yang berisiko keluar.

Dari hasil analisis data dan model Random Forest hasil feature importance, gaji bulanan (MonthlyIncome) menjadi faktor prediktif terkuat terhadap attrition, diikuti oleh usia (Age), total tahun Bekerja (TotalWorkingYears), lama bekerja di perusahaan (YearsAtCompany) dan lingkungan kerja (EnvironmentSatisfaction). Fakrtor tersebut menunjukkan pengaruh yang cukup besar terhadap kecenderungan seorang karyawan meninggalkan perusahaan.

Model prediksi menunjukkan kinerja yang sangat baik dengan akurasi 95,23% serta metrik evaluasi lainnya seperti precision, recall, dan f1-score yang tinggi, menandakan bahwa model mampu membedakan dengan akurat antara karyawan yang bertahan dan yang keluar. Hasil classification report juga menunjukkan nilai precision, recall, dan f1-score yang tinggi untuk kedua kelas meenandakan model mampu mengklasifikasikan karyawan dengan baik.

*Dashboard* yang dikembangkan menampilkan data secara visual, memudahkan HR dalam melihat tren dan pola *attrition* berdasarkan berbagai aspek, serta mengidentifikasi karyawan dengan risiko tinggi secara real-time. Dashboard ini diharapkan dapat membantu departemen HR dalam memantau tren attrition, memahami faktor pendorongnya, dan mengambil langkah proaktif untuk mengurangi tingkat attrition.

### Rekomendasi Action Items (Optional)

Berdasarkan hasil temuan, berikut beberapa langkah *strategis* yang disarankan untuk Jaya Jaya Maju:

* **Evaluasi Skema Gaji:** Karena kompensasi menjadi faktor utama attrition, penting untuk mengevaluasi ulang struktur gaji dan memastikan daya saing di pasar tenaga kerja, terutama untuk posisi yang rawan *turnover*.
* **Program Engagement Karyawan Berdasarkan Usia dan Masa Kerja:** Mengembangkan program engagement yang ditargetkan untuk kelompok usia dan masa kerja tertentu yang menunjukkan tingkat *attrition* lebih tinggi. Misalnya, program pengembangan karir untuk karyawan muda atau program apresiasi untuk karyawan dengan masa kerja lebih pendek.
* **Atur Kebijakan Lembur Secara Bijak:** Perusahaan perlu memastikan beban kerja tidak berlebihan. Jika lembur tidak bisa dihindari, sediakan kompensasi atau fleksibilitas kerja sebagai bentuk apresiasi.
* **Analisis Faktor Tambahan:** Faktor seperti **StockOptionLevel**, **JobSatisfaction**, dan **YearsInCurrentRole** juga berpengaruh dan perlu dianalisis lebih lanjut untuk memahami konteks spesifik yang memicu *attrition*.
* **Lakukan Pendekatan pada Karyawan Berisiko Tinggi:** Gunakan hasil prediksi model untuk melakukan intervensi personal, seperti diskusi one-on-one atau penawaran insentif agar mereka merasa dihargai dan tetap bertahan.
