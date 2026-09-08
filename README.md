# Análise de Consumo de Energia Residencial

## Descrição do Projeto

Este projeto tem como objetivo analisar dados de consumo de energia residencial, com foco na identificação de padrões de uso e possíveis anomalias operacionais. A análise foi realizada utilizando Python e a biblioteca Pandas, com base em um conjunto de dados realista.

O estudo está alinhado com o contexto da empresa **GoodWe**, que atua no monitoramento inteligente de energia, permitindo identificar comportamentos de consumo e gerar insights para otimização energética.

---

## Dicionário de Dados

O dataset contém as seguintes variáveis:

| Atributo | Descrição |
|--------|----------|
| Home ID | Identificador único da residência |
| Appliance Type | Tipo de eletrodoméstico (Geladeira, Aquecedor, etc.) |
| Energy Consumption (kWh) | Consumo de energia em kWh |
| Time | Horário do consumo |
| Date | Data do registro |
| Outdoor Temperature (°C) | Temperatura externa |
| Season | Estação do ano |
| Household Size | Número de moradores |

---

## Tecnologias Utilizadas

- **Python** (Linguagem base)
- **Pandas** (Manipulação e limpeza de dados)
- **Plotly / Matplotlib** (Visualização interativa e estática)
- **SciPy** (Cálculos estatísticos e probabilidade)
- **Scikit-Learn** (Modelagem preditiva e Regressão Linear)

---

## Análise 1 — Variável Quantitativa Discreta  
### Household Size

### Classificação
Variável quantitativa discreta, pois representa contagem de indivíduos.

### Insights

**Distribuição:**
- As frequências são aproximadamente iguais (~20% cada).
- Isso indica uma **distribuição equilibrada**, sem predominância de um tamanho de residência.

**Implicação:**
- Permite análises comparativas sem viés.
- Nenhuma categoria influencia desproporcionalmente os resultados.

---

## Análise 2 — Variável Quantitativa Contínua  
### Energy Consumption (kWh)

### Classificação
Variável quantitativa contínua, pois representa uma medição com valores decimais.

### Insights

**Concentração e Probabilidade:**
- A maior parte dos dados reais de mercado concentra-se nas faixas mais baixas de consumo, indicando que a maioria dos aparelhos possui consumo reduzido e eficiente.
- A probabilidade dos eventos ocorrerem no intervalo da Média ± 2 Desvios Padrões foi validada matematicamente (~95,45%), o que enquadra o uso padrão na curva de distribuição normal.

**Anomalias:**
- Faixas de alto consumo possuem baixa frequência (~3%).
- Podem indicar:
  - Uso intensivo atípico
  - Ineficiência energética (aparelhos antigos/defeituosos)
  - Funcionamento contínuo ininterrupto de equipamentos (fugas de energia)

---

## Análise 3 — Modelagem Preditiva  
### Temperatura Externa vs Consumo de Energia (Regressão Linear)

### Objetivo
Entender como a variação climática afeta o consumo elétrico residencial utilizando Machine Learning supervisionado.

### Insights

**Correlação Linear:**
- O modelo identificou o coeficiente de inclinação entre a Temperatura Externa (X) e o Consumo (Y). 
- Permitiu mapear a taxa exata de aumento de consumo em kWh a cada grau Celsius (°C) alterado no ambiente externo, filtrando cenários de alta correlação (como uso de ar-condicionado no verão) de cenários de ruído estatístico (distribuição uniforme).

---

## Aplicação para a Empresa (GoodWe)

Os resultados desta análise podem gerar grande valor estratégico para a GoodWe através de:

- **Monitoramento inteligente:** Dashboards preditivos com base nos padrões estatísticos encontrados.
- **Detecção automática de anomalias:** Identificação de picos de energia que fogem do intervalo Z-Score da média.
- **Manutenção preventiva:** Geração de alertas quando um equipamento apresenta consumo elevado constante, permitindo intervenção antecipada antes de uma falha crítica.
- **Otimização de ROI (Retorno sobre Investimento):** Otimização da distribuição de energia solar com base nas previsões climáticas da regressão linear.

---

## Estrutura do Projeto

```text
projeto/
├── smart_home_energy_consumption_large.csv   # Dataset utilizado
├── analise.py                                # Script de exploração e visualização
├── challenge_sprint3.py                      # Script de Modelagem Linear e Probabilidade
├── relatorio_estatistico.pdf                 # Interpretação dos resultados
└── README.md                                 # Documentação do projeto
