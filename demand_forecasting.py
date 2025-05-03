'''
Прогнозирование спроса на следующий месяц (например, с использованием линейной регрессии).
'''
from sklearn.linear_model import LinearRegression

def demand_forecasting(merged_data):
    # Подготовка данных
    monthly_revenue = merged_data.resample("ME", on="transaction_date")["amount"].sum().reset_index()
    monthly_revenue["month_num"] = range(1, len(monthly_revenue) + 1)  # Нумерация месяцев

    # Обучение модели
    X = monthly_revenue[["month_num"]]  # Признак
    y = monthly_revenue["amount"]  # Целевая переменная

    model = LinearRegression()
    model.fit(X, y)

    # Прогноз на следующий месяц
    next_month = monthly_revenue["month_num"].max() + 1
    predicted_revenue = model.predict([[next_month]])
    print(f"Прогноз выручки на следующий месяц: {predicted_revenue[0]:,.2f}")