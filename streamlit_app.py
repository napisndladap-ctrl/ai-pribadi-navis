import streamlit as st
import google.generativeai as genai

# Konfigurasi Tampilan Web
st.set_page_config(page_title="AI Pribadi Navis", page_icon="🤖", layout="centered")

st.title("🤖 AI Pribadi Navis")
st.write("Halo Beh! Sekarang aku sudah aktif dan siap diajar ngobrol cerdas.")

# Sediakan tempat buat ngetik API Key langsung di sidebar web (supaya gampang diisi lewat HP)
with st.sidebar:
    st.header("⚙️ Pengaturan AI")
    api_key_input = st.text_input("Masukkan Google Gemini API Key:", type="password")
    st.markdown("[Cara ambil API Key gratis klik di sini](https://aistudio.google.com/)")

if not api_key_input:
    st.warning("⚠️ Masukkan dulu API Key Gemini-mu di kolom samping (sidebar) sebelah kiri untuk mulai mengobrol!")
else:
    try:
        # Konfigurasi API Key dari input pengguna
        genai.configure(api_key=api_key_input)
        
        # Inisialisasi model AI
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Simpan riwayat obrolan di sesi layar
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Tampilkan pesan obrolan sebelumnya
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Kotak input chat di bagian bawah (tampilannya persis kayak aplikasi chat sungguhan!)
        if prompt := st.chat_input("Ketik pesan atau pertanyaanmu di sini, Beh..."):
            # Tambah pesan user ke layar
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate jawaban cerdas dari AI
            with st.chat_message("assistant"):
                with st.spinner("Sedang berpikir..."):
                    chat_session = model.start_chat(history=[])
                    # Mengirim riwayat atau pesan baru
                    response = model.generate_content(prompt)
                    bot_reply = response.text
                    st.markdown(bot_reply)
            
            # Simpan jawaban bot ke riwayat
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            
    except Exception as e:
        st.error(f"Terjadi kesalahan pada API Key atau koneksi: {e}")
