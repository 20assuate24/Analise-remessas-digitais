import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Definir as datas e os corredores
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 1)
corredores = ['EUA -> Brasil', 'Reino Unido -> Quénia', 'Portugal -> Moçambique']

# Simular 10.000 transações
num_transactions = 10000
transactions = []

for i in range(num_transactions):
    # Gerar data e hora aleatórias
    data_transacao = start_date + timedelta(days=random.randint(0, 364), hours=random.randint(0, 23))

    # Escolher um corredor aleatório
    corredor_escolhido = random.choice(corredores)

    # Simular o valor enviado (em USD, GBP ou EUR)
    valor_enviado = round(random.uniform(50, 1000), 2)

    # Simular a taxa de câmbio (valores fictícios, mas realistas)
    taxa_de_cambio = 0
    if corredor_escolhido == 'EUA -> Brasil':
        taxa_de_cambio = round(random.uniform(5.0, 5.5), 4)
    elif corredor_escolhido == 'Reino Unido -> Quénia':
        taxa_de_cambio = round(random.uniform(150.0, 160.0), 4)
    elif corredor_escolhido == 'Portugal -> Moçambique':
        taxa_de_cambio = round(random.uniform(65.0, 70.0), 4)

    # Simular a percentagem da taxa de serviço (fee_percent)
    # A percentagem pode ser diferente por corredor
    fee_percent = 0
    if corredor_escolhido == 'EUA -> Brasil':
        fee_percent = round(random.uniform(0.015, 0.035), 4) # Exemplo: 1.5% a 3.5%
    elif corredor_escolhido == 'Reino Unido -> Quénia':
        fee_percent = round(random.uniform(0.01, 0.02), 4) # Exemplo: 1% a 2%
    elif corredor_escolhido == 'Portugal -> Moçambique':
        fee_percent = round(random.uniform(0.025, 0.045), 4) # Exemplo: 2.5% a 4.5%

    transactions.append({
        'ID_transacao': i + 1,
        'data': data_transacao,
        'corredor': corredor_escolhido,
        'valor_enviado': valor_enviado,
        'taxa_de_cambio': taxa_de_cambio,
        'fee_percent': fee_percent
    })

# Criar o DataFrame e salvar em CSV
df_transactions = pd.DataFrame(transactions)
df_transactions.to_csv('transactions.csv', index=False)

print("Arquivo transactions.csv criado com sucesso!")


