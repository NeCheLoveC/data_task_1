import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def missing_values_table(data, threshold=50):
    mis_val = data.isnull().sum()
    mis_val_percent = 100 * data.isnull().sum() / len(data)

    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Пустые значения', 1: '% от общего количества'})
    print(mis_val_table_ren_columns)

    #mis_val_table_ren_columns = mis_val_table_ren_columns[
    #    mis_val_table_ren_columns.iloc[:, 1] > 1].sort_values(
    #   '% от общего количества', ascending=False).round(1)
    #print(mis_val_table_ren_columns)
    mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:, 1] > 50].sort_values(by="% от общего количества", ascending=False)
    columns_to_drop = mis_val_table_ren_columns.index
    print(columns_to_drop)
    print(mis_val_table_ren_columns)
    # Удаляем выбранные столбцы из DataFrame
    print("Было : " + data.columns.size.__str__())
    data_cleaned = data.drop(columns=columns_to_drop)
    print("Стало : " + data_cleaned.columns.size.__str__())
    print(f"\nУдалены столбцы с пропущенными значениями более {threshold}%.")
    return data_cleaned


data = pd.read_csv('data1.csv')

data = data.replace({'Not Available': np.nan})
for col in list(data.columns):
 # Выбираем столбцы, которые должны быть числовыми
    if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in col or 'therms' in col or 'gal' in col or 'Score' in col):
        data[col] = data[col].astype(float)

data = missing_values_table(data, threshold=50)

# Гистограмма
plt.figure(figsize=(25,15))
plt.style.use('fivethirtyeight')
plt.hist(data['ENERGY STAR Score'].dropna(), bins = 100, edgecolor = 'k');
plt.xlabel('Score');
plt.ylabel('Number of Buildings');
plt.title('Energy Star Score Distribution');

plt.show()




types = data.dropna(subset=['ENERGY STAR Score'])
types = types['Largest Property Use Type'].value_counts()
types = list(types[types.values > 100].index)

# График распределения по категориям зданий
#sns.figsize(12, 10)

# График для каждого здания
plt.figure(figsize=(22,15))
for b_type in types:
    # Select the building type
    subset = data[data['Largest Property Use Type'] == b_type]
    # Density plot енргопотребления
    print(subset.head())
    subset = subset['ENERGY STAR Score'].dropna()
    ax = sns.kdeplot(subset, fill = False, alpha = 0.8)

    # Получаем легенду и добавляем ее




plt.xlabel('Energy Star Score', size = 20); plt.ylabel('Density', size = 20);
plt.title('Density Plot of Energy Star Scores by Building Type', size = 28);
plt.legend(types)
plt.show()


plt.figure(figsize=(55, 15))
data = data.select_dtypes(include=['float64', 'int64'])
data = data.corr()["ENERGY STAR Score"].sort_values()
data = pd.DataFrame(data)
sns.heatmap(data, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Матрица корреляции', size=16)
plt.show()
