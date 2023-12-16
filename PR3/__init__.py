import pandas as pd
from pprint import pprint

def get_stat():
    # Чтение CSV-файла в DataFrame
    df = pd.read_csv("iris.csv")

    # Считаем статистики для каждого столбца
    stat_map = {
            'sepalLength': {
            'Среднее значение': df['sepalLength'].mean(),
            'Медиана': df['sepalLength'].median(),
            'Мода': (', '.join(map(str, df['sepalLength'].mode()))),
            'Размах': df['sepalLength'].max() - df['sepalLength'].min(),
            'Стандартное отклонение': df['sepalLength'].std(),
            'Дисперсия': df['sepalLength'].var()
        },
        'sepalWidth': {
            'Среднее значение': df['sepalWidth'].mean(),
            'Медиана': df['sepalWidth'].median(),
            'Мода': (', '.join(map(str, df['sepalWidth'].mode()))),
            'Размах': df['sepalWidth'].max() - df['sepalWidth'].min(),
            'Стандартное отклонение': df['sepalWidth'].std(),
            'Дисперсия': df['sepalWidth'].var()
        },
        'petalLength': {
            'Среднее значение': df['petalLength'].mean(),
            'Медиана': df['petalLength'].median(),
            'Мода': (', '.join(map(str, df['petalLength'].mode()))),
            'Размах': df['petalLength'].max() - df['petalLength'].min(),
            'Стандартное отклонение': df['petalLength'].std(),
            'Дисперсия': df['petalLength'].var()
        },
        'petalWidth': {
            'Среднее значение': df['petalWidth'].mean(),
            'Медиана': df['petalWidth'].median(),
            'Мода': (', '.join(map(str, df['petalWidth'].mode()))),
            'Размах': df['petalWidth'].max() - df['petalWidth'].min(),
            'Стандартное отклонение': df['petalWidth'].std(),
            'Дисперсия': df['petalWidth'].var()
        },
        'variety': {
            'Мода': df['variety'].mode().iloc[0],
        }
    }

    return stat_map

pprint(get_stat())
