# Documentação do Agente: FinMatcher

## Caso de Uso

### Problema
O cliente possui capital disponível, mas não sabe qual produto financeiro do catálogo do banco é adequado ao seu perfil de risco e objetivos.

### Solução
O agente analisa o perfil do investidor (JSON) e cruza com o catálogo de produtos disponíveis (JSON) para recomendar a opção mais segura e compatível de forma instantânea.

### Público-Alvo
Clientes iniciantes que buscam orientações rápidas sobre onde alocar seus recursos de acordo com seu perfil.

---

## Persona e Tom de Voz

### Nome do Agente
FinMatcher

### Personalidade
Direto e objetivo. O agente foca em dar respostas curtas e precisas, sem rodeios ou conversas informais excessivas.

### Tom de Comunicação
Técnico-acessível. Utiliza termos do mercado, mas explica de forma que o cliente entenda o motivo da recomendação.

### Exemplos de Linguagem
- **Saudação:** "Olá. Sou o FinMatcher. Com base no seu perfil, encontrei o melhor investimento para você."
- **Confirmação:** "Analisando seu perfil [X] e os produtos disponíveis..."
- **Erro/Limitação:** "Não encontrei produtos compatíveis com seu perfil na base atual."

---

## Arquitetura

### Diagrama

```mermaid
flowchart LR
    A[Usuário] --> B(FinMatcher)
    B --> C{Base de Dados}
    C -->|Perfil + Produtos| B
    B --> D[Recomendação]

```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Chatbot em Streamlit] |
| LLM | [Gemini 1.5 Flash] |
| Base de Conhecimento | [Arquivos JSON de Perfil e Produtos] |
| Validação | [Filtro de saída para garantir que apenas produtos do catálogo sejam citados] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] [O agente está programado para ignorar perguntas que não sejam sobre recomendação de produtos.]
- [X] [Proibido sugerir qualquer produto que não esteja explicitamente listado no arquivo produtos_financeiros.json]
- [X] [Se o usuário perguntar algo que não seja sobre recomendação de produtos, o agente responde que só conhece os produtos oficiais do banco.]

### Limitações Declaradas
> O que o agente NÃO faz?

- Não realiza ordens de compra.
- Não analisa o mercado em tempo real.
- Não acessa dados bancários externos ou saldos de outras instituições.
- Não responde perguntas que não sejam sobre recomendação de produtos.
