# 💰 GIGA - Gestor Inteligente de Gastos e Ativos

## Contexto

O **GIGA** é um assistente financeiro inteligente desenvolvido como projeto final do Bootcamp Bradesco - GenAI & Dados. Ele transforma a experiência bancária de simples consultas em uma jornada consultiva e proativa. Focado na simplicidade e agilidade, o GIGA utiliza IA Generativa para:

- **Analisar transações:** identifica padrões no fluxo de caixa.
- **Personalizar investimentos:** Sugere produtos baseados no perfil do usuário.
- **Segurança Normativa:** Opera sob regras rígidas que distinguem sugestões informativas de recomendações profissionais.
- **Confiabilidade:** As respostas passam por filtros de verificação de veracidade.

---

## Estrutura do Projeto

### 1. Documentação do Agente

O GIGA resolve o problema da fragmentação de informações financeiras, unindo a visão de gastos com a oportunidade de investimento. Sua persona é consultiva, educativa e encorajadora.

- **Arquitetura:** Baseada em um orquestrador de IA que consome arquivos estruturados e valida as respostas através de filtros de verificação de veracidade.
- **Segurança:** Implementação de travas de contexto para garantir que o agente não alucine transações ou dados externos.

📄 [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

O agente é alimentado por quatro pilares de dados mockados que garantem a precisão das análises:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico detalhado de entradas e saídas. |
| `historico_atendimento.csv` | CSV | Fornece contexto sobre dúvidas anteriores e padrões de suporte. |
| `perfil_investidor.json` | JSON | Define o perfil de risco, metas e limites do cliente. |
| `produtos_financeiros.json` | JSON | Catálogo oficial de produtos de investimento. |

📄 [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

A inteligência do GIGA é moldada por prompts estruturados que utilizam técnicas de *Few-Shot Prompting*:

- **System Prompt:** Define a proibição do termo "recomendar" e a obrigatoriedade da checagem do campo `aceita_risco`.
- **Edge Cases:** Protocolos para lidar com perguntas fora de escopo e tentativas de acesso a dados sensíveis.

📄 [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

O protótipo desenvolvido em Python, processa de dados via Pandas, utiliza a interface do Streamlit e a capacidade de linguagem natural do modelo Gemini 2.5 Flash.

- **Interface:** Streamlit para uma interação rápida e limpa.
- **Integração:** Conexão direta com as APIs do Gemini.

📄 [`src/app.py`](./src/app.py)

---

### 5. Avaliação e Métricas

O GIGA foi testado e aprovado por meio de testes de estresse de prompt (red teaming) e validação de consistência de dados:
- **Métricas:** Precisão na extração, cálculo e apresentação de valores.
- **Testes:** Validação de dados e proteção contra tentativas de mau uso do assistente.

📄 [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Apresentação estratégica da solução GIGA, focando em como a IA pode converter dados em saúde financeira para os clientes.

📄 [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Ferramentas Utilizadas

| Categoria | Ferramenta |
|-----------|-------------|
| **Linguagem** | Python 3.x |
| **Processamento de dados** | Pandas |
| **LLM** | Gemini 2.5 Flash |
| **Interface** | Streamlit |

---

## Estrutura do Repositório

```
📁 giga_assistente_financeiro
│
├── 📄 README.md                      #Resumo do projeto
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
    └── app.py                        # Código do chatbot
    └── requirements.txt              # Bibliotecas externas utilizadas
```
