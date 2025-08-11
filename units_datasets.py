import pandas as pd

# Carregar os três dataframes
df_transactions = pd.read_csv('data/raw/transactions.csv')
df_customers = pd.read_csv('data/raw/customers.csv')
df_competitors = pd.read_csv('data/raw/competitors.csv')

# --- Passo de correção: Conversão de datas ---
# Converter a coluna 'data' para o tipo datetime em ambos os dataframes
df_transactions['data'] = pd.to_datetime(df_transactions['data'])
df_competitors['data'] = pd.to_datetime(df_competitors['data'])

# Juntar transactions com customers
df_merged = pd.merge(df_transactions, df_customers, on='ID_cliente', how='left')

# Agora, vamos juntar com competitors, usando a data e o corredor
# A junção agora deve funcionar, pois as colunas de data têm o mesmo formato
df_merged = pd.merge(df_merged, df_competitors, on=['data', 'corredor'], how='left')

print("--- DataFrame Final Juntado ---")
print(df_merged.info())
print("\n--- Primeiras linhas ---")
print(df_merged.head())