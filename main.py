from data_cleanup import transaction_processing, customer_processing, data_merging
from data_analysis import (top5, avg_trans_by_city, highest_revenue, percen_trans_payment, revenue_last_month,
                           revenue_customer_category)


def run():

    # Подготовка и очистка данных
    transactions = transaction_processing()
    clients = customer_processing()
    # Объединение данных
    merged_data = data_merging(transactions, clients)

    # Топ-5 популярных услуг
    top5(merged_data)

    # Средняя сумма транзакций по городам
    avg_trans_by_city(merged_data)

    # Услуга с наибольшей выручкой
    highest_revenue(merged_data)

    # Процент транзакций по способам оплаты
    percen_trans_payment(merged_data)

    # Выручка за последний месяц
    revenue_last_month(merged_data)

    # Задание 3: Выручка по категориям клиентов
    revenue_customer_category(merged_data)







if __name__ == "__main__":
    run()