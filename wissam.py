import streamlit as st
import google.generativeai as genai
import time

# 1. I3dadat dyal l'app (Interface)
st.set_page_config(page_title="Chat-AI Wa3ra", page_icon="🤖", layout="centered")

# CSS bach nzow9o l'app chwiya
st.markdown("""
<style>
    .stChatFloatingInputContainer {
        padding-bottom: 20px;
    }
    .title {
        text-align: center;
        color: #4CAF50;
        font-family: 'Arial';
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>✨ App Chat b l'AI</h1>", unsafe_allow_html=True)
st.write("Hadi application dyal chat msawba b Python w katkhdem b dak2 stina3i (Gemini).")

# 2. API Key dyal AI (Darouri bach ykhdem l'AI)
# (Khas ykon 3ndek API key mn Google AI Studio - fabor)
API_KEY = st.sidebar.text_input("🔑 Dkhel API Key dyal Gemini hna:", type="password")
st.sidebar.markdown("[Kliqi hna bach tjib API Key fabor](https://aistudio.google.com/app/apikey)")

# 3. Nkhabbiw lmessages f session bach maymchiwch mnin ndiro actualiser
if "messages" not in st.session_state:
    st.session_state.messages = []

# Nbiyno lmessages l9dam
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Blassa fin kykteb l'utilisateur
if prompt := st.chat_input("Kteb risala dyalek hna..."):
    # Nziyfo lmsg dyal l'utilisateur l session
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. L'AI kyjaweb (Gemini)
    with st.chat_message("assistant"):
        if not API_KEY:
            st.error("⚠️️ Darouri dir API Key f jnab (Sidebar) bach njawbek!")
        else:
            try:
                # I3dad dyal Gemini
                genai.configure(api_key=API_KEY)
                model = genai.GenerativeModel('gemini-pro')
                
                # Animation sghira dyl loading
                message_placeholder = st.empty()
                message_placeholder.markdown("⏳ Kayfker...")
                
                # Njibo ljawab
                response = model.generate_content(prompt)
                
                # Nbiyno ljawab m9ad
                message_placeholder.markdown(response.text)
                
                # Nkhabiw ljawab f session
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
            except Exception as e:
                st.error(f"W9e3 mouchkil: {e}")
