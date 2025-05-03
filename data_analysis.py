

# Топ-5 популярных услуг
def top5(merged_data):
    top_services = merged_data["service"].value_counts().head(5)
    print("Топ-5 услуг по количеству заказов:\n", top_services)

# Средняя сумма транзакций по городам:
def avg_trans_by_city(merged_data):
    avg_amount_per_city = merged_data.groupby("city")["amount"].mean().round(2)
    print("Средняя сумма транзакций по городам:\n", avg_amount_per_city)

# Услуга с наибольшей выручкой
def highest_revenue(merged_data):
    revenue_per_service = merged_data.groupby("service")["amount"].sum()
    max_revenue_service = revenue_per_service.idxmax()
    print(f"Услуга с максимальной выручкой: {max_revenue_service}")