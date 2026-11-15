import streamlit as st

st.title("🤖 AI Pribadi Navis")
st.write("Halo Beh! Website AI pertamamu berhasil jalan nih.")

pesan = st.text_input("Mau ngobrol apa sama AI?")
if pesan:
    st.success(f"Kamu ngetik: '{pesan}' — Mantap, sistemnya nyambung!")
