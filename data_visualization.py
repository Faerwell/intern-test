'''
Визуализация данных.
Построить распределение сумм транзакций.
Создать диаграмму выручки по услугам.
Построить график зависимости средней суммы транзакции от возраста клиентов.
'''

import matplotlib.pyplot as plt


# Распределение сумм транзакций
def distr_of_trans_amounts(merged_data):
    plt.hist(merged_data["amount"], bins=30, edgecolor="black")
    plt.title("Распределение сумм транзакций")
    plt.xlabel("Сумма")
    plt.ylabel("Частота")
    plt.show()

# Выручка по услугам
def revenue_per_services(merged_data):
    # Группировка данных по услугам
    revenue_per_service = merged_data.groupby("service")["amount"].sum().sort_values(ascending=False)

    # Создание графика
    plt.figure(figsize=(12, 6))
    revenue_per_service.plot(kind="bar", color="skyblue")

    # Настройка подписей услуг
    plt.xticks(
        ticks=range(len(revenue_per_service)),  # Позиции на оси X
        labels=revenue_per_service.index.tolist(),  # Названия услуг из индекса
        rotation=45,  # Поворот подписей
        ha="right"  # Выравнивание по правому краю
    )

    plt.title("Выручка по услугам")
    plt.xlabel("Услуга")
    plt.ylabel("Сумма выручки")
    plt.tight_layout()
    plt.show()

# Зависимость суммы транзакции от возраста
def trans_amount_dependence_on_age(merged_data):
    merged_data.groupby("age")["amount"].mean().plot(
        kind="line", title="Средняя сумма транзакции по возрасту"
    )
    plt.xlabel("Возраст")
    plt.ylabel("Средняя сумма")
    plt.show()