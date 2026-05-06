import pandas as pd
import plotly.express as px

## Dicionário de Dados: Consumo de Energia Residencial

# Este documento descreve os campos e metadados contidos no conjunto de dados de consumo de energia.

# A GoodWe não fabrica apenas inversores, ela fornece ecossistemas onde o usuário monitora para onde a energia solar está indo. O dataset detalha o "Appliance Type", o que permite à GoodWe aprimorar algoritmos que dizem ao cliente, "Sua geladeira está consumindo mais do que o normal".

# ### Atributo
# Home ID- Um identificador exclusivo para cada residência (anonimizado).
# Appliance Type- O eletrodoméstico específico em uso (ex: Geladeira, Forno, Aquecedor).
# Energy Consumption (kWh)- Energia consumida pelo aparelho em quilowatts-hora (kWh).
# Time- O horário em que ocorreu o consumo de energia (formato 24 horas).
# Date- A data em que o consumo de energia foi registrado (AAAA-MM-DD).
# Outdoor Temperature (°C)- A temperatura externa no momento do consumo de energia, em graus Celsius.
# Season- A estação do ano (Inverno, Verão, Outono, Primavera).
# Household Size- Número de pessoas residentes na casa.


df= pd.read_csv('./smart_home_energy_consumption_large.csv')

print(df)

## a) 1 variável quantitativa discreta, na sequência, extraia pelo menos 2 insights da tabela utilizando #: **Household Size**

### Esta variável é classificada como quantitativa discreta pois representa uma contagem de unidades inteiras (pessoas), onde não existem valores fracionários (não é possível ter 2,5 pessoas em uma casa).
### Insights Extraídos:

# - Distribuição:

# A distribuição do tamanho das residências apresenta proporções muito semelhantes entre todas as categorias, com frequências próximas de 20%. Isso indica uma distribuição equilibrada, sem predominância de um tamanho específico de residência na amostra.

# Essa uniformidade permite análises comparativas mais consistentes entre diferentes tamanhos de residência, reduzindo o viés causado por concentração de dados em uma única categoria.

# - Ligação com consumo

# Como a distribuição dos tamanhos das residências é equilibrada entre todas as categorias, o consumo energético pode ser analisado de forma comparativa entre diferentes perfis de domicílio, sem que uma categoria específica influencie de forma desproporcional os resultados.

# Essa distribuição uniforme permite investigar diferenças no consumo energético entre residências com diferentes números de moradores, possibilitando identificar padrões de eficiência sem viés causado por concentração de dados.

freq = df["Household Size"].value_counts().sort_index()

freq_rel = df["Household Size"].value_counts(normalize=True).sort_index()

tabela = pd.DataFrame({
    "Frequência": freq,
    "Frequência Relativa (%)": freq_rel * 100
})

print(tabela)


## b) 1 variável quantitativa contínua, na sequência, extraia pelo menos 2 insights da tabela utilizando #. **Energy Consumption (kWh)**

### Esta variável é quantitativa contínua pois representa uma medição física que pode assumir qualquer valor dentro de um intervalo, incluindo casas decimais (ex: 10,55 kWh).
### Insights Extraídos:

# - Concentração: 

# A maior parte dos valores de consumo está concentrada nas faixas mais baixas de kWh, especialmente no intervalo inicial, que apresenta a maior frequência. Isso indica que a maioria dos aparelhos possui consumo energético reduzido, caracterizando um padrão geral de baixo consumo na amostra.

# - Anomalia: 

# As faixas superiores de consumo apresentam baixa frequência (cerca de 3% cada), indicando que poucos casos concentram níveis elevados de consumo energético. Esses valores podem representar situações de uso intensivo ou possíveis ineficiências operacionais, como funcionamento contínuo de equipamentos, o que justifica a necessidade de monitoramento e ações de manutenção preventiva.

df["kWh_bin"] = pd.cut(df["Energy Consumption (kWh)"], bins=10)

freq = df["kWh_bin"].value_counts().sort_index()

tabela_kwh = pd.DataFrame({
    "Frequência": freq,
    "Frequência Relativa (%)": (freq / freq.sum()) * 100
})

print(tabela_kwh)



### 03) (2,0 pontos) Elaborar um relatório técnico contendo os principais insights obtidos nas análises realizadas nos itens 01 e 02, destacando de que forma os resultados podem contribuir para a tomada de decisão e/ou geração de valor para a empresa.

# A análise dos dados de consumo energético residencial permitiu identificar padrões relevantes tanto na distribuição das residências quanto no comportamento de consumo dos aparelhos. A distribuição equilibrada do tamanho das residências garante que as análises comparativas sejam realizadas sem viés, permitindo avaliar de forma confiável o impacto do número de moradores no consumo energético.

# Além disso, a concentração do consumo em faixas mais baixas indica que a maioria dos aparelhos opera dentro de padrões esperados, enquanto a presença de valores elevados em menor frequência possibilita a identificação de potenciais anomalias. Esses casos representam oportunidades estratégicas para detecção de ineficiências energéticas, como equipamentos com alto consumo ou funcionamento contínuo.

# Do ponto de vista da empresa GoodWe, esses resultados podem ser aplicados no desenvolvimento de sistemas inteligentes de monitoramento energético, capazes de identificar automaticamente padrões anormais de consumo e gerar alertas ao usuário. Isso agrega valor ao serviço oferecido, permitindo ações de manutenção preventiva, redução de custos energéticos e aumento da eficiência no uso da energia.

# Dessa forma, a utilização de análise de dados no consumo residencial não apenas contribui para a compreensão dos padrões de uso, mas também possibilita a criação de soluções tecnológicas que geram valor tanto para a empresa quanto para o consumidor final.