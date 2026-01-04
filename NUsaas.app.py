import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="NUSaas - Infraestrutura de IA", page_icon="🚀")

st.title("🤖 NUSaas: O Futuro do Atendimento")
st.write("Bem-vindo ao portal de inteligência do seu negócio.")

# Configuração da Chave na barra lateral
with st.sidebar:
    st.header("Configuração")
    api_key = st.text_input("Cole sua Gemini API Key:", type="password")
    st.divider()
    st.info("O NUSaas oferece Dashboard, API de Chatbot e Fluxos de Automação.")

if api_key:
    genai.configure(api_key=api_key)
    # Usando gemini-pro para maior compatibilidade
    model = genai.GenerativeModel('gemini-pro')

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Como posso ajudar com sua automação?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                # CONTEXTO ATUALIZADO: Definição do seu modelo de negócio
                contexto = """
                Você é o Especialista de IA do NUSaas. Seu objetivo é ajudar o cliente a entender nossa plataforma.
                O NUSaas é uma plataforma completa que oferece:
                1. Dashboard Inteligente: Para gestão de dados e visualização de métricas de IA.
                2. API para Chatbots: Conectividade fácil para integrar nossa IA em qualquer site ou sistema.
                3. Fluxos de Automação: Ferramenta visual para criar automações complexas (No-Code).

                Planos:
                - Starter: R$ 197/mês (Acesso à API e Dashboard básico).
                - Business: R$ 497/mês (Fluxos de automação ilimitados e suporte VIP).

                Seja profissional, técnico e sempre tente mostrar o valor da automação para o negócio do cliente.
                """
                
                response = model.generate_content(f"{contexto}\nCliente: {prompt}")
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Erro na API: {e}")
else:
    st.warning("Insira sua API Key na lateral para começar.")
