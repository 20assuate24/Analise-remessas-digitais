import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Definir as datas e os corredores
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 1)
corredores = ['EUA -> Brasil', 'Reino Unido -> Quénia', 'Portugal -> Moçambique']

# Simular 365 dias de dados
competitor_data = []

current_date = start_date
while current_date < end_date:
    for corredor in corredores:
        # Simular a taxa média do concorrente
        competitor_fee = 0
        if corredor == 'EUA -> Brasil':
            competitor_fee = round(random.uniform(0.018, 0.038), 4)
        elif corredor == 'Reino Unido -> Quénia':
            competitor_fee = round(random.uniform(0.012, 0.022), 4)
        elif corredor == 'Portugal -> Moçambique':
            competitor_fee = round(random.uniform(0.027, 0.047), 4)

        competitor_data.append({
            'data': current_date.strftime('%Y-%m-%d'),
            'corredor': corredor,
            'competitor_fee_percent': competitor_fee
        })
    current_date += timedelta(days=1)

# Criar o DataFrame e salvar em CSV
df_competitors = pd.DataFrame(competitor_data)
df_competitors.to_csv('data/raw/competitors.csv', index=False)

print("Arquivo competitors.csv criado com sucesso!")