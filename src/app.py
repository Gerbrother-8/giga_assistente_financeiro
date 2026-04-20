import streamlit as st
import pandas as pd
import json
import os
from google import genai
from datetime import datetime

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="GIGA - Gestor Inteligente de Gastos e Ativos",
    page_icon="💰",
    layout="centered"
)

st.title("💰 GIGA")
st.caption("Gestor Inteligente de Gastos e Ativos")

# ==========================================
# 2. CARREGAMENTO DOS DADOS
# ==========================================

@st.cache_data
def carregar_dados_locais():
    caminho_base = r"C:\Users\germa\OneDrive\Documentos\Chatbot GIGA\data"
    try:
        perfil = json.load(open(os.path.join(caminho_base, 'perfil_investidor.json'), encoding='utf-8'))
        produtos = json.load(open(os.path.join(caminho_base, 'produtos_financeiros.json'), encoding='utf-8'))
        transacoes = pd.read_csv(os.path.join(caminho_base, 'transacoes.csv'))
        historico = pd.read_csv(os.path.join(caminho_base, 'historico_atendimento.csv'))
        return perfil, produtos, transacoes, historico
    except Exception as e:
        st.error(f"Erro ao carregar arquivos em {caminho_base}: {e}")
        return None, None, None, None

perfil, produtos, transacoes, historico_atend = carregar_dados_locais()

# ==========================================
# 3. CONSTRUÇÃO DA INSTRUÇÃO DO SISTEMA
# ==========================================

def criar_instrucao_sistema(perfil, produtos, transacoes, historico):
    nome_usuario = perfil.get('nome', 'João Silva')
    aceita_risco = perfil.get('aceita_risco', False)
    
    prompt = f"""
Você é o GIGA (Gestor Inteligente de Gastos e Ativos), um assistente financeiro inteligente. Seu objetivo é ajudar seu cliente a gerir sua saúde financeira e alcançar suas metas de investimento através de análises de dados e sugestões personalizadas.

REGRAS:
1. Utilize exclusivamente os dados fornecidos nos arquivos de contexto abaixo. Não utilize dados em tempo real.
2. O agente deve sempre utilizar os termos "sugerir" ou "sugestão". É proibido utilizar os termos "recomendar" ou "recomendação", principalmente ao falar sobre produtos financeiros.
3. Mantenha uma personalidade consultiva, educativa e encorajador.
4. Utilize um tom profissional, mas acessível, evitando termos técnicos complexos sem explicação.
5. Antes de sugerir qualquer investimento, verifique o campo 'aceita_risco'. Como o valor atual é '{aceita_risco}', se for 'false', apresente apenas opções de Renda Fixa com risco 'baixo'.
6. Se a informação solicitada não estiver nos arquivos ou se o usuário pedir dados em tempo real, responda que não possui essa informação no momento.
7. O agente não tem autorização para realizar compras, transferências ou qualquer movimentação financeira direta.

CONTEXTO DE DADOS:
---
PERFIL: {json.dumps(perfil, ensure_ascii=False)}
PRODUTOS: {json.dumps(produtos, ensure_ascii=False)}
TRANSAÇÕES: {transacoes.to_string(index=False)}
HISTÓRICO: {historico.to_string(index=False)}
---
"""
    return prompt

# ==========================================
# 4. CONFIGURAÇÕES LATERAIS E API KEY
# ==========================================

with st.sidebar:
    st.header("Configurações do Chat")
    api_key = st.text_input("Gemini API Key:", type="password")
    
    if st.button("Limpar Histórico"):
        st.session_state.chat_history = []
        st.rerun()

# ==========================================
# 5. INICIALIZAÇÃO DO ESTADO DO CHAT
# ==========================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==========================================
# 6. EXIBIÇÃO DA CONVERSA
# ==========================================

for mensagem in st.session_state.chat_history:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])

# ==========================================
# 7. PROCESSAMENTO DE ENTRADA E RESPOSTA
# ==========================================

if prompt_usuario := st.chat_input("Como posso ajudar suas finanças hoje?"):
    
    if not api_key:
        st.warning("Por favor, insira a sua API Key no menu lateral.")
        st.stop()

    with st.chat_message("user"):
        st.markdown(prompt_usuario)
    
    st.session_state.chat_history.append({"role": "user", "content": prompt_usuario})

    try:
        client = genai.Client(api_key=api_key)
        
        instrucao_giga = criar_instrucao_sistema(perfil, produtos, transacoes, historico_atend)
        
        historico_formatado = []
        for m in st.session_state.chat_history[:-1]:
            role_google = "model" if m["role"] == "assistant" else "user"
            historico_formatado.append({"role": role_google, "parts": [{"text": m["content"]}]})

        resposta = client.models.generate_content(
            model='gemini-2.5-flash',
            config={
                'system_instruction': instrucao_giga,
                'temperature': 0.7
            },
            contents=historico_formatado + [{"role": "user", "parts": [{"text": prompt_usuario}]}]
        )

        with st.chat_message("assistant"):
            st.markdown(resposta.text)
        
        st.session_state.chat_history.append({"role": "assistant", "content": resposta.text})

    except Exception as e:
        st.error(f"Erro ao processar solicitação: {e}")