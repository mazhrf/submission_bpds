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

Sumber data: [Dataset Mahasiswa Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:

**1. Run `notebook.ipynb`:**

  * **Instal Dependensi:** Pada terminal proyek, jalankan perintah berikut.
    ```
    pip install -r requirements.txt
    ```

  * **Jalankan Notebook:** Gunakan `jupyter notebook`, `jupyter lab` (lokal) atau unggah ke Google Colab dan jalankan semua sel.

**2. Run Streamlit App (`app.py`):**

   * **Model :**  file model (`model.pkl`) dan encoder (`encoder.pkl`) berada di dalam folder `model/` pada direktori proyek Anda.
   * **Instal Streamlit (jika belum):**
     ```bash
     pip install streamlit
     ```
   * **Jalankan Aplikasi:** Di terminal proyek, jalankan:
     ```bash
     streamlit run app.py
     ```

     Aplikasi Streamlit akan terbuka di *browser* Anda.

**3. Jalankan Dashboard (Metabase w/ Docker):**

  * **Instal Docker Desktop:** Unduh dan instal dari [www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
  * **Pindahkan Database:** Taruh `metabase.db.mv.db` pada direktori kerja.
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

Dashboard ini dibuat menggunakan Metabase dan berperan sebagai media visualisasi interaktif untuk memantau kinerja mahasiswa serta mengidentifikasi faktor-faktor yang mempengaruhi tingkat *dropout*. Menyajikan informasi menyeluruh terkait kondisi mahasiswa dan indikator-indikator penting yang relevan.

### Komponen Utama Dashboard:

1.  **Statistik Umum Mahasiswa:**
    * **Total Mahasiswa:** Sebanyak 4.424 mahasiswa tercatat dalam sistem.
    * **Mahasiswa Terdaftar (Aktif):** 794 mahasiswa sedang aktif menempuh studi.
    * **Mahasiswa Lulus:** 2.209 mahasiswa telah menyelesaikan seluruh kewajiban akademik.
    * **Mahasiswa Keluar:** 1.421 mahasiswa tercatat keluar dari perguruan tinggi, baik karena mengundurkan diri maupun sebab lainnya.
    * **Mahasiswa Berpotensi Dropout (>0.5):** 125 mahasiswa terdeteksi memiliki potensi tinggi untuk keluar.
    * **Mahasiswa dengan Risiko Dropout Sangat Tinggi (>0.6):** Sebanyak 48 mahasiswa berada pada tingkat risiko paling tinggi dan memerlukan perhatian lebih.

2.  **Faktor-Faktor Utama Penyebab Mahasiswa Dropout:**
    * Menampilkan 10 fitur teratas yang paling berkontribusi terhadap kemungkinan mahasiswa keluar, berdasarkan hasil pemodelan analitik. Faktor paling berpengaruh di antaranya:
        1. `Curricular_units_2nd_sem_approved`
        2. `Curricular_units_2nd_sem_grade`
        3. `Curricular_units_1st_sem_approved`
        4. `Curricular_units_1st_sem_grade`
        5. `Age_at_enrollment`
        6. `Tuition_fees_up_to_date`
        7. `Scholarship_holder`
        8. `Debtor`
        9. `Gender_Male`
        10. `Course_Animation and Multimedia Design`
    
    * Faktor-faktor ini menjadi perhatian utama dalam upaya mitigasi risiko dropout.

3.  **Distribusi Mahasiswa Berdasarkan Status:**
    * Visualisasi menampilkan proporsi mahasiswa berdasarkan status mereka:
        * **Graduate (Lulus):** 2.209 mahasiswa (50%)
        * **Enrolled (Masih Terdaftar):** 794 mahasiswa (18%)
        * **Dropout (Keluar):** 1.421 mahasiswa (32%)

    * Total keseluruhan mahasiswa ditampilkan pada bagian tengah diagram sebagai indikator utama.

### Insight Dashboard:
Dashboard ini secara komprehensif mengungkap bahwa **faktor akademik** memiliki pengaruh dominan terhadap potensi mahasiswa mengalami *dropout* di Jaya Jaya Institut. Secara spesifik, jumlah unit kurikuler yang disetujui dan nilai akademik pada semester pertama dan kedua muncul sebagai indikator paling signifikan. Hal ini mencerminkan bahwa performa awal mahasiswa di masa-masa awal perkuliahan sangat menentukan keberlanjutan studi mereka. Mahasiswa dengan pencapaian rendah di semester awal cenderung memiliki risiko lebih tinggi untuk tidak menyelesaikan pendidikannya. Selain performa akademik, `Age_at_enrollment` juga menjadi faktor penting. Data menunjukkan bahwa mahasiswa yang berusia lebih muda saat masuk perguruan tinggi memiliki kemungkinan lebih besar untuk *dropout*. Hal ini dapat disebabkan oleh kurangnya kematangan emosional, kesulitan beradaptasi dengan lingkungan perguruan tinggi, atau beban akademik yang tidak sesuai dengan ekspektasi. Faktor-faktor non-akademik seperti status keuangan mahasiswa — apakah mereka menerima beasiswa (`Scholarship_holder`) atau memiliki tanggungan hutang (`Debtor`) — serta keteraturan dalam pembayaran biaya kuliah (`Tuition_fees_up_to_date`) turut memberikan kontribusi terhadap risiko *dropout*. Meskipun demikian, dampak dari faktor-faktor ini cenderung lebih kecil jika dibandingkan dengan pengaruh performa akademik. Artinya, masalah akademik lebih sering menjadi alasan utama dibandingkan tekanan finansial. Distribusi *dropout* berdasarkan gender menunjukkan perbedaan yang tidak signifikan, menandakan bahwa risiko ini terjadi secara relatif merata antara mahasiswa laki-laki dan perempuan. Upaya seperti pemantauan rutin terhadap nilai dan penyelesaian unit, pemberian bimbingan akademik secara berkala, serta program pendampingan bagi mahasiswa baru dapat menjadi solusi preventif yang efektif. Di samping itu, perhatian terhadap kondisi keuangan mahasiswa — seperti pemberian bantuan atau keringanan biaya — tetap menjadi aspek penting untuk mengurangi hambatan dalam menyelesaikan studi. Kesimpulannya, untuk menurunkan tingkat *dropout*, diperlukan pendekatan yang menyeluruh dan berkelanjutan yang mencakup dukungan **akademik**, **emosional**, dan **finansial** bagi mahasiswa selama masa studi mereka.

## Menjalankan Prototype Machine Learning w/ Streamlit

Prototype sistem *machine learning* ini dirancang untuk memprediksi apakah seorang mahasiswa di Jaya Jaya Institut berpotensi mengalami *dropout* atau tidak, berdasarkan data individual mahasiswa yang dimasukkan oleh pengguna.

### Step-By-Step:

1. Anda dapat mengakses prototype melalui tautan berikut: [here](https://ririe-submission-bpds2.streamlit.app)

2. **Isi semua kolom input** yang tersedia di antarmuka aplikasi. Data yang diminta dikelompokkan dalam beberapa bagian sebagai berikut:

   * **Informasi Umum Mahasiswa (Bagian Atas):**
     - `Application Mode`: Tentukan jenis jalur pendaftaran mahasiswa.
     - `Course`: Pilih program studi yang sedang diambil.
     - `Gender`: Tentukan jenis kelamin mahasiswa.
     - `Previous Qualification`: Pilih jenjang pendidikan terakhir sebelum masuk perguruan tinggi.
     - `Age at Enrollment`: Atur usia mahasiswa saat pertama kali terdaftar menggunakan *slider*.

   * **Kinerja Akademik Semester 2 (Bagian Kanan Atas):**
     - `2nd Sem Units Approved`: Jumlah unit kurikuler yang berhasil diselesaikan di semester kedua.
     - `2nd Sem Grade`: Rata-rata nilai yang diperoleh mahasiswa pada semester kedua.

   * **Kinerja Akademik Semester 1 (Bagian Kanan Tengah):**
     - `1st Sem Units Approved`: Jumlah unit kurikuler yang diselesaikan pada semester pertama.
     - `1st Sem Grade`: Rata-rata nilai akademik pada semester pertama.

   * **Kondisi Finansial Mahasiswa (Bagian Bawah):**
     - `Tuition Fees Up to Date?`: Masukkan 1 jika pembayaran biaya kuliah sudah lunas, 0 jika belum.
     - `Scholarship Holder?`: Masukkan 1 jika mahasiswa merupakan penerima beasiswa, 0 jika bukan.
     - `Debtor?`: Masukkan 1 jika mahasiswa memiliki utang biaya kuliah, 0 jika tidak.

3. **Tekan tombol “Prediksi”** untuk melihat hasil.

Sistem akan segera memproses data yang dimasukkan menggunakan model *machine learning* yang sudah dilatih. Hasil prediksi akan ditampilkan di bagian bawah halaman beserta probability.

### Teknis Singkat Prototype:

- Aplikasi ini dikembangkan menggunakan *framework* Streamlit, yang memudahkan integrasi antara model *machine learning* berbasis Python dengan antarmuka pengguna yang interaktif.
- Model prediktif yang digunakan telah dilatih menggunakan data historis mahasiswa untuk mendeteksi pola-pola yang berkaitan dengan *dropout*.
- Data input yang diisi oleh pengguna akan dikonversi (di-*encode*) menjadi format numerik dan kategorikal agar kompatibel dengan model.
- Model kemudian memproses data dan menampilkan prediksi status mahasiswa secara langsung melalui antarmuka Streamlit.

## Conclusion

Proyek ini berhasil mengembangkan sistem deteksi dini risiko *dropout* mahasiswa di Jaya Jaya Institut, sebagai bagian dari upaya strategis menekan angka putus studi. Dengan memanfaatkan data historis mahasiswa, kami membangun model *machine learning* prediktif berbasis **Random Forest**, yang terintegrasi dengan *business dashboard* interaktif untuk menyajikan wawasan mendalam bagi pengambil keputusan. Model dievaluasi menggunakan data uji (`X_test_scaled`, `y_test`) dan menghasilkan performa yang sangat baik dan seimbang antara kedua kelas, yaitu mahasiswa yang *dropout* dan yang tidak.

**Hasil Evaluasi:**
- **Accuracy**: 0.9434 (sekitar 94.34% data uji berhasil diprediksi dengan benar)
- **ROC AUC Score**: 0.9786 — menunjukkan kemampuan model dalam membedakan mahasiswa yang berisiko *dropout* dan yang tidak tergolong sangat tinggi.

**Classification Report:**

| Kelas | Keterangan              | Precision | Recall | F1-Score | Support |
|-------|--------------------------|-----------|--------|----------|---------|
| 0     | Dropout                  | 0.92      | 0.97   | 0.94     | 601     |
| 1     | Enrolled & Graduate      | 0.97      | 0.92   | 0.94     | 601     |

- **Macro Average F1-Score**: 0.94  
- **Weighted Average F1-Score**: 0.94

Hasil ini menunjukkan bahwa model mampu mengklasifikasikan kedua kelas secara seimbang, dengan nilai *precision* dan *recall* yang konsisten tinggi.

Berdasarkan analisis *feature importance*, model mengidentifikasi bahwa:
- **Faktor akademik** (khususnya jumlah unit yang disetujui dan nilai pada semester 1 dan 2) merupakan prediktor paling berpengaruh terhadap potensi *dropout* mahasiswa.
- Temuan ini konsisten dengan pola pada dashboard, yang menunjukkan mahasiswa dengan nilai dan unit rendah memiliki risiko *dropout* lebih tinggi.
- Faktor non-akademik seperti `Age_at_enrollment`, `Tuition_fees_up_to_date`, `Scholarship_holder`, dan `Debtor` juga berkontribusi dalam prediksi, namun dampaknya relatif lebih kecil dibandingkan faktor akademik.

### Rekomendasi Action Items

Berdasarkan hasil evaluasi model dan temuan dalam proyek, berikut sejumlah langkah strategis yang dapat diterapkan oleh Jaya Jaya Institut untuk menurunkan tingkat *dropout* mahasiswa:

* **Optimalisasi Sistem Prediksi:**
    * Terapkan prototipe berbasis Streamlit ke dalam sistem akademik guna memantau risiko *dropout* mahasiswa secara *real-time*.
    * Manfaatkan *business dashboard* secara berkala untuk mengevaluasi pola *dropout*, menilai efektivitas intervensi, dan menyusun strategi berbasis data.

* **Penguatan Dukungan Finansial dan Konseling:**
    * Evaluasi dan perluas cakupan program bantuan biaya pendidikan bagi mahasiswa yang bukan `Scholarship_holder`, memiliki tunggakan `Tuition_fees_up_to_date`, atau berstatus `Debtor`.
    * Tawarkan layanan konseling keuangan untuk membantu mahasiswa menyusun rencana pembayaran dan menyelesaikan masalah keuangan.

* **Intervensi Dini terhadap Risiko Akademik:**
    * Identifikasi mahasiswa dengan nilai dan jumlah unit rendah di semester awal (`Curricular_units_1st_sem_grade`, `Curricular_units_1st_sem_approved`, `Curricular_units_2nd_sem_grade`, `Curricular_units_2nd_sem_approved`) sebagai target utama intervensi.
    * Sediakan dukungan berupa bimbingan akademik, program belajar tambahan, atau *peer tutoring* bagi mahasiswa dengan performa awal yang lemah.
    * Lakukan pemantauan berkala melalui dashboard untuk memastikan mahasiswa berisiko menerima dukungan tepat waktu.

* **Program Adaptasi Mahasiswa Baru:**
    * Kembangkan program orientasi dan adaptasi yang lebih menyeluruh untuk mahasiswa dengan `Age_at_enrollment` yang rendah, guna membantu mereka bertransisi ke lingkungan perkuliahan.
    * Tawarkan pendampingan ekstra bagi mahasiswa yang mendaftar melalui `Application_mode` tertentu yang menunjukkan tingkat *dropout* lebih tinggi, seperti `2nd Phase - General Contingent`.

* **Evaluasi Program Studi dan Pengajaran:**
    * Lakukan kajian terhadap mata kuliah dan `Course` yang mencatat angka *dropout* tinggi untuk mengidentifikasi perbaikan yang mungkin dibutuhkan dalam kurikulum atau metode pengajaran.
    * Pastikan kualitas pembelajaran terjaga untuk mempertahankan motivasi dan hasil belajar mahasiswa.

Dengan menjalankan rekomendasi-rekomendasi ini, diharapkan Jaya Jaya Institut dapat menciptakan lingkungan akademik yang lebih suportif dan mendorong keberhasilan studi mahasiswa secara lebih merata.
