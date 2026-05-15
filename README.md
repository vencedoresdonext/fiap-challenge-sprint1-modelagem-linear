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

- Python
- Pandas
- Plotly (para visualização)

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

**Concentração:**
- A maior parte dos dados está nas faixas mais baixas de consumo.
- Indica que a maioria dos aparelhos possui consumo reduzido.

**Anomalias:**
- Faixas de alto consumo possuem baixa frequência (~3%).
- Podem indicar:
  - uso intensivo
  - ineficiência energética
  - funcionamento contínuo de equipamentos

---

## Aplicação para a Empresa (GoodWe)

Os resultados desta análise podem gerar valor para a GoodWe através de:

- Monitoramento inteligente de consumo
- Detecção automática de anomalias
- Geração de alertas de manutenção preventiva
- Redução de custos energéticos para o usuário
- Otimização do uso de energia solar

Exemplo prático:
> Um equipamento com consumo elevado e constante pode indicar falha, permitindo intervenção antecipada.

---

## Estrutura do Projeto
projeto

├── smart_home_energy_consumption_large.csv

├── analise.py

├── README.md


---

## Como Executar

1. Instale as dependências:
```bash
pip install pandas plotly
```

## Conclusão

A análise permitiu identificar padrões relevantes no consumo energético residencial, destacando a predominância de baixo consumo e a existência de casos específicos de alto consumo que podem indicar anomalias.

Esses insights demonstram como a análise de dados pode ser aplicada para gerar valor estratégico, tanto para empresas quanto para consumidores.
