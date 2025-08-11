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


# Analisar a média das taxas e o volume de transações por cliente
analise_cliente = df_merged.groupby('ID_cliente').agg(
    transacoes_totais=('ID_transacao', 'count'),
    valor_enviado_total=('valor_enviado', 'sum'),
    taxa_media=('fee_percent', 'mean')
)

print("\n----Análise por tipo de Cliente----")
print(analise_cliente)

# Plotar a média das taxas por cliente
plt.figure(figsize=(12, 6))
# A anotação do cliente recorrente foi ajustada para ser mais clara
sns.barplot(x=analise_cliente.index, y="taxa_media", data=analise_cliente, color='blue')
plt.title('Taxa Média de Serviço por Cliente')
plt.xlabel('Cliente Recorrente')
plt.ylabel('Taxa de Serviços Média (%)')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.show()

# O segundo gráfico foi ajustado para evitar erros de escala.
# Se precisar comparar taxas e volume, considere usar dois eixos Y
plt.figure(figsize=(14, 8))
sns.barplot(x="corredor", y="fee_percent", data=df_merged, color='blue', label='Taxa da Empresa')
sns.barplot(x="corredor", y="competitor_fee_percent", data=df_merged, color='orange', alpha=0.6, label='Taxa dos Concorrentes')
plt.title('Comparação de Taxas por Corredor')
plt.xlabel('Corredor')
plt.ylabel('Taxa de Serviços Média (%)')
plt.legend()
plt.show()