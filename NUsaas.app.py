import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="NUSaas - Infraestrutura de IA", page_icon="🚀")
st.title("🤖 NUSaas: Inteligência de Negócio")

with st.sidebar:
    st.header("Configuração")
    api_key = st.text_input("AIzaSyBTAB2rpo2XdtPveqcvlWA3pbg8ImKBDJg:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Como posso ajudar?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                contexto = "Você é o especialista do NUSaas (Dashboard, API e Automação)."
                response = model.generate_content(f"{contexto}\n{prompt}")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erro na API: {e}")
else:
    st.warning("Insira sua API Key na lateral para começar.")
