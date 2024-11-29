from collections import Counter # импорт библиотек
import string
import docx
import pandas as pd
import matplotlib.pyplot as plt



file_path = 'lion.docx'   # путь к файлу


doc = docx.Document(file_path)  # извлечение текста из файла docx
full_text = []
for para in doc.paragraphs:
    full_text.append(para.text)
text = ' '.join(full_text)


translator = str.maketrans('', '', string.punctuation)   # удаление знаков препинания и перевод текста в нижний регистр
text = text.translate(translator).lower()


words = text.split()      # встречаемость русских слов
word_count = Counter(words)


total_words = sum(word_count.values())# общая суммы всех слов


word_frequency = {word: (count / total_words) * 100 for word, count in word_count.items()}# подсчет частоты встречаемости слов в процентах


word_list = [(word, count, word_frequency[word]) for word, count in word_count.items()] # сохранение статистики по словам в Excel
df = pd.DataFrame(word_list, columns=['Слово', 'Количество', 'Частота (%)'])
df.to_excel('word_frequency_statistics.xlsx', index=False)


letters = [char for char in text if char.isalpha() and char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']# подсчет встречаемости русских букв
letter_count = Counter(letters)

df_letters = pd.DataFrame(letter_count.items(), columns=['Буква', 'Частота'])
plt.figure(figsize=(10, 6))
plt.bar(df_letters['Буква'], df_letters['Частота'], color='orange')
plt.title('Частота встречаемости букв')
plt.xlabel('Буквы')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


print("Статистика по русским буквам:")# вывод статистики по русским буквам
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
