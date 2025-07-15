import pandas as pd
from sklearn.linear_model import LinearRegression
from joblib import dump

# Sample dataset
data = {
    "area": [1000, 1500, 1800, 2400, 3000],
    "bedrooms": [2, 3, 3, 4, 5],
    "age": [10, 5, 2, 7, 1],
    "price": [150000, 200000, 230000, 300000, 400000]
}

df = pd.DataFrame(data)
X = df[["area", "bedrooms", "age"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

dump(model, "house_price_model.pkl")
print("✅ Model trained and saved as house_price_model.pkl")
