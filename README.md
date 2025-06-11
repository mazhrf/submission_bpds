# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut telah berdiri sejak tahun 2000, dikenal sebagai lembaga pendidikan dengan lulusan yang berkualitas. Namun, belakangan ini institusi menghadapi permasalahan serius terkait meningkatnya angka **dropout** mahasiswa. Tingginya jumlah mahasiswa yang tidak menyelesaikan studi berdampak negatif terhadap citra institusi serta mengganggu efektivitas operasionalnya.

### Permasalahan Bisnis

Tingginya tingkat dropout di Jaya Jaya Institut menunjukkan adanya sejumlah isu mendasar yang perlu segera diatasi:

* **Faktor Demografis:** Usia saat masuk dan latar belakang pendidikan sebelumnya turut berpengaruh terhadap kelulusan mahasiswa.
* **Kesulitan Akademik:** Sebagian mahasiswa mengalami hambatan dalam mengikuti kegiatan perkuliahan, yang terlihat dari rendahnya nilai dan banyaknya mata kuliah yang tidak lulus.
* **Permasalahan Finansial:** Kesulitan dalam membayar biaya pendidikan tepat waktu dapat menjadi salah satu penyebab utama terjadinya dropout.
* **Tidak Tersedianya Sistem Pemantauan Dini:** Belum terdapat sistem yang secara aktif memantau dan mengidentifikasi mahasiswa dengan potensi tinggi untuk mengalami dropout.
* **Kurangnya Ketertarikan atau Ketidaksesuaian Jurusan:** Mahasiswa mungkin kehilangan semangat belajar atau merasa tidak cocok dengan program studi yang dipilih.

Situasi ini membutuhkan solusi yang berbasis data agar institusi dapat melakukan intervensi yang lebih cepat, tepat sasaran, dan memberikan dampak nyata.

### Tujuan Proyek

Proyek ini dirancang untuk membantu Jaya Jaya Institut dalam mengurangi tingkat dropout mahasiswa melalui langkah-langkah berikut:

* **Mengungkap faktor-faktor kunci** yang berperan dalam meningkatkan risiko mahasiswa mengalami dropout.
* **Mengembangkan model prediksi berbasis *machine learning*** yang mampu mengenali potensi dropout sejak dini.
* **Menyediakan *dashboard* interaktif untuk keperluan manajerial**, guna memantau perkembangan mahasiswa dan mendukung perencanaan strategi intervensi secara proaktif.

### Cakupan Proyek

Proyek ini akan mencakup tahapan-tahapan berikut:

1. **Data Understanding**   
   Mengumpulkan informasi mahasiswa yang relevan serta memahami struktur, asal-usul, dan potensi isu kualitas data. Tahapan ini penting untuk memperoleh wawasan menyeluruh terhadap konteks data yang akan dianalisis.

3. **Data Preparation**   
   Melakukan pembersihan data dari nilai yang hilang (*missing values*), data yang menyimpang (*outliers*), serta ketidakkonsistenan. Data juga diproses lebih lanjut, seperti *encoding* variabel kategorikal dan normalisasi, agar siap untuk dianalisis dan dimodelkan.

5. **Exploratory Data Analysis (EDA)**   
   Melakukan analisis deskriptif dan visual untuk menemukan pola, tren, serta keterkaitan antar variabel. Tahap ini bertujuan untuk mengidentifikasi variabel-variabel penting yang dapat memengaruhi dropout.

7. **Modelling**   
   Memisahkan data menjadi bagian pelatihan dan pengujian, memilih algoritma yang tepat, melatih model dengan data pelatihan, serta melakukan penyetelan parameter (*hyperparameter tuning*) guna meningkatkan akurasi model.

9. **Evaluasi Model**   
    Menilai performa model dengan menggunakan data pengujian serta metrik evaluasi seperti akurasi, presisi, *recall*, dan F1-score untuk memilih model terbaik dalam memprediksi risiko dropout.

11. **Pembuatan Streamlit**   
    Merancang antarmuka sederhana berbasis Streamlit yang memungkinkan pengguna berinteraksi langsung dengan model, memasukkan data mahasiswa, dan memperoleh hasil prediksi secara *real-time*.

13. **Pengembangan Dashboard**   
    Membangun *dashboard* interaktif bagi manajemen akademik untuk memantau metrik dropout, mengevaluasi faktor risiko utama, serta meninjau prediksi model secara langsung.

15. **Dokumentasi dan Rekomendasi**   
    Menyusun laporan menyeluruh dari seluruh tahapan proyek, menyajikan temuan-temuan utama, serta memberikan saran berbasis data yang dapat diimplementasikan untuk menekan angka dropout.

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
![Dashboard 2](<ririee-dashboard3.png>)
![Dashboard 2](<ririee-dashboard4.png>)

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
