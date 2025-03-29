import streamlit as st
import pickle
import numpy as np

# Modeli yükle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("📊 iPhone13 Fiyat Tahmin Uygulaması")

# Kullanıcıdan giriş al
pil = st.slider("Pil Kapasitesi (%)", min_value=0.0, max_value=100.0, step=1.0)
kasa = st.slider("Kasa Durumu (0-10)", min_value=0.0, max_value=10.0, step=1.0)
garanti = st.radio("Garanti Durumu", ["Var", "Yok"])

garanti_value = 1.0 if garanti == "Var" else 0.0

if st.button("Tahmin Yap"):
    input_data = np.array([[pil, garanti_value, kasa]])
    predicted_price = model.predict(input_data)[0]
    st.success(f"📢 Tahmini Fiyat: {predicted_price:.2f} TL")
