import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_spending(transactions):
    amounts = [t.get("amount", 0) for t in transactions]

    # Safety check
    if len(amounts) < 2:
        return 0.0

    X = np.arange(len(amounts)).reshape(-1, 1)
    y = np.array(amounts)

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict([[len(amounts)]])[0]

    return round(float(prediction), 2)