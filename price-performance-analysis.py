import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Caregando o dataset para analises 
df_merged = pd.read_csv('data/processed/merged_data.csv')

# Calcular a média da taxa da empresa e das concorrentes por corredor
analise_comparativa = df_merged.groupby('corredor')[["fee_percent", "competitor_fee_percent"]].mean().reset_index() 

# Visualizar a média da taxa da empresa e das concorrentes por corredor
print(analise_comparativa)
# Plotar a comparação de taxas
plt.figure(figsize=(14, 8))
sns.barplot(x="corredor", y="fee_percent", data=analise_comparativa, color='blue', label='Taxa da Empresa')
sns.barplot(x="corredor", y="competitor_fee_percent", data=analise_comparativa, color='orange', alpha=0.6, label='Taxa dos Concorrentes')
plt.title('Comparação de Serviço Média: Empresa vs. Concorrentes')
plt.xlabel('Corredor')
plt.ylabel('Taxa de Serviços Média (%)')
plt.legend
plt.show()


Perguntas e Hipóteses (Visão Estratégica):
Como Cientistas de Dados Sêniores, não paramos na simples constatação. aprofunde a análise para entender o impacto destes preços.
Impacto no Cliente: Nossas taxas mais baixas estão a atrair mais clientes? Queremos ter um desempenho melhor com clientes novos ou recorrentes?
Optimização de Receita: O fato de sermos mais baratos significa que estamos a maximizar a nossa receita? Será que imaginamos aumentar um pouco a taxa em corredores onde a nossa vantagem é maior sem perder clientes?