import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
n_samples = 100
data = {
    'Rooms': np.random.randint(1, 6, n_samples),
    'Size': np.random.randint(500, 3500, n_samples),
    'Location_Score': np.random.uniform(1, 10, n_samples),
}
data['Price'] = (data['Rooms'] * 50000) + (data['Size'] * 150) + (data['Location_Score'] * 20000) + np.random.normal(0, 5000, n_samples)

df = pd.DataFrame(data)
df.to_csv('house_data.csv', index=False)
print("Dataset created: house_data.csv")

X = df[['Rooms', 'Size', 'Location_Score']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n--- Model Performance ---")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolors='k', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted House Prices')
plt.savefig('prediction_plot.png')
plt.show()

sample_house = np.array([[3, 1500, 8]]) 
predicted_price = model.predict(sample_house)
print(f"\nPredicted price for a 3-room, 1500sqft house (Loc: 8): ${predicted_price[0]:,.2f}")
