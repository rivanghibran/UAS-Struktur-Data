﻿# Soal UAS-Struktur-Data 2024 
 
Tugas Final
Struktur Data 
Semester Genap T.A. 2023/2024

Anda tergabung dalam divisi IT suatu perusahaan retail yang baru saja berdiri. Anda bertanggung jawab untuk pengelolaan 2 data yaitu data stok barang dan data transaksi konsumen. Karena perusahaan baru saja berdiri Anda diminta mengembangkan program sederhana dengan ketentuan sebagai berikut.

1.Program dibuat dalam bentuk Menu.
2.Terdapat 2 Menu utama saat program pertama kali dijalankan yaitu
      1) Kelola Stok Barang dan
      2) Kelola Transaksi Konsumen, ditambah lagi satu menu untuk keluar dari program 0) Exit Program.
3.Jika Menu 1) Kelola Stok Barang dipilih maka akan ada 2 sub menu (dan 1 tambahan menu kembali ke MENU UTAMA) yaitu:
      1.1) Input Data Stok Barang
      1.2) Restok Barang
4.Jika Menu 2) Kelola Transaksi Konsumen dipilih maka akan ada 3 (dan 1 tambahan menu kembali ke MENU UTAMA) sub menu yaitu:
      2.1) Input Data Transaksi Baru
      2.2) Lihat Data Seluruh Transaksi Konsumen
      2.3) Lihat Data Transaksi Berdasarkan Subtotal
5.Jika Menu 0) Exit Program yang dipilih maka sistem akan berhenti melakukan perulangan menampilkan menu dan program akan berhenti.
Diagram jenjang untuk sistem yang dibangung adalah sebagai berikut:

Detil penjelasan sistem untuk masing--masing menu diatur sebagai berikut:

Menu 1.1 Input Data Stok Barang
      1.Data Stok Barang disimpan ke dalam struktur data Binary Search Tree (BST).
      2.Atribut yang disimpan untuk 1 data adalah: No. SKU; Nama Barang; Harga Satuan; Jumlah Stok.
      3.Proses insert ke dalam BST berdasarkan No. SKU.
      4.No. SKU adalah kode unik untuk setiap barang dan terdiri darai 4 digit Angka.
      5.Saat proses input data stok barang seluruh atribut (pada poin no.2) akan diinputkan oleh user melalui keyboard.
      6.Saat proses input akan dilakukan pengecekan apakah No. SKU sudah tersimpan di dalam BST.
            Jika No. SKU SUDAH TERSIMPAN di BST: sistem akan menolak permintaan input data dari user
            Jika No. SKU BELUM TERSIMPAN di BST: sistem akan menyimpan permintaan input data dari user ke BST.
            
