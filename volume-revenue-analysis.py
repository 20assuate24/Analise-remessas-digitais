import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset unido
df_merged = pd.read_csv('data/processed/merged_data.csv')

# --- Passo de correção: Calcular a receita bruta ---
# A receita é o valor enviado multiplicado pela nossa taxa (fee_percent)
df_merged['receita_bruta'] = df_merged['valor_enviado'] * df_merged['fee_percent']

# Analisar receita e volume por corredor
analise_corredor_completa = df_merged.groupby('corredor').agg(
    volume_transacoes=('ID_transacao', 'count'),
    receita_total=('receita_bruta', 'sum'),
    taxa_media=('fee_percent', 'mean')
).reset_index()

print("\n--- Análise Completa por Corredor (Receita Bruta) ---")
print(analise_corredor_completa)

# Visualizar a receita total e o volume de transações
fig, ax1 = plt.subplots(figsize=(14, 8))

# Gráfico de barras para volume de transações
sns.barplot(x='corredor', y='volume_transacoes', data=analise_corredor_completa, ax=ax1, color='lightskyblue', label='Volume de Transações')
ax1.set_title('Volume de Transações e Receita Bruta por Corredor')
ax1.set_ylabel('Volume de Transações', color='lightskyblue')
ax1.tick_params(axis='y', labelcolor='lightskyblue')
ax1.legend(loc='upper left')

# Gráfico de linha para receita total
ax2 = ax1.twinx()
sns.lineplot(x='corredor', y='receita_total', data=analise_corredor_completa, ax=ax2, color='darkorange', marker='o', label='Receita Bruta')
ax2.set_ylabel('Receita Bruta', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')
ax2.legend(loc='upper right')

plt.show()
