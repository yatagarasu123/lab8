### Лабораторна робота: Робота з JSON у Python

## Мета роботи:
### Мета лабораторної роботи: Ознайомлення з різними способами роботи з JSON файлами у Python.
### Очікуваний результат: Набуття практичних навичок виконання завдань, пов'язаних з обробкою JSON даних.

## Опис завдання:
### В цій лабораторній роботі потрібно було виконати декілька завдань, в кожному з яких потрібно написати функцію для розв'язання різноманітних задач, пов'язаних з обробкою JSON файлів. Наприклад: парсинг JSON файлів, перетворення даних, валідація JSON схеми, робота з вкладеними JSON структурами, оновлення даних у JSON файлах тощо.

## Виконання роботи:
### Структура проекту:
#### Код розділений на різні функції, кожна функція відповідає за окреме завдання з відповідною назвою, наприклад: task1, task2, task3 тощо.
### Опис файлів:
#### main.py: містить код Python з функціями для вирішення необхідних завдань.
#### README.md: описує структуру проекту, призначення кожного файлу, основні функції та методи з поясненням їх роботи.

## Опис основних функцій та методів з поясненням їх роботи
```python
#task 1
def task1(file_path, age):
    with open(file_path, 'r') as file:
        data = json.load(file)
    names_above = [entry['name'] for entry in data if entry['age'] > age]
    return names_above
#Приклад використання
result = task1("data.json", 30)
print(result)

#task 2
def task2(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)
# Приклад використання
with open("output.json", 'r') as file:
    output_data = json.load(file)
    print(output_data)
```


## Результати:
### Кожен рядок відповідає за виведення відповідної функції, тобто: 1 рядок - task1, 2 рядок - task2 і так далі.
![example_output](![![image](https://github.com/yatagarasu123/lab8/assets/145234911/6aef15b6-70e1-4b10-ba50-8d96a36254cc)
]()
)

## Висновки:
### Мета роботи була досягнута: були розглянуті та реалізовані різні методи обробки JSON даних у Python. Також вийшло розібратися та почати розумітися в цій темі.

## Інструкції з запуску:
### Потрібно відкрити файл `main.py` будь-яким зручним вам способом, головне щоб був встановлений та працював інтерпретатор Python. Додати необхідні JSON файли, які використовуються у прикладах. Після виконання цих дій можна запустити скрипт, і він виведе необхідні результати.
