import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações para melhorar a visualização dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Carregar os dados
df_transactions = pd.read_csv('data/raw/transactions.csv')

# Visualizar as 5 primeiras linhas para ter uma ideia da estrutura
print("--- Primeiras 5 linhas ---")
print(df_transactions.head())

# Obter informações sobre o DataFrame (tipos de dados, valores nulos)
print("\n--- Informações do DataFrame ---")
print(df_transactions.info())

# Obter estatísticas descritivas básicas das colunas numéricas
print("\n--- Estatísticas Descritivas ---")
print(df_transactions.describe())