# -*- coding: utf-8 -*-
"""
2º SEMESTRE – CHALLENGE SPRINT 3:

ORIENTAÇÕES GERAIS:

- Todos os entregáveis deverão conter o nome completo e o número de matrícula de todos os integrantes;

- Todos os integrantes do grupo são responsáveis pela entrega final;

- Não envie links, poste todos os entregáveis diretamente no Portal, nos formatos exigidos;

- Após o prazo de entrega, o sistema não aceitará envios posteriores;

- O(s) arquivo(s) enviado(s) será(ão) o(s) avaliado(s), não sendo permitida substituição após o prazo;

- Será descontado 1,0 ponto por item ausente e/ou não atendido na avaliação.

Objetivo: A partir da base de dados utilizada nas entregas anteriores (ou, alternativamente, de uma nova base ajustada), e assumindo que as variáveis numéricas selecionadas seguem uma Distribuição Normal, escolha uma variável aleatória e realize as seguintes análises utilizando a Linguagem de Programação Python:

01) (2,5 pontos) Probabilidade acima da Mediana:

a) Cálculo da mediana

b) Cálculo da probabilidade.

c) Código estruturado e resultados apresentados corretamente.

d) Classificação correta do evento (raro, pouco provável, provável, quase certo).OBS: Acesse o link abaixo e com base na base de dados escolhida, resolva os exercícios solicitados acima. https://cursos.alura.com.br/forum/topico-calculo-da-probabilidade-da-distribuicao-normal-com-quaisquer-valores-de-media-e-desvio-padrao-195298

02) (2,5 pontos) Probabilidade dentro do intervalo (média ± 2s):

a) Cálculo da média, desvio padrão e intervalo.

b) Cálculo da probabilidade.

c) Código estruturado e resultados apresentados corretamente

d) Classificação correta do evento.

OBS: Acesse o link abaixo e com base na base de dados escolhida, resolva os exercícios solicitados acima. https://cursos.alura.com.br/forum/topico-calculo-da-probabilidade-da-distribuicao-normal-com-quaisquer-valores-de-media-e-desvio-padrao-195298

03) (3,0 pontos) Modelagem com Regressão Linear:

a) Código correto da Regressão Linear em Python (uso adequado de bibliotecas e execução sem erro).

b) Gráfico da reta ajustada com título, eixos e legenda claros.

c) Interpretação dos coeficientes da regressão.

OBS: Acesse o link abaixo e com base na base de dados escolhida, resolva os exercícios solicitados acima. https://www.alura.com.br/conteudo/estatistica-correlacao-regressao?srsltid=AfmBOoqS5tFc1hthi_IuyVE3Pjp2rzo_5keq2EPdt7-FchAr19uxKFxL

04) (2,0 pontos) Organização, clareza e interpretação geral:

a) Entrega em PDF com códigos, gráficos e explicações bem estruturadas.

b) Interpretação dos resultados de forma clara, relacionando estatística e aprendizado de máquina.

05) Em seguida, apenas um representante de cada grupo deverá postar no Portal:a) O arquivo com a base de dados, obrigatoriamente em formato .csv (Comma-Separated Values) ou .xlsx (Excel);

b) Os códigos desenvolvidos, obrigatoriamente em formato .py (Python).

OBS: As entregas devem ser realizadas estritamente conforme as orientações e formatos definidos e trabalhados em aula pelo(a) respectivo(a) professor(a) da disciplina durante o semestre.

## Integrantes

| Nome | RM |
|---|---|
| Natan Silva da Costa | 573100 |
| Leonardo Scotti Tobias | 573305 |
| Luca Almeida Lucareli | 569061 |
| Henrique Almeida Lucareli | 569183 |
| Enzo Seiji Delgado Tabuchi | 573156 |

---
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./smart_home_energy_consumption_large.csv')

col_x = 'Energy Consumption (kWh)'
col_y = 'Outdoor Temperature (°C)'

variavel = df[col_x]

# (2,5 pontos) Probabilidade acima da Mediana:
media = variavel.mean()
desvio_padrao = variavel.std()
mediana = variavel.median()

# P(X > Mediana) = 1 - P(X <= Mediana)
prob_acima_mediana = 1 - norm.cdf(mediana, loc=media, scale=desvio_padrao)

print(f"a) Mediana calculada: {mediana:.4f}")
print(f"b) Probabilidade (X > Mediana): {prob_acima_mediana:.4f} ({(prob_acima_mediana*100):.2f}%)")

# Classificação
if prob_acima_mediana < 0.05: classif_1 = "raro"
elif prob_acima_mediana <= 0.30: classif_1 = "pouco provável"
elif prob_acima_mediana <= 0.70: classif_1 = "provável"
else: classif_1 = "quase certo"

print(f"d) Classificação do evento: {classif_1}\n")


#(2,5 pontos) Probabilidade dentro do intervalo (média ± 2s):
limite_inferior = media - 2 * desvio_padrao
limite_superior = media + 2 * desvio_padrao

# P(Limite_Inferior < X < Limite_Superior)
prob_inferior = norm.cdf(limite_inferior, loc=media, scale=desvio_padrao)
prob_superior = norm.cdf(limite_superior, loc=media, scale=desvio_padrao)
prob_intervalo = prob_superior - prob_inferior

print(f"a) Média: {media:.4f} | Desvio Padrão (s): {desvio_padrao:.4f}\n Intervalo: [{limite_inferior:.4f}, {limite_superior:.4f}]")
print(f"b) Probabilidade P(Média-2s < X < Média+2s): {prob_intervalo:.4f} ({(prob_intervalo*100):.2f}%)")

if prob_intervalo < 0.05: classif_2 = "raro"
elif prob_intervalo <= 0.30: classif_2 = "pouco provável"
elif prob_intervalo <= 0.70: classif_2 = "provável"
else: classif_2 = "quase certo"

print(f"d) Classificação do evento: {classif_2}\n")


#(3,0 pontos) Modelagem com Regressão Linear:
X = df[[col_x]]
y = df[col_y]

modelo = LinearRegression()
modelo.fit(X, y)

coef_linear = modelo.intercept_
coef_angular = modelo.coef_[0]

print(f"a) Código e bibliotecas importadas e executadas com sucesso.")
print(f"c) Coeficiente Linear (Intercepto): {coef_linear:.4f}\n Coeficiente Angular (Inclinação): {coef_angular:.4f}\n")

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='#0078D7', label='Dados Reais (Dispersão)', alpha=0.5, edgecolors='w')
plt.plot(X, modelo.predict(X), color='#D13438', linewidth=2.5, label='Reta de Regressão')
plt.title(f'Regressão Linear Ajustada: {col_x} vs {col_y}', fontsize=14, fontweight='bold')
plt.xlabel(col_x, fontsize=12)
plt.ylabel(col_y, fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
