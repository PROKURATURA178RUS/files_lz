import pandas as pd
import matplotlib.pyplot as plt

file_path = 'titanic.parquet'


df = pd.read_parquet(file_path)# чтение файла


print(df.head())# выводим первые строки набора данных, чтобы увидеть его структуру


csv_output_path = 'titanic.csv'# сохранение данных в формате csv
df.to_csv(csv_output_path, index=False, encoding='utf-8')
print(f'Файл сохранен как: {csv_output_path}')

csv_file_path = 'titanic.csv'


df = pd.read_csv(csv_file_path)# чтение данных из файла csv


survival_counts = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)# группируем данные по классу билета и считаем количество выживших и не выживших


survival_percentage = survival_counts.div(survival_counts.sum(axis=1), axis=0) * 100# вычисляем проценты выживания для каждого класса


survival_percentage.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'],# создаем гистограмму
                     figsize=(10, 6))


plt.title('Выживаемость пассажиров Титаника')# настраиваем заголовок и метки
plt.xlabel('Класс билета')
plt.xticks(rotation=0)
plt.legend(['Не выжили', 'Выжили'])


plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.0f}%'))# настройка оси Y на проценты
plt.ylim(0, 100)


plt.tight_layout()# отображаем гистограмму
plt.show()