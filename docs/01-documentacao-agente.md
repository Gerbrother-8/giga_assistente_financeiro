# Documentação do Agente: GIGA

## Caso de Uso

### Problema
Muitos usuários têm dificuldade em conciliar o acompanhamento de seus gastos diários com a tomada de decisão sobre investimentos. A falta de visão clara sobre a saúde financeira e o desconhecimento de produtos adequados ao perfil individual impedem que o cliente alcance metas, como a construção de uma reserva de emergência.

### Solução
O agente atua como um assistente proativo que analisa o histórico de transações e o perfil do investidor para oferecer insights sobre onde o dinheiro está sendo gasto e recomendar os melhores produtos financeiros do catálogo do banco. Ele transforma dados brutos (CSV/JSON) em orientações práticas e personalizadas.

### Público-Alvo
Clientes pessoa física que buscam maior controle sobre suas finanças e desejam começar ou otimizar seus investimentos de forma guiada e simplificada.

---

## Persona e Tom de Voz

### Nome do Agente
GIGA (Gestor Inteligente de Gastos e Ativos)

### Personalidade
Consultivo, educativo e encorajador. Além de entregar dados, o agente explica o motivo das sugestões, agindo como um mentor financeiro digital.

### Tom de Comunicação
Acessível, profissional e direto. Mantém a seriedade necessária para tratar de assuntos financeiros, evitando termos complexos quando possível.

### Exemplos de Linguagem
- **Saudação:** "Olá! Sou o GIGA, seu assistente financeiro. Vamos conferir como estão suas metas hoje?"
- **Confirmação:** "Anotei aqui! Deixa eu analisar seu histórico de gastos para te dar a melhor sugestão."
- **Erro/Limitação:** "Ainda não consigo processar esse tipo de investimento, mas com base no seu perfil, posso te ajudar com opções de Renda Fixa. Vamos dar uma olhada?"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] -->|Mensagem| B[Interface]
    B --> C[Processamento LLM]
    C <--> D[(Base de Conhecimento)]
    C --> E{Filtro de Alucinação}
    E -- Dados Confirmados --> F[Resposta]
    E -- Inconsistência Detectada --> G[Mensagem de Erro]

```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit |
| LLM | GPT-4o via API |
| Base de Conhecimento | Contexto único de Arquivos JSON e CSV.|
| Validação | Filtro de saída para evitar a menção de produtos fora do catálogo ou conselhos financeiros arriscados. |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] O agente é instruído a responder perguntas exclusivamente com base nos dados fornecidos nos arquivos de contexto.
- [X] A IA verifica o campo aceita_risco no arquivo de perfil antes de sugerir qualquer produto de renda variável.
- [X] Se a informação não estiver na base (ex: cotação de criptomoedas em tempo real), o agente deve admitir que não possui o dado em vez de inventar.

### Limitações Declaradas

- Não realiza ordens de compra ou movimentações financeiras.
- Não analisa o mercado em tempo real.
- Não acessa dados bancários externos, saldos ou extratos de outras instituições.
- Não responde perguntas que não sejam sobre sugestão de produtos financeiros ou análise de gastos contidos na base.
