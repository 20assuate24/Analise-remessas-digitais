import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset unido
df_merged = pd.read_csv('data/processed/merged_data.csv')

# --- Análise por tipo de cliente: Recorrente vs. Não-Recorrente ---
analise_cliente_tipo = df_merged.groupby('cliente_recorrente').agg(
    transacoes_totais=('ID_transacao', 'count'),
    valor_enviado_total=('valor_enviado', 'sum'),
    taxa_media=('fee_percent', 'mean')
).reset_index()

print("\n--- Análise por Tipo de Cliente ---")
print(analise_cliente_tipo)

# Visualizar a taxa média para clientes recorrentes vs. novos
plt.figure(figsize=(10, 6))
sns.barplot(x='cliente_recorrente', y='taxa_media', data=analise_cliente_tipo)
plt.title('Taxa Média de Serviço por Tipo de Cliente')
plt.xlabel('Cliente Recorrente')
plt.ylabel('Taxa Média de Serviço (%)')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.show()

