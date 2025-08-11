import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# --- Passo 1: Preparação dos dados ---
# Carregar o dataset unido
df_merged = pd.read_csv('data/processed/merged_data.csv')
df_merged['data'] = pd.to_datetime(df_merged['data'])

# Criar a receita bruta
df_merged['receita_bruta'] = df_merged['valor_enviado'] * df_merged['fee_percent']

# Criar a variável de diferença de preço
df_merged['diferenca_taxa'] = df_merged['fee_percent'] - df_merged['competitor_fee_percent']

# Agregar os dados para o modelo
df_modelo = df_merged.groupby(['data', 'corredor']).agg(
    volume_transacoes=('ID_transacao', 'count'),
    media_taxa=('fee_percent', 'mean'),
    media_diferenca_taxa=('diferenca_taxa', 'mean'),
    media_taxa_concorrente=('competitor_fee_percent', 'mean'),
    receita_bruta_total=('receita_bruta', 'sum')
).reset_index()

# --- Passo 2: Treino do Modelo ---
# Separar os dados em variáveis de entrada (X) e saída (y)
features = ['media_taxa', 'media_diferenca_taxa', 'media_taxa_concorrente']
target = 'volume_transacoes'

X = df_modelo[features]
y = df_modelo[target]

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de Regressão
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões e avaliar o modelo
y_pred = modelo.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Avaliação do Modelo ---")
print(f"Erro Quadrático Médio (MSE): {mse:.2f}")
print(f"R-quadrado (R²): {r2:.2f}")

# --- SIMULAÇÃO: Otimização de Preços no Corredor Crítico ---

# Identificar as features para o corredor Reino Unido -> Quénia
df_uk_kenya_sim = df_modelo[df_modelo['corredor'] == 'Reino Unido -> Quénia'].copy()

# Valor da nossa taxa atual neste corredor (a média)
media_taxa_atual = df_uk_kenya_sim['media_taxa'].mean()

# Simular um aumento de 0.5% (0.005 em forma decimal)
media_taxa_simulada = media_taxa_atual + 0.005

# Criar um DataFrame de teste com os novos valores
# Usamos a média da diferença e da taxa do concorrente para manter o cenário estável
cenario_simulacao = pd.DataFrame([{
    'media_taxa': media_taxa_simulada,
    'media_diferenca_taxa': df_uk_kenya_sim['media_diferenca_taxa'].mean(),
    'media_taxa_concorrente': df_uk_kenya_sim['media_taxa_concorrente'].mean()
}])

# Prever o novo volume de transações com a nova taxa
volume_previsto = modelo.predict(cenario_simulacao)[0]

# Calcular a receita bruta total prevista (novo volume * nova taxa * valor médio da transação)
valor_medio_transacao = df_merged[df_merged['corredor'] == 'Reino Unido -> Quénia']['valor_enviado'].mean()
receita_prevista = volume_previsto * media_taxa_simulada * valor_medio_transacao

print("\n--- Simulação de Otimização de Preços ---")
print(f"Taxa Média Atual (Reino Unido -> Quénia): {media_taxa_atual:.4f}")
print(f"Taxa Média Simulada (Aumento de 0.5%): {media_taxa_simulada:.4f}")
print(f"Volume de Transações Previsto: {volume_previsto:.2f}")
print(f"Receita Bruta Prevista: {receita_prevista:.2f}")