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
    ## Taktik dan Pencegahan Umum 
    \n\n
    Dikarenakan ransomware menginfeksi melalui 3 jalur utama yaitu melalui website, link dan attachment pada email, dan melalui Flash disk, berikut ini langkah-langkah yang direkomendasikan untuk melindungi data-data anda:
    \n\n
    
    ### Langkah-langkah pencegahan serangan Ransomware
    Langkah yang pertama yaitu Anda harus waspada terhadap 3 jalur utama penyebaran ransomware diatas dan menerapkan langkah-langkah pencegahan dasar untuk melindungi semua perangkat komputer di perusahaan Anda. Jangan membuka link atau attachment email secara sembarangan dan jika ada notifikasi tentang masalah keamanan, sebaiknya dikonfirmasikan kepada si pengirim terlebih dahulu atau periksa ekstensi dari file yang dikirimkan lewat email tersebut. Harus lebih waspada lagi pada ekstensi file yang terkompresi (.zip, .rar, dll). Begitu juga penggunaan USB flash disk, sebaiknya tidak digunakan sembarangan, apalagi ketika digunakan di kantor.Bagaimanapun juga, meskipun setiap pegawai sudah berhati-hati dalam hal ini, tetap saja mustahil untuk melindungi semua sistem dan komputer dari serangan cyber tadi. Oleh karena itu, sangat penting untuk selalu memperbarui sistem operasi di komputer ke versi yang paling terbaru untuk mengurangi kerentanan sistemnya. Selain itu, sangat disarankan juga menginstal anti virus dan terus memperbarui versinya.
    \n\n

    ### Langkah-langkah mengurangi resiko kerusakan jika terinfeksi
   Meskipun sudah dilakukan pencegahan seperti yang disebutkan di atas, serangan ransomware masih bisa terjadi, dan Anda harus sudah mengetahuinya akan kemungkinan tersebut. Dengan backup system yang bagus, Anda bisa mengembalikan data Anda meskipun sistem anda mengalami serangan. 
    \n\n

    """)
   


# ! SMALL IMAGE AND DESCRIPTION AREA ###########################################################################################

with st.container():
    type1, type2 = st.columns(2)
    text_type1, text_type2 = st.columns(2)

    with type1:
        st.write("### Keamanan")
        st.image("img/keamanan.jpg", width=200, caption='First Hacker')

    with type2:
        st.write("### Aturan backup 3-2-1")
        st.image("img/backup.jpg", width=200, caption='Second Hacker')

    with text_type1:
        st.markdown("Pencadangan adalah proses menduplikasi data dari komputer dan menyimpannya secara terpisah untuk mencegah data tersebut hilang sewaktu-waktu atau terjadi situasi yang tidak diharapkan.")
   
    with text_type2:
        st.markdown("Di dunia pencadangan, dikatakan bahwa untuk melindungi data Anda dengan sempurna, Anda harus mengikuti Aturan 3-2-1 .Aturan 3-2-1 meliputi 3 aturan yang pertama buat 3 pencadangan. Kedua simpan data pencadangan di dua media penyimpanan yang berbeda. dan terakhir Cadangkan satu salinan ke lokasi yang terpencil. ")

    st.markdown("""
    ### Adapun pembahanan lebih terperinci mengenai aturan Backup 3-2-1:
    \n\n
    1.Membuat backup
       Dengan hanya 1 atau 2 pencadangan, selalu ada kemungkinan bahwa satu atau keduanya akan rusak atau hilang, seperti yang terjadi pada data aslinya. Oleh karena itu, cadangan yang ketiga akan menciptakan lapisan keamanan yang ekstra.
    \n\n
    2.Menyimpan di dua media penyimpanan yang berbeda
       Jika semua cadangan data disimpan di satu media penyimpanan yang sama, Anda bisa kehilangan semua data tersebut jika masalahnya berhubungan dengan masalah media. Menyimpan cadangan data di beberapa jenis media yang berbeda, seperti DVD, hard disk, tape, dan online akan mengurangi kemungkinan satu masalah dapat menghapus semua cadangan data Anda.
    \n\n
    3.Mencadangkan satu salinan di tempat yang terpencil.
    Bagaimana jika rumah atau kantor Anda mengalami kebakaran? Di Indonesia, sering sekali terjadi gempa bumi. Jadi sangat dimungkinkan Anda akan mengalami bencana semacam itu. Jika semua cadangan data anda berada di satu lokasi, mereka bisa mengalami kerusakan atau gangguan dengan mudah. Dengan menyimpan setidaknya satu cadangan di lokasi terpencil, Anda dapat lebih siap menghadapi berbagai jenis bencana alam dan buatan manusia. 
    \n\n
    
    ### Penanganan Insiden Siber Ransomware
    \n\n\n
    Dalam melakukan penanganan insiden siber ransomware, perlu dilakukan penelusuran terkait penyebab malicious software (malware) yang mengakibatkan terkuncinya data pengguna. Kegiatan penelusuran insiden siber dapat dilakukan sesuai dengan tahapan sebagai berikut :

    """)

# ! EXPANDER ##############################################################################################################
with st.container():
    with st.expander("Fase Persiapan"):
        st.markdown("""
        Tahap ini adalah tahap dimana kebijakan, prosedur,teknologi, dan sumber daya manusia harus disiapkan secara matang, dimana akan digunakan pada proses penanganan terhadap insiden. Dalam suatu organisasi/institusi, kemampuan melakukan respon yang cepat terhadap suatu insiden, merupakan persiapan yang mendasar bagi penanganan insiden siber ransomware.
        \n\n
        Langkah yang dapat diambil, sebagai berikut :
        1. Mempersiapkan tim tanggap insiden siber yang dapat berasal dari internal atau eksternal organisasi;
        2. Mempersiapkan dokumen pendukung untuk melakukan penanganan insiden, misalkan dokumen prosedur penanganan insiden, dokumen kebijakan penggunaan laptop/pc, antivirus, backup;
        3. Melakukan koordinasi dengan pihak terkait, misalkan tim aplikasi, tim infrastruktur, tim pakar, atau tim tanggap insiden lainnya (CSIRT) yang mendukung dalam penanganan insiden siber;
        4. Menyiapkan tools yang dapat berupa License Tools, Open Source Tools, sumber terbuka lainnya. Tools yang dapat digunakan untuk melakukan analisis misalkan Process Explorer (https://download.sysinternals.com/files/ProcessExplorer.zip) dan Autoruns (https://download.sysinternals.com/files/Autoruns.zip). Beberapa website yang menyediakan informasi mengenai serangan ransomware beserta teknik mitigasi atau menyediakan decryption tools : https://nomoreransom.org, https://blog.emsisoft.com.


        """)


    with st.expander("Fase Identifikasi dan Analisis"):
        st.markdown("""
        Melakukan identifikasi dan analisis terhadap sistemt erdampak guna mendapatkan akar permasalahan dari insiden yang terjadi. Langkah yang dapat dilakukan :
        \n\n
        Langkah yang dapat diambil, sebagai berikut :
        1.Melakukan identifikasi jenis ransomware untuk melakukan analisis lebih lanjut. Adapun langkah-langkah yang dilakukan sebagai berikut : Temukan pesan yang disampaikan oleh aplikasi Ransomware (README File). Dalam file pesan tersebut berisi mengenai alamat email penyerang, string pesan dari malware tersebut; Temukan jenis ekstensi dari file yang terkena insiden siber ransomware (misalkan *.crypt, *.cry, *.locked, dst); Gunakan file Readme, Email Penyerang, dan Sampel File yang terkena insiden untuk mendapatkan jenis Ransomware melalui sumber terbuka misalkan https://nomoreransom.org atau https://blog.emsisoft.com
        2.Memeriksa apakah antivirus berfungsi normal atau tidak. Hal ini karena ada malware yang dapat menghancurkan instalasi antivirus dengan merusak executable file, mengubah kunci registri atau merusak file definisi, maupun menonaktifkan update dari signature suatu file.
        3.Melakukan identifikasi dan analisis pada environment sistem terdampak guna mencari persistent mechanism penyerang atau artefak digital hasil penyerangan yang dilakukan. Proses yang dilakukan adalah sebagai berikut :
            - Identifikasi dan analisis proses berjalan, misalkan menggunakan tools Process Explorer untuk melakukan identifikasi Malicious Process yang sedang berjalan di sistem komputer. Aplikasi Process Explorer dapat secara langsung diaktifkan terkoneksi pada VirusTotal.com untuk dilakukan Process Scanning dengan antivirus yang terdaftar;
            -Identifikasi dan analisis jaringan komunikasi menggunakan tools Netstat untuk melakukan identifikasi Malicious Connection baik dengan status Listening, Established, SYN_SENT.
        4.Melakukan identifikasi dan analisis pada sistem jaringan komunikasi untuk mengetahui Lateral Movement dari penyerang dengan melakukan implementasi daftar indikasi kebocoran (indicator of compromise) pada perimeter keamanan seperti Firewall, Network IDS, Host IDS.
        
        
        """)
        
    with st.expander("Fase Penahanan"):
        st.markdown("""
        Tahap ini bertujuan untuk mencegah penyebaran Ransomware. Prosedur yang dilakukan pada tahap penahanan adalah sebagai berikut :        \n\n
        Langkah yang dapat diambil, sebagai berikut :
        1. Melakukan isolasi sistem terdampak agar insiden siber ransomware tidak menyebar melalui jaringan misalkan dengan menutup akses ke jaringan.
        2. Mengubah konfigurasi routing table pada Firewall untuk memisahkan sistem yang terinfeksi dengan sistem lainnya.
        3. Melakukan backup data pada sistem yang terdampak. 
        4. Identifikasi gejala kemiripan pada sistem lain untuk mencegah penyebaran serangan. Jika terdapat kemiripan, maka sistem tersebut juga harus dilakukan proses penahanan.
           
        """)

    with st.expander("Fase Penghapusan"):
        st.markdown("""
        1. Menghentikan proses yang terindikasi merupakan Malicious Process;
        2. Menghapus autostart process yang mencurigakan dari hasil analisa aplikasi autostart;
        3. Jika terdapat user–user yang dibuat oleh malware, maka hapus user–user yang tidak dikenali tersebut untuk menghindari masuknya kembali malware melalui user yang tidak dikenal tersebut;
        4. Setelah program malware dihapus dan malicious process di kill process, lakukan full scanning terhadap sistem menggunakan signature antivirus yang sudah diperbaharui.
        
        """)

    with st.expander("Fase Pemulihan"):
        st.markdown("""
        Tahap pemulihan merupakan tahap mengembalikan sistem terdampak pada kondisi normal seperti semula. Proses yang dilakukan adalah sebagai berikut :
        1. Melakukan dekripsi file yang terkena dampak dengan menggunakan decryption tools yang tersedia;
        2. Melakukan validasi sistem untuk memastikan sudah tidak ada aplikasi atau file yang rusak atau terinfeksi. Begitu pula kesalahan atau kekurangan konfigurasi sistem untuk kemudian disesuaikan kembali;
        3. Melakukan aktivitas monitoring untuk memantau lalu lintas jaringan yang terhubung;
        4. Jika terjadi kerusakan yang cukup parah (file sistem terhapus, data penting hilang, menyebabkan kegagalan booting pada sistem operasi), maka sistem dibangun ulang dari file backup terakhir sistem yang dimiliki;
        5. Melakukan update/patching Sistem Komputer dan Antivirus.
        """)


    with st.expander("Fase Tindak Lanjut "):
        st.markdown("""
        Tahap ini adalah fase di mana semua dokumentasi kegiatan yang dilakukan dicatat sebagai referensi untuk masa mendatang. Prosedur yang dapat dilakukan adalah sebagai berikut:
        1. Membuat dokumentasi dan laporan terkait penanganan insiden siber ransomware, yang berisi langkah-langkah dan hasil yang telah didapatkan. 
        2. Memberikan analisa dan penjelasan apa yang harus dilakukan, sehingga meminimalisir insiden serupa tidak terulang kembali. 
        3. Menuliskan bukti-bukti yang ditemukan, hal ini terkait dengan proses hukum kedepannya. 
        4. Membuat evaluasi dan rekomendasi. Rekomendasi yang dapat diberikan diantaranya: 
        5. Peningkatan pengetahuan tentang penanganan insiden Ransomware, misalnya melalui pelatihan, cyber exercise.
        6. Implementasikan sistem monitoring untuk pendeteksian dini serangan ataupun insiden siber.
        7. Meningkatkan pertahanan sistem
        8. Melakukan penyempurnaan prosedur penanganan insiden siber berdasarkan insiden siber yang terjadi.
        """)
        

st.markdown("\n\n\n\n")

st.sidebar.markdown("Type & Solution ❄️")