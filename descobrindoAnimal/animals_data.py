import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

import creating_data
run = creating_data

uri = 'dados_comprar.csv'
dados = pd.read_csv(uri)
x = dados[
    ["perninha_curta", "pelo_longo", "faz_auau"]
]
y = dados ["qual_animal"]
SEED = 5

np.random.seed(SEED)
treino_x, teste_x, treino_y, teste_y = train_test_split(
    x, y, test_size=0.25
)

print(f'Treinaremos com {len(treino_x)} e testaremos com {len(teste_x)}')

modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
print(f'A taxa de acerto foi de {acuracia}%')

