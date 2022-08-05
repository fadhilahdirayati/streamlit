import streamlit as st

with st.container():
    cyber,  grapic_text, grapic = st.columns([1,3,1])

    cyber.image("img/Cyber_Logo.png", width=64)
    grapic.image("img/graphi_design.png", width=70)

    grapic_text.markdown("""
    <div class="header-logo" style="display: flex; justify-content:space-around; align-items:center;">
            <img src="./img/Cyber_Logo.png" alt="">
            <h3><span style="color: red;">PC</span>-<span>THERE</span></h3>
            <img src="./img/graphi_design.png" alt="">
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
        <h1 class="title" style='text-align: center;'>Bahaya Serangan Ransomware</h1>
    """, unsafe_allow_html=True)
    st.image("img/Ransomware_1.jpg")

    st.markdown("""
    ## Apa itu Ransomware ?
    Ransomware merupakan sebuah nama dari kelas malware yang terdiri dari dua kata, ransom (tebusan) dan malware, yang bertujuan untuk menuntut pembayaran untuk data / informasi pribadi yang telah dicuri, atau data yang aksesnya dibatasi (enkripsi). Saat ini, malicious software telah melakukan diversifikasi (usaha memperoleh keuntungan) dengan cara mereka memeras uang dari korban. Orang dapat berargumen bahwa ransomware adalah bentuk pemerasan sederhana yang digunakan untuk pemerasan secara massal, disebarkan ke banyak pengguna dan dibuat lebih efisien dengan memanfaatkan Cryptocurrency untuk anonymity sebuah transaksi.
    \n\n
    Munculnya ransomware telah menjadi sebuah epidemi secara global karena hal tersebut terus memakan banyak korban di seluruh dunia, memaksa perusahaan untuk memutuskan antara mencoba memulihkan data dari cadangan (dan berpotensi kehilangan data penting sejak cadangan terakhir) dan membayar sejumlah besar tebusan kepada peretas. Ransomware telah menjadi berita utama baru-baru ini dengan mengumpulkan korban yang terkenal, termasuk rumah sakit Los Angeles, dan dua rumah sakit Jerman. Dari CryptoLocker, Locky, dan Kovter, hingga serangan baru-baru ini yang memanfaatkan CryptXXX, dan Petya. Pada tahun 2017, Rumah Sakit Kanker Dharmais dan Rumah Sakit Harapan Kita, Jakarta terkena ransomware Wannacry yang mengakibatkan beberapa database pasien pada komputer tidak dapat diakses. Malware bermodus menyandera data dan meminta tebusan uang itu telah mengunci sistem dan data pasien dengan meminta uang Rp 4 juta sebagai tebusan.
    \n\n
    
    ### Tahapan Serangan Ransomware
    serangan ransomware diawali dengan “malware arrival” ditandai adanya aktivitas dari pengguna baik melakukan klik sebuah malicious links atau malicious software. Setiap malware yang telah diklik, akan secara otomatis melakukan koneksi ke C2C (Command and Control) yang merupakan pusat kegiatan malicious software untuk melakukan pengiriman perintah (Command) dan melakukan kontrol pada victim (Control). Pada tahap koneksi ke C2C, malware akan melakukan unduh file pendukung lainnya untuk dapat melakukan serangan lebih dalam lagi. Selanjutnya, malware akan mencari file penting untuk dapat melakukan pencurian atau target penguncian file. Setiap file yang menjadi target, akan dilakukan enkripsi dan akan memunculkan sebuah file note yang berisi alamat email penyerang beserta nomor rekening pembayaran untuk dapat melakukan dekripsi file yang terkunci. Dengan demikian, penyerang akan memberikan mekanisme dekripsi file jika pembayaran sudah dilakukan. Namun, hal tersebut tidak dapat dipastikan karena beberapa pengguna yang terkena ransomware dan melakukan pembayaran, penyerang tidak memberikan informasi ini
    
    ### Bagaimana Ransomware Menerobos Komputer Anda?
    Biasanya, peretas menyasar korban yang, menurutnya, bersedia membayar tebusan dan mendapatkan kembali data mereka dengan cepat. Dalam beberapa tahun terakhir, perusahaan besar termasuk rumah sakit besar dan bahkan Sony Pictures sudah menjadi sasaran.Tetapi hampir semua orang bisa menjadi korban serangan ransomware, dan biasanya terjadi dengan salah satu dari dua cara:
    \n\n
    - Pertama, Anda mengunduh ransomware yang tersamarkan sebagai lampiran email.
    Pernahkah Anda menerima email dari seseorang yang tidak Anda kenal, yang disertai lampiran samar yang dinamai misalnya “Invoice”? Kerap kali, pesan-pesan aneh tersebut adalah ransomware atau serangan malware lainnya yang menyamar (dikenal sebagai Trojan). Email tersebut bahkan mungkin berasal dari seseorang yang Anda kenal, tetapi lampiran yang tampak tidak berbahaya itu mungkin virus yang menunggu untuk menginfeksi komputer Anda segera setelah Anda unduh.
    - Kedua, peretas mengeksploitasi celah dalam pertahanan komputer.
   Exploitasi memanfaatkan kerentanan atau kesalahan dalam kode program komputer atau sistem operasi.
   Peretas bisa menemukan, misalnya, kerentanan di versi Windows terbaru yang memungkinkan dia menyelinap lewat pintu belakang PC Anda dan menginstal malware di mesin Anda.
   Eksploitasi yang diketahui adalah masalah terkait perangkat lunak yang telah ditemukan dan, biasanya, ditambal dengan pembaruan keamanan. Eksploitasi yang tidak diketahui belum dipublikasikan dan menjadi “serangan zero-day,” atau serangan malware pertama dari jenisnya.
    
    ### Jenis - Jenis Ransomware
    """)

    # ! EXPANDER ##############################################################################################################

