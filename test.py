import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

company = st.selectbox('Brand/Nama HP', df['Nama HP'].unique())

prosesor = st.selectbox('Processor', df['Upd_Processor'].unique())

rating = st.selectbox('Rating', [1, 2, 3, 4, 5])

ram = st.selectbox('RAM/GB',[2,4,8,12])

rom = st.selectbox('ROM/GB',[4,8,16,32,64,128,512])

baterai = st.selectbox('Battery',[1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000])

size_back_cam = st.selectbox('Size Kamera Belakang (MP)',[5,10,50,100,200])

total_back_cam = st.selectbox('Total Kamera Belakang',[1,2,3,4])

size_front_cam = st.selectbox('Size Kamera Depan (MP)',[5,10,15,20,30,50])

total_front_cam = st.selectbox('Total Kamera Depan',[1,2])



if st.button('Predict Price'):
    query = np.array([company,rating,ram,rom,baterai,size_back_cam,total_back_cam,size_front_cam,total_front_cam,prosesor], dtype=object)
    query = query.reshape(1,10)
    st.title("predicted in IDR : Rp " + str(int(np.exp(pipe.predict(query)[0]))))