import streamlit as st
import pandas as pd
import altair as alt
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

st.set_page_config(
    page_title = "Dashboard",
    layout = "wide"
)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('Inf1.png')    

# Mengubah font aplikasi Streamlit
st.markdown(
    """
    <style>
    body {
        font-family: 'Roboto', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan judul di tengah halaman
st.markdown(
    """
    <style>
    .title {
        display: flex;
        font-family: 'Roboto', sans-serif;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 45vh;
        text-align: center;
        font-size: 78px;
        font-weight: bold;
    }
    </style>
    
    <div class="title">
        <h1>Inflasi Indonesia Tahun 2022 Capai Rekor Tertinggi dalam Sewindu, Benarkah?</h1>
    </div>
    """,
    unsafe_allow_html=True
    )
st.markdown('**Oleh : _Zumrotul Wahidah_**')

tab1, tab2, tab3 = st.tabs([ "🗃 DATA","📈 GRAFIK","📊K-Means CLustering"])

with tab1:
    st.header("Data")
    df1 = pd.DataFrame({
    'Tahun': [2015,2016,2017,2018,2019,2020,2021,2022],
    'Inflasi Umum Tahunan': [3.35,3.02,3.61,3.13,2.72,1.68,1.87,5.51]
    })
    
    df2 = pd.read_excel('inflansibulan.xlsx')

    df3 = pd.read_excel('kelompok.xlsx')

    data = pd.read_excel('kmeans1.xlsx')

    tab1.caption('Sumber Data : :blue[_Badan Pusat Statistik_]')
    col1, col2, col3 = tab1.columns(3)
    with col1:
                st.write("")
                st.write("Data Inflasi Tahun 2015-2022")
                st.write(df1,use_container_width=True)
    with col2:
                st.write("")
                st.write("Data Inflasi Januari-Desember Tahun 2022")
                st.write(df2,use_container_width=True)
    with col3:
                st.write("Data Inflasi Bulanan Berdasarkan Kelompok Tahun 2022")
                st.write(df3,use_container_width=True)

    st.write("Data Inflasi 90 Kota di Indonesia Berdasarkan Kelompok Pengeluaran Tahun 2022")
    st.write(data,use_container_width=True)

with tab2:
    st.header("Grafik")
    col1, col2 = tab2.columns(2)

    with col1:
    #Line Chart Inflasi Year to Year
        st.header("Inflasi Indonesia 2015-2022")
        chart1 = alt.Chart(df1).mark_bar().encode(
        x = 'Tahun',
        y= 'Inflasi Umum Tahunan'
        )
        st.altair_chart(chart1)
    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('Inflasi adalah kenaikan harga barang dan jasa secara umum dan terus menerus dalam jangka waktu tertentu. Berdasarkan laporan Badan Pusat Statistik (BPS), sepanjang tahun 2022 Indonesia mengalami inflasi sebesar 5.51%. Angka ini menjadi rekor inflasi tertinggi dalam kurun waktu 8 tahun terakhir.')

    tab2.header("Pergerakan Inflasi Sepanjang Tahun 2022")
    chart11= alt.Chart(df2).mark_line().encode(
    x ='Tanggal',
    y='Inflasi'
    )
    tab2.altair_chart(chart11,use_container_width=True)
    tab2.markdown('Pergerakan tingkat inflasi gabungan 90 kota berdasarkan bulan pada tahun 2022 menunjukkan kenaikan inflasi sebesar 1.17% di bulan September setelah pada bulan sebelumnya mengalami deflasi sebesar 0.21%. Bulan September ini juga menjadi angka tertinggi inflasi bulanan sepanjang 2022.')

    tab2.header("Pergerakan Inflasi Sepanjang Tahun 2022 Berdasarkan Kelompok")
    chart = alt.Chart(df3).mark_line().encode(
        x='Tanggal',
        y='Inflasi',
        color='Kelompok'
    ).properties(
        height=600
    )

    # Streamlit
    tab2.altair_chart(chart,use_container_width=True)

    tab2.header("Inflasi Berdasarkan Kelompok September 2022")
    col1, col2, col3, col4,col5,col6,col7,col8,col9,col10,col11 = tab2.columns(11)
    with col1:
        st.write("Makanan, Minuman, dan Tembakau")
        st.image("makanan.png", caption="10.3")
    with col2:
        st.write("")
        st.write("")
        st.write("Pakaian dan Alas Kaki")
        st.image("pak.png", caption="0.2")
    with col3:
        st.write("Perumahan, Air, Listrik dan Bahan Bakar Rumah")
        st.image("listrik.png", caption="0.16")
    with col4:
        st.write("Perlengkapan, Peralatan dan Pemeliharaan Rutin Rumah Tangga")
        st.image("rt.png", caption="0.35")
    with col5:
        st.write("")
        st.write("")
        st.write("")
        st.write("Kesehatan")
        st.image("kes.png", caption="0.57")
    with col6:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("Transportasi")
        st.image("trans.png", caption="8.88")
    with col7:
        st.write("Informasi, Komunikasi dan Jasa Keuangan")
        st.image("kom.png", caption="-0.03")
    with col8:
        st.write("")
        st.write("")
        st.write("")
        st.write("Rekreasi, Olahraga dan Budaya")
        st.image("olg.png", caption="0.31")
    with col9:
        st.write("")
        st.write("")
        st.write("")
        st.write("Pendidikan")
        st.image("pend.png", caption="0.21")   
    with col10:
        st.write("Penyediaan Makanan dan Minuman/Restoran")
        st.image("wrg.png", caption="0.57") 
    with col11:
        st.write("Perawatan Pribadi dan Jasa Lainnya")
        st.image("pri.png", caption="0.28") 
    st.markdown("Pergerakan inflasi September 2022 menurut kelompok menunjukkan kelompok tertinggi penyumbang inflasi adalah kelompok Makanan, Minuman, Tembakau dengan angka inflasi sebesar 10.3%, disusul kelompok transportasi dengan angka inflasi sebesar 8.88%.")
    st.header("catatan peristiwa yang menjadi pemicu inflasi pada 2022")
    st.markdown("""
        <ul>
            <li>Januari 2022: Terjadi kelangkaan minyak goreng dan penetapan kebijakan satu harga minyak goreng.</li>
            <li>April 2022: Kenaikan harga avtur yang mendorong kenaikan tarif angkutan udara.</li>
            <li>Mei 2022: Permintaan naik memasuki bulan Ramadan dan Hari Raya Idul Fitri sehingga memicu kenaikan harga pangan.</li>
            <li>Juni 2022: Terjadi anomali cuaca di berbagai wilayah yang mengakibatkan gagal panen beberapa komoditas hortikultura sehingga memicu kenaikan harga.</li>
            <li><span style="color: red;">September 2022: Pemerintah menaikkan harga BBM jenis Pertalite 30,72%, Solar naik 32,04%, dan Pertamax naik 16%.</li>
            <li>Desember 2022: Musim libur sekolah, perayaaan Natal 2022, dan Tahun Baru 2023 mendorong kenaikan harga komoditas pangan dan transportasi.</li>
        </ul>
    """, unsafe_allow_html=True)
    st.caption('Sumber Data : :blue[_Databoks_]')

with tab3:

    
    import numpy as np
    from sklearn.cluster import KMeans
    # Data
    data1 = data.iloc[0:, 1:12]

    import seaborn as sns
    # Menghitung matriks korelasi
    correlation_matrix = data1.corr()

    # Menampilkan matriks korelasi
    st.subheader('Asumi Analisis Cluster')

    st.markdown("Uji Multikolinearitas")
    # Membuat heatmap korelasi
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    st.pyplot(fig)
    st.markdown("Uji multikolinearitas dilakukan untuk mengetahui apakah terdapat korelasi antar variabel independen atau variabel bebas. Uji multikolinearitas dalam penelitian ini dilakukan dengan cara melihat koefisien korelasi antar variabel independen.Berdasarkan hasil korelasi, tidak terdapat nilai korelasi antar variabel yang memiliki koefisien korelasi mendekati 1. Multikolinearitas terjadi jika nilai koefisien korelasi antar variabel bernilai > 0.80, dengan ini dapat disimpulkan jika tidak terjadi multikolinearitas pada data penelitian.")

    # Membuat objek KMeans dengan 2 cluster
    kmeans = KMeans(n_clusters=3)
    # Melakukan k-means clustering
    kmeans.fit(data1)
    # Mendapatkan label cluster untuk setiap data
    labels = kmeans.labels_
    # Mendapatkan pusat cluster
    st.subheader('Pusat Cluster')
    centers = kmeans.cluster_centers_
    st.write(centers)
    # Mendapatkan label cluster untuk setiap data
    cluster_labels = kmeans.labels_

    # Menambahkan kolom cluster ke data
   
    data['Cluster'] = cluster_labels
    data['Longitude'] = data['Longitude']
    data['Latitude'] = data['Latitude']


    # Menampilkan hasil clustering
    st.subheader('Hasil Analisis K-Means Clustering')
    st.write(data)

    # Menampilkan jumlah data dalam setiap cluster
    st.subheader('Jumlah Data dalam Setiap Cluster')
    st.write(data['Cluster'].value_counts())

    import folium
    from streamlit_folium import st_folium, folium_static

    # Judul halaman
    st.title("Persebaran Inflasi Tertinggi Tahun 2020 Kelompok Makanan, Minuman, dan Tembakau")
    # Menampilkan peta dengan koordinat tengah di Indonesia
    m = folium.Map(location=[-2.5489, 118.0149], zoom_start=5)
    folium.Marker(location=[-2.74167,107.65300], popup="Tanjung Pandan").add_to(m)
    folium.Marker(location=[-2.12932,106.10960], popup="Kota Pangkal Pinang").add_to(m)
    folium.Marker(location=[-4.5467590,136.8837210], popup="Timika").add_to(m)
    folium.Marker(location=[-2.5330000,140.7170000], popup="Kota Jayapura").add_to(m)
    # Menampilkan peta ke dalam Streamlit
    folium_static(m,width=1200, height=600)

  