with st.container():
    with st.expander("Encrypting Ransomware"):
        st.markdown("""Jenis ransomware ini, setelah dijalankan, secara diam-diam akan melakukan pencarian dan mengenkripsi file penting di sistem komputer korban. Setelah langkah pertama selesai, sebuah pesan ditampilkan kepada pengguna yang meminta tebusan dan untuk mengembalikan file yang terkunci (enkripsi). Instruksi rinci disajikan kepada pengguna, bahkan informasi kontak baik telepon maupun email disediakan. Setelah tebusan dibayarkan, korban akan diberikan kunci atau kode untuk dekripsi file, yang dapat dijalankan khusus untuk mendekripsi file di sistem komputer korban. Contoh dari encrypting ransomware adalah CryptoWall, CryptoLocker, WannaCry dan Locky.
        """)

    with st.expander("Non-Encrypting Ransomware"):
        st.write("Beda halnya dengan Ransomware jenis Encrypting, Ransomware jenis non-encrypting melakukan penguncian akses pengguna ke sebuah sistem komputer tanpa melakukan enkripsi pada sistem file dan menampilkan pesan penyerang untuk menuntut sebuah tebusan (ransom) atau meminta tindakan pengguna yang membutuhkan uang untuk membuka kunci. Untuk membuat pengguna membayar uang tebusan, beberapa threat actor meminta korbannya. untuk diberikan pembayaran di awal dengan meminta pengguna untuk menghubungi nomor telepon tertentu. Contoh ransomware ini adalah Winlocker dan Reveton.")

    with st.expander("Locker Ransomware"):
        st.write("Locker ransomware tidak membeda-bedakan apa yang dikuncinya. Setelah memasuki komputer, semuanya terkunci! Jika Anda tidak bisa masuk ke komputer atau menggunakannya untuk tugas-tugas dasar tanpa melihat pesan tebusan yang mengancam, Anda mungkin telah terinfeksi oleh locker ransomware.")

    with st.expander("Scareware"):
         st.write("Seperti locker ransomware, scareware kerap kali akan membatasi semua akses ke komputer dan data Anda. Perbedaannya adalah bahwa scareware mencoba beragam taktik untuk memaksa Anda membayar tebusan. Anda mungkin melihat jendela pop up yang diduga sedang “memindai” komputer untuk mendeteksi masalah. Dia tentu saja akan menemukan beberapa masalah dan menawari Anda untuk “memperbaikinya” — dengan harga yang lumayan besar. Anda tidak akan bisa menyingkirkan pesan tersebut atau terus menggunakan komputer sebelum membayar uang tebusan.")
    
    with st.expander("Doxware"):
        st.write("Sebagai satu bentuk ransomware yang menyebalkan, doxware bukan hanya konten yang menghapus atau membatasi akses ke data Anda. Dia mengancam untuk mempublikasikan informasi sensitif, seperti merusak foto atau video, informasi identifikasi pribadi, atau data keuangan, secara publik di Internet jika tebusan tidak dibayarkan. Doxware dapat sangat menghancurkan bagi bisnis maupun individu.")
        
        st.markdown("\n\n\n\n")


st.sidebar.markdown("Home❄️")


