from data_cleanup import transaction_processing, customer_processing, data_merging


def run():
    transactions = transaction_processing()
    clients = customer_processing()
    merged_data = data_merging(transactions, clients)











if __name__ == "__main__":
    run()