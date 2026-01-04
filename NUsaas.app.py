import streamlit as st
import google.generativeai as genai

# 1. Configuração da página e Estilo
st.set_page_config(page_title="NUSaas - Infraestrutura de IA", page_icon="🚀", layout="wide")

st.title("🤖 NUSaas: Inteligência de Negócio")
st.markdown("---")

# 2. Barra Lateral para Configuração
with st.sidebar:
    st.header("⚙️ Configuração")
    api_key = st.text_input("Cole sua Gemini API Key:", type="password")
    st.divider()
    st.info("""
    **O que é o NUSaas?**
    * Dashboard de Métricas
    * API para Chatbots
    * Fluxos de Automação No-Code
    """)

# 3. Lógica do Chatbot
if api_key:
    try:
        genai.configure(api_key=api_key)
        # Usando gemini-pro para garantir compatibilidade total
        model = genai.GenerativeModel('gemini-pro')

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Exibe o histórico de mensagens
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Entrada do usuário
        if prompt := st.chat_input("Como posso ajudar com sua automação?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # Treinamento do Bot
                contexto = """
                Você é o Especialista de IA do NUSaas. 
                Sua missão é vender e explicar a plataforma NUSaas.
                Serviços: Dashboard de métricas, API para Chatbots e Fluxos de Automação No-Code.
                Planos: Starter (R$ 197/mês) e Business (R$ 497/mês).
                Responda de forma profissional, curta e técnica.
                """
                
                full_prompt = f"{contexto}\n\nCliente perguntou: {prompt}"
                response = model.generate_content(full_prompt)
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"Erro na conexão com o Google: {e}")
        st.info("Dica: Verifique se sua API Key está correta e se o modelo gemini-pro está disponível.")
else:
    st.warning("⚠️ Por favor, insira sua API Key na barra lateral para ativar a inteligência.")

# 4. Rodapé Visual (Opcional - Simulação de Dashboard)
if api_key:
    st.markdown("---")
    st.subheader("📊 Prévia do seu Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Requisições API", "1.250", "+12%")
    col2.metric("Automações Ativas", "42", "稳定")
    col3.metric("Tempo de Resposta", "0.8s", "-0.2s")
