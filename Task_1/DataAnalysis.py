import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = {
    'Category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Home', 'Clothing', 'Electronics'],
    'Sales': [1200, 800, 500, 1500, 700, 600, 1100],
    'Profit': [300, 150, 50, 400, 80, 120, 280],
    'Units': [10, 25, 15, 12, 20, 18, 9]
}
df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)

print("--- Basic Data Analysis ---")
avg_sales = df['Sales'].mean()
print(f"Average Sales: ${avg_sales:.2f}")

plt.style.use('ggplot')

plt.figure(figsize=(8, 5))
df.groupby('Category')['Sales'].sum().plot(kind='bar', color='teal')
plt.title('Total Sales per Category')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('bar_chart.png') 
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['Sales'], df['Profit'], color='darkorange', s=100)
plt.title('Sales vs Profit Correlation')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.grid(True)
plt.savefig('scatter_plot.png')
plt.show()

plt.figure(figsize=(6, 4))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='YlGnBu')
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.show()

print("\nTask 1 Completed: Visuals saved and analysis printed.")
