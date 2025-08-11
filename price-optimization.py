import pandas as pd
import numpy as np
from scipy import stats

# Carregar o dataset unido
df_merged = pd.read_csv('data/processed/merged_data.csv')

# --- Passo 1: Filtrar os dados para o corredor e clientes novos ---
# Vamos assumir que a primeira transação de cada ID_cliente o classifica como 'novo'.
# Para simplificar, vamos filtrar o corredor de maior receita
df_ab_test = df_merged[df_merged['corredor'] == 'Portugal -> Moçambique'].copy()

# --- Passo 2: Simular os grupos de controle e teste ---
# Dividir aleatoriamente os clientes em dois grupos
np.random.seed(42) # para garantir a reprodutibilidade
clientes_unicos = df_ab_test['ID_cliente'].unique()
grupo_teste = np.random.choice(clientes_unicos, size=int(len(clientes_unicos) * 0.5), replace=False)

df_controle = df_ab_test[~df_ab_test['ID_cliente'].isin(grupo_teste)].copy()
df_teste = df_ab_test[df_ab_test['ID_cliente'].isin(grupo_teste)].copy()

# --- Passo 3: Aplicar a mudança de preço ao Grupo de Teste ---
# Simular uma redução de 1% na taxa para o Grupo de Teste
df_teste['fee_percent_ajustada'] = df_teste['fee_percent'] - 0.01

# --- Passo 4: Calcular e comparar as métricas ---
volume_controle = df_controle['ID_transacao'].count()
volume_teste = df_teste['ID_transacao'].count()

receita_controle = (df_controle['valor_enviado'] * df_controle['fee_percent']).sum()
receita_teste = (df_teste['valor_enviado'] * df_teste['fee_percent_ajustada']).sum()

print("\n--- Análise da Simulação de Experimento A/B ---")
print(f"Volume de Transações - Grupo de Controle: {volume_controle}")
print(f"Volume de Transações - Grupo de Teste: {volume_teste}")
print(f"Receita Bruta Total - Grupo de Controle: {receita_controle:.2f}")
print(f"Receita Bruta Total - Grupo de Teste: {receita_teste:.2f}")

# --- Passo 5: Teste Estatístico (t-test) ---
# Vamos simular os resultados diários para ter uma amostra para o teste t
df_controle_diario = df_controle.groupby('data')['ID_transacao'].count()
df_teste_diario = df_teste.groupby('data')['ID_transacao'].count()

# O teste t compara as médias dos dois grupos
t_stat, p_value = stats.ttest_ind(df_controle_diario, df_teste_diario, equal_var=False)

print("\n--- Teste de Significância Estatística (t-test) ---")
print(f"Estatística t: {t_stat:.2f}")
print(f"Valor p: {p_value:.4f}")

