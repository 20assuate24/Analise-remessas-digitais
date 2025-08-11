import pandas as pd
import numpy as np

# Simular 2000 clientes únicos
num_customers = 3000

# Criar IDs de clientes únicos
customer_ids = [f'C{i+1}' for i in range(num_customers)]

# Criar o dataframe de clientes
df_customers = pd.DataFrame({'ID_cliente': customer_ids})

# Simular se o cliente é novo ou recorrente
# Vamos supor que 70% dos clientes são recorrentes e 30% são novos
df_customers['cliente_recorrente'] = np.random.choice([True, False], size=num_customers, p=[0.7, 0.3])

# Salvar o dataframe de clientes em CSV
df_customers.to_csv('data/raw/customers.csv', index=False)

print("Arquivo customers.csv criado com sucesso!")

# --- Ação Adicional para o projeto: ---
# Agora, vamos atribuir esses clientes às transações que já criamos
# Isso nos permitirá fazer a análise de clientes na Fase 2

# Carregar o arquivo transactions.csv que já criamos
df_transactions = pd.read_csv('data/raw/transactions.csv')

# Atribuir IDs de cliente aleatoriamente às transações
# Alguns clientes farão mais de uma transação, o que é realista
df_transactions['ID_cliente'] = np.random.choice(customer_ids, size=len(df_transactions), replace=True)

# Salvar o novo dataframe de transações com o ID do cliente
df_transactions.to_csv('data/raw/transactions.csv', index=False)

print("O arquivo transactions.csv foi atualizado com os IDs dos clientes!")
