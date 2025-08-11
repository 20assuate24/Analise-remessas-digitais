import pandas as pd
import numpy as np
import os

#Carregar os tres dataframes
df_transactions = pd.read_csv('data/raw/transactions.csv')
df_customers = pd.read_csv('data/raw/customers.csv')
df_competitors = pd.read_csv('data/raw/competitors.csv') 

# Corrigir o formato das  datas para a junção
df_transactions['data'] = pd.to_datetime(df_transactions['data'])
df_competitors['data'] = pd.to_datetime(df_competitors['data']) 

# Juntar os dataframes
df_merged = pd.merge(df_transactions, df_customers, on='ID_cliente', how='left')
df_merged = pd.merge(df_merged, df_competitors, on=['data', 'corredor'], how='left')

# Verificar se o diretório 'data/processed' existe, caso contrário, criar
if not os.path.exists(output_dir := 'data/processed'):
    os.makedirs('data/processed')
    print(f"Diretório {output_dir} criado com sucesso!")

# Salvar o dataframe final em CSV
df_merged.to_csv(os.path.join(output_dir, 'merged_data.csv'), index=False)  

print("Arquivo merged_data.csv criado com sucesso na pasta processed!")  

# Visualização do Resultado de união
print("----Dataframe Final Juntado----")
print(df_merged.info())
print("----Primeiras linhas do Dataframe Final----")
print(df_merged.head())
print("----Ultimas linhas do Dataframe Final----")    
print(df_merged.tail())
print("----Colunas do Dataframe Final----") 
print(df_merged.columns.tolist())
