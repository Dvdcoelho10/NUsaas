import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="NUSaas - Atendimento Inteligente", page_icon="🚀")

st.title("🤖 NUSaas: O Futuro do Atendimento")
st.write("Bem-vindo ao portal de inteligência do seu negócio.")

# Configuração da Chave na barra lateral
with st.sidebar:
    st.header("Configuração")
    api_key = st.text_input("Cole sua Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

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
                # Contexto de atendimento
                contexto = "Você é o atendente oficial do NUSaas. Seja profissional e ajude o cliente."
                response = model.generate_content(f"{contexto}\nCliente: {prompt}")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erro na API: {e}")
else:
    st.warning("Insira sua API Key na lateral para começar.")