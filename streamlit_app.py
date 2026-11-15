import streamlit as st
import subprocess
import sys

# Instal otomatis modul AI khusus untuk tampilan HP
try:
    import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

st.set_page_config(page_title="AI Pribadi Navis", page_icon="🤖", layout="centered")

st.title("🤖 AI Pribadi Navis")
st.write("Halo Beh! Sekarang aplikasinya sudah siap.")

with st.sidebar:
    st.header("⚙️ Pengaturan")
    api_key_input = st.text_input("Masukkan API Key:", type="password")
    st.markdown("[Ambil API Key gratis di sini](https://aistudio.google.com/)")

if not api_key_input:
    st.warning("⚠️ Masukkan dulu API Key Gemini-mu di menu sebelah kiri ya, Beh!")
else:
    try:
        genai.configure(api_key=api_key_input)
        model = genai.GenerativeModel("gemini-2.5-flash")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Ketik pesan di sini..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("Mengetik..."):
                    chat_session = model.start_chat(history=[])
                    response = chat_session.send_message(prompt)
                    bot_reply = response.text
                    st.markdown(bot_reply)

            st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        st.error(f"Error: {e}")
