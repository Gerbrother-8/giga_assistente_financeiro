# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Fornece contexto sobre dúvidas anteriores e padrões de suporte. |
| `perfil_investidor.json` | JSON | Define o perfil de risco, metas e limites do cliente. |
| `produtos_financeiros.json` | JSON | Serve como o catálogo oficial de produtos para recomendações de investimento. |
| `transacoes.csv` | CSV | Permite a análise de fluxo de caixa e identificação de hábitos de consumo. |

---

## Adaptações nos Dados

Nenhuma adaptação ou expansão foi realizada nos dados mockados originais.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos são carregados em memória no início da execução da aplicação (utilizando as bibliotecas `pandas` para os arquivos CSV e `json` para os arquivos JSON). Os dados são convertidos em strings estruturadas ou dicionários para fácil manipulação pelo orquestrador.

### Como os dados são usados no prompt?
Os dados são injetados dinamicamente no System Prompt (Contexto do Sistema). Antes de cada interação, o agente recebe um resumo atualizado do perfil do usuário, saldo calculado e catálogo de produtos, garantindo que qualquer resposta gerada pela LLM esteja ancorada nestes fatos (técnicas de Few-Shot Prompting e Context Injection).

---

## Exemplo de Contexto Montado

Abaixo, um exemplo de como as informações são organizadas internamente antes de serem enviadas para a IA:

```
[CONTEXTO DO USUÁRIO]
- Cliente: João Silva (32 anos)
- Perfil: Moderado
- Meta Atual: Completar reserva de emergência (Faltam R$ 5.000,00)
- Renda Mensal: R$ 5.000,00

[EXTRATO RECENTE]
- 01/10: Salário (Entrada: R$ 5.000,00)
- 02/10: Aluguel (Saída: R$ 1.200,00)
- 03/10: Supermercado (Saída: R$ 450,00)

[CATÁLOGO DISPONÍVEL]
- Tesouro Selic (Risco Baixo | Aporte mín: R$ 30,00)
- CDB Liquidez Diária (Risco Baixo | Aporte mín: R$ 100,00)
- Fundo Multimercado (Risco Médio | Aporte mín: R$ 500,00)
```
