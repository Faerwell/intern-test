from data_cleanup import transaction_processing, customer_processing, data_merging
from data_analysis import top5, avg_trans_by_city, highest_revenue


def run():
    transactions = transaction_processing()
    clients = customer_processing()
    merged_data = data_merging(transactions, clients)

    # Топ-5 популярных услуг
    top5(merged_data)

    # Средняя сумма транзакций по городам
    avg_trans_by_city(merged_data)

    # Услуга с наибольшей выручкой
    highest_revenue(merged_data)










if __name__ == "__main__":
    run()