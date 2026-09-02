import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score )
from house_prices import data
df = pd.DataFrame(data)
# 2. Understand Data
print(df.head(5))
print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)
# 3. Check/Clean Data
print("\nMissing values:")
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()
# 4. EDA
plt.scatter(df['Size'], df['Price'])
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('House Prices vs Size')
plt.show()
# 5. Select Features and Target
X = df[["Size", "Bedrooms", "Age"]]
y = df["Price"]
# 6. Train/Test Split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# 7. Create Linear Regression Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# 8. Train Model
model.fit(X_train, y_train)
# 9. Inspect Model   │ What did it learn?   │          
print("Intercept:", model.intercept_)
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", coefficient)
# 10. Make Predictions | Get answers | Make me a cookie.
y_pred = model.predict(X_test)
# 11. Evaluate Model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("\nModel Evaluation")
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)
print("R2  :", r2)
# 12. Compare Actual vs Predicted
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})
print("\nActual vs Predicted:")
print(results)
# 13. Save Model
import joblib
joblib.dump(model, "house_price_model.pkl")
print("\nModel saved successfully!")