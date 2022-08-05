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
        <h1 class="title" style='text-align: center;'> Edisi Berita Ransomware</h1>
        <div class="des-title" style='text-align: center;'>Kumpulan beberapa berita mengenai Ransomeware</div>
        <br><br>
    """, unsafe_allow_html=True)


news1, news2, news3 = st.tabs(["Data BI yang Bocor Bertambah", "Serangan Siber Ransomware pada RS Dharmais", "BPS Aman dari Serangan Malware Wannacry"])

with news1:
    
    st.video("https://www.youtube.com/watch?v=kCzjFVGKM5Y")

    st.markdown("""
    ### Korban Serangan Ransomware, Data BI yang Bocor Bertambah
    25 Jan 2022  KOMPAS.TV
    \n\n
    Setelah Bank Indonesia memastikan tidak ada data kritikal diretas geng ransomware conti, hari ini (24/01) diketahui data bocor BI bertambah. Dari tweet dark tracer siang tadi menyebut, geng ransomware conti terus menguanggah data internal Bank Indonesia. Jika di kebocoran data pertama adalah 487 mb kini mencapai 74 gb. Sementara, PC internal yang pada awalnya adalah 16 datanya berkembang menjadi 237 PC.
    \n\n
    Seperti diketahui, data Bank Indonesia diserang ransomware pada Desember lalu. Conti sendiri diketahui ransomware beraksi internasional menebar masalah di banyak negara.Mengutip Cybersecurity and Infrastructure Security Agency (CISA) dan FBI Amerika Serikat, conti bahkan sudah melakukan 400 serangan di Amerika Serikat dan organisasi internasional. Lagi penjahat cyber menembus sistem kemanan siber lembaga negara, kali ini Bank Indonesia jadi korban serangan ransomware. Baca Juga Bank Indonesia Jelaskan Soal Peretasan Data, Meski BI memastikan tidak ada sejumlah data kritikal berhasil diambil geng conti ransomware.
    \n\n
    Pembobolan data oleh hacker ke sejumlah kementerian, lembaga juga pernah diduga bocor atau diretas hacker. Sebut saja data BPJS data eHAC sampai situs pusat malware nasional dari BSSN terkena peretasan dengan metode perusakan atau deface. Yang jelas kasus serangan siber di Indonesia setiap tahun menunjukkan tren kenaikan. Tahun 2019 lebih dari 288 juta, 2020 lebih dari 495 juta, dan 2021 lebih dari 888 juta itu di periode Januari sampai Agustus saja. Data ini campuran, secara total termasuk juga swasta dari berbagai sektor e-commerce, kesehatan dan lain-lain.

    """)
with news2:
    
    st.video("https://www.youtube.com/watch?v=eOWUaUN00uM")

    st.markdown("""
    ### Waspada Joker! Virus Baru di Android
     16 Mei 2017  CNN Indonesia
    \n\n
    Presiden Direktur Rumah Sakit Dharmais, Abdul Kadir, menjelaskan kronologi terjadinya serangan virus cyber ransomware WannaCry pada sistem IT rumah sakit yang terletak di kawasan Jakarta Barat itu. "Jadi serangannya itu terjadi pada hari Sabtu, tanggal 13 Mei 2017 jam 05.00 subuh," ujar Abdul saat memberi keterangan pers di lobi RS Dharmais, Jakarta Barat, Senin (15/5/2017). Dia menjelaskan, pada saat itu seorang petugas RS Dharmais hendak memasukkan data seorang pasien rawat inap. Namun tampilan pada monitor komputer berbeda dari tampilan biasanya. "Tiba-tiba muncul tampilan di monitor itu berubah semua," ucap Abdul.
    \n\n
   Melihat keanehan pada tampilan monitor, petugas rumah sakit tersebut kemudian melapor kepada petugas instalasi IT pasien rawat inap RS Dharmais. "Mendengar laporan itu, diinstruksikan untuk menghentikan semua proses IT dan mematikan semua komputer yang ada di RS ini," ujar Abdul. Abdul menjelaskan, dari data yang telah dihimpun, terdapat sekitar 60 unit komputer di RS Dharmais yang terserang ransomware WannaCry. Serangan virus itu dia sebut tidak melumpuhkan layanan rumah sakit terhadap pasien dan pengunjung. "Kami ini punya sekitar 600 unit komputer dan hanya sekitar 60 unit saja yang terserang virus. Saat ini 60 unit komputer tersebut sudah kami amankan untuk disterilkan," ujar Abdul.

    """)

with news3:
    
    st.video("https://www.youtube.com/watch?v=KfvE5VFfQBw")
    st.markdown("""
    ### BPS Aman dari Serangan Malware Wannacry
    16 Mei 2017  CNN Indonesia
    \n\n
    Badan Pusat Statistik (BPS) memastikan bahwa seluruh data yang dihimpun dan dimiliki, aman dari gangguan virus Ransomware WannaCry yang mengincar sistem komputer di berbagai belahan dunia. Kepala BPS Suhariyanto atau yang akrab disapa Ketjuk mengatakan, Biro Sistem Informasi Statistik (SIS) BPS telah melakukan pemindahan dan penyegaran atas seluruh data yang dimiliki sesuai dengan arahan dari Menteri Komunikasi dan Informatika (Menkominfo) Rudiantara. "Pak Rudiantara sudah bilang tidak perlu panik. Kami ikuti langkah yang sudah ditentukan dan kami sudah memindahkan (back up) data sesuai arahan dari Menkominfo. Alhamdulillah setelah dibuka, datanya tidak ada masalah. Semoga aman-aman saja," kata Ketjuk di Kantor BPS, Senin (15/5).
    \n\n
    Bahkan, sambung Ketjuk, proteksi dan antisipasi yang dilakukan oleh BPS sesuai dengan arahan Menkominfo telah dilakukan sejak kabar virus WannaCry menyebar pada akhir pekan lalu.
    "Sebetulnya kami sudah siap dari kemarin pagi. Biro SIS sudah melakukan berbagai proteksi," imbuh Ketjuk.
    Di Indonesia, berdasarkan laporan yang diterima oleh Kementerian Komunikasi dan Informatika, virus ini menyerang sistem komputer Rumah Sakit Harapan Kita dan Rumah Sakit Dharmais.
    Sampai saat ini belum terdata secara pasti berapa banyak perusahaan di Indonesia yang terkena serangan dari Ransomware WannaCry. Kerugian yang didapat dari virus ini pun berbeda, tergantung data atau dokumen yang dicuri oleh virus tersebut.
    Di Indonesia, ransomware WannaCry mulai terdeteksi pada Jumat sore (12/5). Itu merupakan keuntungan tersendiri karena sebagian besar perusahaan sudah mematikan komputernya.
 
    \n\n
    "Serangan ini masif di seluruh dunia, jadi bukan hanya di Indonesia saja. Engineer dan negara di seluruh dunia sedang mencari jalan. Penanganan global sedang dilakukan," kata Rudiantara akhir pekan kemarin.
    Terkait serangan tersebut, Rudiantara mengatakan keamanan siber menjadi program prioritas kementeriannya. Saat ini, pemerintah sedang mendorong terus percepatan pembentukan Badan Siber Nasional untuk menangani dan mencegah kasus-kasus siber seperti ke depannya.
    "Saat ini, Peraturan Presiden atau Keputusan Presiden soal pembentukan Basinas sedang diproses," pungkasnya.
     """)


    

st.sidebar.markdown("News❄️")