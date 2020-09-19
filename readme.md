Langkah dalam pembuatan modul Pendaftaran Sidang:
1. Membuat DB lokal dengan nama "akademik",
2. Setting koneksi DB pada .flaskenv,
3. Instalasi Library Python => python -m venv virtualenvi,
4. Jalankan Script Python ke mode virtual =>  virtualenvi\Scripts\activate,
5. Upgrade dan instal PIP Python => python -m pip install --upgrade pip,
6. Membuat file req.txt dan lakukan instalasi tools dengan Run Script => pip install -r req.txt, 
7. Proses Flask DB Init, Migrate, & Upgrade struktur tabel & membuat relasi antar tabel yang dibutuhkan pada Model. Berupa: users, prodis, sidangs, & berkas_sidang,
8. Membuat File & Script Controllers untuk proses CRUD data ke masing-masing tabel DB. Berupa: userController, prodiController, sidangController, & berkasSidangController,
9. Membuat File & Script Route untuk proses POST, GET, PUT, & DELETE. Berupa: routeUser, routeProdi, routeSidang, & routeFile,
10. Daftarkan file Model & Route pada file "__init__.py"
11. Melakukan test aplikasi (Flask Run) Daftar Sidang untuk proses CRUD, mulai dari modul User, Prodi, Sidang, & fileSidang,
12. Mencoba melakukan CRUD dengan Post, Get, Put, & Delete data melalui Postman, kemudian cek hasil proses ke masing-masing tabel penyimanan data,
13. Install & konfigurasi JWT Token User Login & Refresh Token pada userController & sidangController,
14. Install & konfigurasi Flask-Mail, untuk melakukan proses kirim Email secara otomatis apabila melakukan POST tambah data User dan Daftar Sidang pada flaskenv, config.py, & controller,
15. Konfigurasi & Test Run Background Proses pada "__init__.py",
16. Setting Queue Worker Redis pada "__init__.py" dan coba jalankan dengan perintah "rq worker" dan "flask run" dari 2 terminal yang berdeda.

- SELESAI -




