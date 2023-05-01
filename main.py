import streamlit as st
import extra_streamlit_components as stx

st.title ('✨Menghitung Konsentrasi Terukur dan Kadar Suatu Zat Dalam Sampel✨')
st.write('---')

left_column, right_column = st.columns(2)
with left_column:
    st.write('_Intro_ - Aplikasi ini bertujuan untuk memudahkan dalam menghitung konsentrasi terukur dan kadar dalam sampel. Sampel tersebut dapat berupa cairan, bubuk (padatan) atau dalam bentuk tablet.')
with right_column:
    st.write('''KELOMPOK 1 (1E - PMIP) :
1.	Andhika Maulana Ramadhan 		(2220444)
2.	Khalisa Aprilla				(2220462)
3.	Khansa Khaeriyah			(2220464)
4.	Nisa Fauzia Zufar 			(2220477)
5.	Zahraa Dwi Nurazizah			(2220500)
''')
st.write('---')

tab = stx.tab_bar(data=[
    stx.TabBarItemData(id="Cairan", description="", title="Cairan"),
    stx.TabBarItemData(id="Bubuk", description="", title="Bubuk"),
    stx.TabBarItemData(id="Tablet", description="", title="Tablet")
])

if tab == "Cairan":
    absorbansi = st.number_input('Masukkan Absorbansi', key='first_tab_Masukkan_Absorbansi', format='%f')
    intersep = st.number_input('Masukkan Intersep', key='first_tab_Masukkan_Intersep', format='%f')
    slope = st.number_input('Masukkan Slope', key='first_tab_Masukkan_Slope', format='%f')
    fp = st.number_input('Masukkan fp (_jika tidak ada isi 1_)', key='first_tab_Masukkan_fp_(_jika_tidak_ada_isi_1_)', format='%f')
    tombol = st.button ('Hitung')
    if tombol :
        konsentrasi_terukur = (absorbansi - intersep)/slope
        kadar = konsentrasi_terukur*fp
        st.success (f'Konsentrasi Terukur adalah {konsentrasi_terukur:.4f} mg/l')
        st.success (f'Kadar dalam sampel adalah {kadar:.2f} mg/l')

elif tab == "Bubuk":
    absorbansi = st.number_input('Masukkan Absorbansi', key='first_tab_Masukkan_Absorbansi', format='%f')
    intersep = st.number_input('Masukkan Intersep', key='first_tab_Masukkan_Intersep', format='%f')
    slope = st.number_input('Masukkan Slope', key='first_tab_Masukkan_Slope', format='%f')
    fp = st.number_input('Masukkan fp (_jika tidak ada isi 1_)', key='first_tab_Masukkan_fp_(_jika_tidak_ada_isi_1_)', format='%f')
    volume_sampel = st.number_input('Masukkan Volume Sampel _(mL)_', key='first_tab_Masukkan_Volume_Sampel_(mL)', format='%f')
    bobot_sampel = st.number_input('Masukkan Bobot Sampel _(gram)_', key='first_tab_Masukkan_Bobot_Sampel_(gram)', format='%f')
    tombol = st.button ('Hitung')
    if tombol :
        konsentrasi_terukur = (absorbansi - intersep)/slope
        kadar = konsentrasi_terukur*volume_sampel/bobot_sampel
        st.success (f'Konsentrasi Terukur adalah {konsentrasi_terukur:.4f} mg/l')
        st.success (f'Kadar dalam sampel adalah {kadar:.2f} mg/kg')
        
elif tab == "Tablet":
    absorbansi = st.number_input('Masukkan Absorbansi', key='first_tab_Masukkan_Absorbansi', format='%f')
    intersep = st.number_input('Masukkan Intersep', key='first_tab_Masukkan_Intersep', format='%f')
    slope = st.number_input('Masukkan Slope', key='first_tab_Masukkan_Slope', format='%f')
    fp = st.number_input('Masukkan fp (_jika tidak ada isi 1_)', key='first_tab_Masukkan_fp_(_jika_tidak_ada_isi_1_)', format='%f')
    volume_sampel = st.number_input('Masukkan Volume Sampel _(Liter)_', key='first_tab_Masukkan_Volume_Sampel_(Liter)', format='%f')
    bobot_sampel = st.number_input('Masukkan Bobot Sampel _(Kg)_', key='first_tab_Masukkan_Bobot_Sampel_(Kg)', format='%f')
    rata_rata_bobot_tablet= st.number_input('Masukkan Rata-rata Bobot Tablet _(Kg)_', key='first_tab_Masukkan_Rata-rata_Bobot_Tablet_(Kg)', format='%f')
    tombol = st.button ('Hitung')
    if tombol :
        konsentrasi_terukur = (absorbansi - intersep)/slope
        kadar_dalam_sampel = konsentrasi_terukur*volume_sampel/bobot_sampel
        kadar_dalam_tablet = kadar_dalam_sampel*rata_rata_bobot_tablet
        st.success (f'Konsentrasi Terukur adalah {konsentrasi_terukur:.4f} mg/l')
        st.success (f'Kadar dalam sampel adalah {kadar_dalam_sampel:.2f} mg/kg')
        st.success (f'Kadar dalam tablet adalah {kadar_dalam_tablet:.2f} mg/Tablet')

else: 
    result = "Select an option first"