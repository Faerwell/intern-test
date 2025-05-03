import pandas as pd


def transaction_processing():
    # Загрузка данных
    transactions = pd.read_excel("transactions_data.xlsx")

    # Удаление дубликатов
    transactions = transactions.drop_duplicates(subset="transaction_id")

    # Удаление строк с пропусками в ключевых полях
    transactions = transactions.dropna(subset=["client_id", "amount", "transaction_date"])

    # Нормализация дат
    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"],
        errors="coerce"
    )
    transactions = transactions.dropna(subset=["transaction_date"])

    # Удаление отрицательных сумм
    transactions = transactions[transactions["amount"] >= 0]
    # Удаление выбросов (метод IQR)
    Q1 = transactions["amount"].quantile(0.25)
    Q3 = transactions["amount"].quantile(0.75)
    IQR = Q3 - Q1
    transactions = transactions[
        ~((transactions["amount"] > Q3 + 1.5 * IQR) |
          (transactions["amount"] < Q1 - 1.5 * IQR))
    ]

    # Нормализация категориальных данных
    transactions["payment_method"] = (
        transactions["payment_method"]
        .str.lower()
        .replace({"кредитная карта": "credit_card", "банковский перевод": "bank_transfer"})
    )
    transactions["city"] = transactions["city"].str.title()

    return transactions

def customer_processing():
    clients = pd.read_json("clients_data.json", orient="records")

    # Валидация возраста
    clients = clients[(clients["age"] >= 18) & (clients["age"] <= 100)]

    # Нормализация пола
    clients["gender"] = (
        clients["gender"]
        .str.upper()
        .replace({"M": "Male", "F": "Female", "М": "Male", "Ж": "Female"})
        .fillna("Unknown")
    )

    # Заполнение пропусков в стоимости активов
    clients["net_worth"] = clients["net_worth"].fillna(0).clip(lower=0)

    return clients

def data_merging(transactions, clients):
    #print("Столбцы в transactions:", transactions.columns.tolist())
    #print("Столбцы в clients:", clients.columns.tolist())

    # Переименование столбца в clients
    clients = clients.rename(columns={"id": "client_id"})

    # Удаление пустых client_id
    transactions = transactions[transactions["client_id"] != ""]

    # Приведение типов
    transactions["client_id"] = transactions["client_id"].astype(str)
    clients["client_id"] = clients["client_id"].astype(str)

    # Объединение
    merged_data = pd.merge(transactions, clients, on="client_id", how="inner")

    return merged_data