#Bar Chart Inflasi 90 Kota
    tab3.header("Inflasi 90 Kota di Indonesia Tahun 2022")
    sorted_data = data.sort_values('Tahunan')
    chart2 = alt.Chart(data).mark_bar().encode(
    x='Kota',
    y= alt.Y('Tahunan', sort=sorted_data['Tahunan'].tolist()),
    )
    tab3.altair_chart(chart2, use_container_width=True)

    chart = alt.Chart(df3).mark_line().encode(
        x='Tanggal',
        y='Inflasi',
        color='Kelompok'
    ).properties(
        height=600
    )
tab3.header("Inflasi 90 Kota di Indonesia Tahun 2022")
    sorted_data = data.sort_values('Tahunan')
    chart2 = alt.Chart(data).mark_bar().encode(
    x='Kota',
    y= alt.Y('Tahunan', sort=sorted_data['Tahunan'].tolist()),
    )
    tab3.altair_chart(chart2, use_container_width=True)

 nama = data.iloc[0:]
    data = {
        'Nama': nama['Kota'],
        'Inflasi': nama['Tahunan'],
        'Cluster': nama['kluster']
    }
    dataakhir = pd.DataFrame(data)
    tab3.write(dataakhir)

 # Menampilkan scatter plot
    scatter_plot = alt.Chart(dataakhir).mark_circle(size=60).encode(
        x= 'Inflasi',
        y='Cluster',
        color=alt.Color('Cluster:N', scale=alt.Scale(scheme='category10'))
    ).interactive()

    tab3.write("Scatter Plot:")
    tab3.altair_chart(scatter_plot, use_container_width=True)

 nama = data.iloc[0:]
    data = {
        'Nama': nama['Kota'],
        'Makanan, Minuman, dan Tembakau': nama['Makanan, Minuman, dan Tembakau'],
        'Pakaian dan Alas Kaki': nama['Pakaian dan Alas Kaki '],
        'Perumahan, Air, Listrik dan Bahan Bakar Rumah': nama['Perumahan, Air, Listrik dan Bahan Bakar Rumah'],
        'Perlengkapan, Peralatan dan Pemeliharaan Rutin Rumah Tangga': nama['Perlengkapan, Peralatan dan Pemeliharaan Rutin Rumah Tangga'],
        'Nama': nama['Kota'],
        'Nama': nama['Kota'],
        'Cluster': nama['kluster']
    }
    dataakhir = pd.DataFrame(data)
    tab3.write(dataakhir)

dfklus = pd.read_excel('maps.xlsx')
    
    def main():
        # Judul halaman
        tab3.title("Persebaran Inflasi Tertinggi Tahun 2020")

        # Menampilkan peta dengan koordinat tengah di Indonesia
        m = folium.Map(location=[-2.5489, 118.0149], zoom_start=5)
        folium.Marker(location=[-0.95,100.3530556], popup="Kota Padang").add_to(m)
        folium.Marker(location=[-0.3055556,100.3691667], popup="Kota Bukittinggi").add_to(m)
        folium.Marker(location=[0.5333333,101.45], popup="Kota Pekanbaru").add_to(m)
        folium.Marker(location=[-6.9147444,107.6098111], popup="Kota Bandung").add_to(m)
        folium.Marker(location=[-7.733333,109], popup="Cilacap").add_to(m)
        folium.Marker(location=[-7.5666667,110.8166667], popup="Kota Surakarta").add_to(m)
        folium.Marker(location=[-8.172357,113.700302], popup="Jember").add_to(m)
        folium.Marker(location=[-6.12009,106.150299], popup="Kota Serang").add_to(m)
        folium.Marker(location=[-10.1833333,123.5833333], popup="Kota Kupang").add_to(m)
        folium.Marker(location=[-6.332973,106.807915], popup="Kota Baru").add_to(m)
        folium.Marker(location=[-3.328499,114.589203], popup="Kota Banjarmasin").add_to(m)
        folium.Marker(location=[2.767765,117.432145], popup="Kota Tanjung Selor").add_to(m)
        folium.Marker(location=[-3.972201,122.5149028], popup="Kota Kendari").add_to(m)
        folium.Marker(location=[-5.46667,122.633], popup="Kota Bau-Bau").add_to(m)
        # Menampilkan peta ke dalam Streamlit
        folium_static(m,width=1200, height=600)

    if __name__ == '__main__':
        main()