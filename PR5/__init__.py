import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Чтение данных из CSV файла
features = pd.read_csv('data1.csv',nrows=50, usecols=['ENERGY STAR Score', 'Site EUI (kBtu/ft²)',
                      'Weather Normalized Source EUI (kBtu/ft²)',
                      'Total GHG Emissions (Metric Tons CO2e)'])

plot_data = features
# Замена inf на NaN
plot_data = plot_data.replace({'Not Available': np.nan})
plot_data = plot_data.replace({np.inf: np.nan, -np.inf: np.nan})

for col in list(plot_data.columns):
 # Выбираем столбцы, которые должны быть числовыми
    if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in col or 'therms' in col or 'gal' in col or 'Score' in col):
        plot_data[col] = plot_data[col].astype(float)
#plot_data = plot_data.dropna()


plt.figure(figsize=(25, 20))
#for col in list(features.columns):
#    if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in col or 'therms' in col or 'gal' in col or 'Score' in col):
#        features[col] = features[col].astype(float)



# Переименование столбцов для удобства
plot_data = plot_data.rename(columns={'Site EUI (kBtu/ft²)': 'Site EUI',
                                      'Weather Normalized Source EUI (kBtu/ft²)': 'Weather Norm EUI',
                                      'Total GHG Emissions (Metric Tons CO2e)': 'Total GHG Emissions'})

# Удаление строк с пропущенными значениями
plot_data = plot_data.dropna()

# Функция для расчета коэффициента корреляции и его добавления на график
def corr_func(x, y, **kwargs):
    r = np.corrcoef(x, y)[0][1]
    ax = plt.gca()
    ax.annotate("r = {:.2f}".format(r),
                xy=(.2, .8), xycoords=ax.transAxes,
                size=12)

# Создание объекта PairGrid
grid = sns.PairGrid(data=plot_data, height=3)

# Верхняя часть - scatter plots
grid.map_upper(plt.scatter, color='red', alpha=0.6)

# Диагональ - гистограммы
grid.map_diag(plt.hist, color='red', edgecolor='black')

# Нижняя часть - kernel density plots и корреляция

grid.map_lower(sns.histplot, stat="density", binwidth=0.1)
grid.map_lower(corr_func)

# Заголовок для всего графика
plt.suptitle('Pairs Plot of Energy Data', size=16, y=1.02)


# Показать график
plt.show()