Menu 1.2 Restok Barang
      1.Menu Restok Barang akan meng--update stok barang yang tersimpan di dalam BST sesuai dengan No. SKU yang diinputkan oleh user melalui keyboard.
      2.Proses Restok Barang dimulai dengan user mamasukkan No. SKU dari barang yang akan diupdate.
            Jika No. SKU SUDAH TERSIMPAN di BST: sistem akan meminta user memasukkan jumlah stok baru yang akan ditambahkan ke data barang tersebut
            Jika No. SKU BELUM TERSIMPAN di BST: sistem akan menolak permintaan Restok Barang dan menyarankan user untuk melakukan input data stok barang terlebih              dahulu.
      3.Setelah user memasukkan jumlah stok baru yang akan ditambahkan ke data barang tersebut, sistem akan menghitung total stok barang dengan rumus:
      𝒕𝒐𝒕𝒂𝒍 𝒔𝒕𝒐𝒌 𝒃𝒂𝒓𝒂𝒏𝒈 = 𝒔𝒕𝒐𝒌 𝒍𝒂𝒎𝒂 + 𝒔𝒕𝒐𝒌 𝒃𝒂𝒓𝒖
      dimana stok lama adalah atribut jumlah stok yang tersimpan di BST daan stok baru adalah jumlah stok yang diinputkan user melalui keyboard.
      4.Setelah perhitungan total stok dilakukan, sistem kemudian akan mengupdate jumlah stok barang dengan No. SKU tersebut dengan hasil perhitungan total stok.
      Menu 2.1 Input Data Transaksi Baru
      1.Data Transaksi Baru disimpan ke dalam struktur data Array atau List.
      2.Atribut yang disimpan untuk 1 data adalah :
      Nama Konsumen; No. SKU barang yang dibeli; Jumlah Beli; Subtotal
      3.Proses insert ke dalam Array/List hanya membutuhkan inputan 3 atribut dari keyboard user yaitu Nama Konsumen; No. SKU barang yang dibeli; dan Jumlah Beli.          Sedangkan Subtotal didapatkan dari hasil perhitungan dengan rumus berikut:
      𝑺𝒖𝒃𝒕𝒐𝒕𝒂𝒍= 𝑯𝒂𝒓𝒈𝒂 𝑺𝒂𝒕𝒖𝒂𝒏 𝑩𝒂𝒓𝒂𝒏𝒈 𝒚𝒂𝒏𝒈 𝒅𝒊𝒃𝒆𝒍𝒊 × 𝑱𝒖𝒎𝒍𝒂𝒉 𝑩𝒆𝒍𝒊
      4.Saat proses input data transaksi baru mula--mula user memasukkan Nama Konsumen. Proses memasukkan nama konsumen hanya terjadi 1x di awal.
      5.Setelah memasukkan Nama Konsumen, user akan memasukkan No. SKU barang yang dibeli oleh konsumen tersebut.
            Jika No. SKU SUDAH TERSIMPAN di BST: sistem akan meminta user memasukkan jumlah barang yang dibeli.
            Jika No. SKU BELUM TERSIMPAN di BST: sistem akan memunculkan pesan “No. SKU yang diinputkan belum terdaftar” dan meminta user memilih “Apakah ingin                 melanjutkan transaksi (Y/N)?”.
                Jika user memilih Y maka sistem akan meminta user akan memasukkan No. SKU barang yang dibeli oleh konsumen tersebut dan mengulang proses di atas.
                Jika user memilih N maka sistem akan kembali ke Sub Menu Kelola Transaksi Konsumen, dan tidak ada data yang diinputkan ke dalam Array.
      6.Setelah user memasukkan jumlah barang yang dibeli, sistem akan melakukan pemeriksaan sebagai berikut:
      Jika Jumlah Stok ≥ jumlah barang yang dibeli (dari inputan keyboard user) maka sistem akan melakukan 2 hal.
              1) Sistem akan mengupdate Jumlah Stok barang sesuai dengan No.SKU yang diinputkan user dengan rumus: 𝒕𝒐𝒕𝒂𝒍 𝒔𝒕𝒐𝒌 𝒃𝒂𝒓𝒂𝒏𝒈 = 𝒔𝒕𝒐𝒌 𝒍𝒂𝒎𝒂 − 𝒋𝒖𝒎𝒍𝒂𝒉 𝒃𝒂𝒓𝒂𝒏𝒈                   𝒚𝒂𝒏𝒈 𝒅𝒊𝒃𝒆𝒍𝒊
              dimana stok lama adalah stok yang tersimpan di dalam BST dan jumlah barang yang dibeli adalah hasil inputan keyboard user.
              2) Sistem akan mencatatkan transaksi konsumen ke dalam Array.
                Jika Jumlah Stok < jumlah barang yang dibeli (dari inputan keyboard user) maka sistem akan memunculkan pesan “Jumlah Stok No.SKU yang Anda beli                     tidak mencukupi” dan meminta user memilih “Apakah ingin melanjutkan transaksi (Y/N)?”.
                    Jika user memilih Y maka sistem akan meminta user akan memasukkan jumlah barang yang dibeli dan mengulang proses di atas.
                    Jika user memilih N maka sistem akan kembali ke Sub Menu Kelola Transaksi Konsumen, dan tidak ada data yang diinputkan ke dalam Array.
      7.Setelah sistem memasukkan data transaksi ke dalam Array, sistem akan memunculkan pesan “Data Transaksi Konsumen Berhasil Diinputkan” dan meminta user               memilih “Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)?”.
        Jika user memilih Y maka sistem akan meminta user memasukkan No. SKU barang yang dibeli oleh konsumen tersebut dan mengulang proses di atas.
        Jika user memilih N maka sistem akan kembali ke Sub Menu Kelola Transaksi Konsumen, dan tidak ada data yang diinputkan ke dalam Array.
        
Menu 2.2 Lihat Data Seluruh Transaksi Konsumen
      1.Menu ini akan menampilkan seluruh data transaksi konsumen yang tersimpan di Array.
      2.Data yang ditampilkan antara lain:
        Nama Konsumen; No. SKU barang yang dibeli; Jumlah Beli; Subtotal
      3.Setelah menampilkan data sistem akan kembali ke Sub Menu Kelola Transaksi Konsumen.
        Menu 2.3 Lihat Data Transaksi Berdasarkan Subtotal
          1.Menu ini akan menampilkan seluruh data transaksi konsumen yang tersimpan di Array secara urut.
          2.Pengurutan dilakukan berdasarkan nilai subtotal pada masing--masing data transaksi konsumen
          3.Data ditampilkan mulai dari subtotal yang paling besar hingga nilai subttotal yang paling kecil.
          4.Data yang ditampilkan antara lain:
          Nama Konsumen; No. SKU barang yang dibeli; Jumlah Beli; Subtotal
          5.Menu ini dapat diimplementasikan dengan Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort (pilih salah 1).
