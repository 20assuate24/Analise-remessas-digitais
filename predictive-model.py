import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset unido
df_merged = pd.read_csv('data/processed/merged_data.csv')
df_merged['data'] = pd.to_datetime(df_merged['data'])

# Criar a receita bruta 
# A receita é o valor enviado multiplicado pela nossa taxa (fee_percent)
df_merged['receita_bruta'] = df_merged['valor_enviado'] * df_merged['fee_percent']

# Criar a variável de diferença de preço
# Vamos calcular a diferença de taxa (a nossa taxa menos a do concorrente)
df_merged['diferenca_taxa'] = df_merged['fee_percent'] - df_merged['competitor_fee_percent']

# Agregar os dados para o modelo
# O modelo de regressão precisa de prever o volume de transações por período,
# então vamos agrupar os dados por data e corredor.
df_modelo = df_merged.groupby(['data', 'corredor']).agg(
    volume_transacoes=('ID_transacao', 'count'),
    media_taxa=('fee_percent', 'mean'),
    media_diferenca_taxa=('diferenca_taxa', 'mean'),
    media_taxa_concorrente=('competitor_fee_percent', 'mean'),
    receita_bruta_total=('receita_bruta', 'sum')
).reset_index()

print("\n--- Primeiras linhas do DataFrame para Modelagem ---")
print(df_modelo.head())

