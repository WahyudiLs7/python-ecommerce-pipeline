# Python E-Commerce Pipeline

Aplikasi sederhana menggunakan Python untuk mengelola data pesanan pelanggan, menghitung total pendapatan, dan mengalkulasi pajak secara otomatis. Project ini dibuat untuk mendemonstrasikan pemahaman dasar Object-Oriented Programming (OOP) di Python.

## Konsep yang Digunakan

Pada program ini, saya menggunakan konsep **Encapsulation** (membungkus data di dalam class). 
- Data spesifik pesanan (seperti ID, Nama, Tanggal, dan Total Harga) dibungkus di dalam `class Order`.
- Logika untuk mengelola banyak pesanan sekaligus (menyimpan ke dalam *list*, menghitung total keseluruhan pendapatan, dan total keseluruhan pajak) dibungkus di dalam `class OrderProcessor`.

## Cara Pengujian

Saya memasukkan 3 data pesanan sebagai sampel pengujian dengan rincian sebagai berikut:
1. Pesanan Budi (Rp 100.000)
2. Pesanan Siti (Rp 150.000)
3. Pesanan Andi (Rp 50.000)

Dengan total harga keseluruhan **Rp 300.000**, program berhasil berjalan dan menghitung pajak sebesar 10% secara otomatis, menghasilkan output total pajak sebesar **Rp 30.000**.
