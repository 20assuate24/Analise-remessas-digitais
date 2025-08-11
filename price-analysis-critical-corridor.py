import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset unido
df_merged = pd.read_csv('data/processed/merged_data.csv')

# --- Passo de pré-processamento: Garantir que a coluna 'data' é do tipo datetime ---
df_merged['data'] = pd.to_datetime(df_merged['data'])

# --- Filtrar o dataframe para o corredor de interesse ---
# O erro "df_merge" foi corrigido para "df_merged"
df_uk_kenya = df_merged[df_merged['corredor'] == 'Reino Unido -> Quénia'].copy()

# Agrupar por data para analisar a evolução
# Calculamos a média das taxas para cada dia
evolucao_precos = df_uk_kenya.groupby('data').agg(
    nossa_taxa=('fee_percent', 'mean'),
    taxa_concorrentes=('competitor_fee_percent', 'mean')
).reset_index()

# Visualizar a evolução da nossa taxa e a dos concorrentes
plt.figure(figsize=(14, 8))
sns.lineplot(x='data', y='nossa_taxa', data=evolucao_precos, label='Nossa Taxa', marker='o')
sns.lineplot(x='data', y='taxa_concorrentes', data=evolucao_precos, label='Taxa dos Concorrentes', marker='o')
plt.title('Evolução das Taxas de Serviço: Reino Unido -> Quénia')
plt.xlabel('Data')
plt.ylabel('Taxa de Serviço Média (%)')
plt.legend()
plt.grid(True)
plt.show()

