import os

# IMPORTANT:
# Set the backend BEFORE importing keras
os.environ["KERAS_BACKEND"] = "jax"

import keras
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("dataset.csv")
df.columns = df.columns.str.strip()  # Remove leading/trailing spaces from column names
print("Columns:", df.columns.tolist())

print("\nDataset:")
print(df.head())

print("\nDataset information:")
print(df.info())


# ============================================================
# 2. SEPARATE FEATURES AND TARGET
# ============================================================

X=df.drop("passed", axis=1) # drop the target column from features
y=df["passed"] 


# ============================================================
# 3. SPLIT DATA
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y  # preserve the class distribution(pass/fail ratio) in train and test sets
)


# ============================================================
# 4. SCALE FEATURES
# ============================================================

scaler = StandardScaler() #create an instance of StandardScaler

X_train = scaler.fit_transform(X_train) #learn scaling rules from training data and scale to training data
X_test = scaler.transform(X_test) #use the same scaling rules learned from training data to scale the test data & NOT other scaling rules


# ============================================================
# 5. BUILD DEEP LEARNING MODEL
# ============================================================

model = keras.Sequential([
    keras.layers.Input(shape=(X_train.shape[1],)),  # X_train.shape[1] gives the number of features in the dataset =columns and X_train.shape[0] gives the number of rows in the dataset =rows

    keras.layers.Dense(
        32,
        activation="relu" #reLU activation function is used for hidden layers (recitified linear unit) and sigmoid activation function is used for output layer
    ),  #conceptually, the first layer is the input layer and the last layer is the output layer and all the layers in between are hidden layers
    #conceptually, negative -> 0 & positive values -> stays positive and the output is linear for positive values and the output is 0 for negative values

    keras.layers.Dense(
        16,
        activation="relu" # remove negative values and keep positive values as it is
    ),

    keras.layers.Dense(
        8,
        activation="relu"
    ),

    keras.layers.Dense(
        1,
        activation="sigmoid" #sigmoid activation function is used for output layer that gives output between 0 and 1 and is used for binary classification problems
    )
])


# ============================================================
# 6. COMPILE MODEL
# ============================================================

model.compile(  #Give the model the ability to learn from the data and make predictions
    optimizer="adam", #Adam is an optimization algorithm.
    loss="binary_crossentropy", #binary_crossentropy is used for binary classification problems
    metrics=["accuracy"] #what percentage of correct predictions the model made on the dataset
)


# ============================================================
# 7. DISPLAY MODEL
# ============================================================

print("\nModel Architecture:")
model.summary()


# ============================================================
# 8. TRAIN MODEL
# ============================================================

print("\nTraining model...")

history = model.fit(
    X_train,
    y_train,
    epochs=50, #means the model gets up to 50 iterations through the training data.
    batch_size=16, # in the batch size, the model processes 16 samples at a time before updating the model's weights. This helps in faster convergence and better generalization.
    validation_split=0.2, #means 20% of the training data is used for validation during training. This helps monitor the model's performance on unseen data and prevent overfitting.
    verbose=1  #1 gives a progress display and 0 gives no display
)


# ============================================================
# 9. EVALUATE MODEL
# ============================================================

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("\n================================")
print("MODEL PERFORMANCE")
print("================================")
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")


# ============================================================
# 10. MAKE PREDICTIONS
# ============================================================

probabilities = model.predict(X_test, verbose=0)

predictions = (probabilities >= 0.5).astype(int).flatten() # if probabiliites >50% then convert  into true-> 1 and false->0 and flatten() is used to convert the 2D array into 1D array


# ============================================================
# 11. CLASSIFICATION REPORT
# ============================================================

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=["Fail", "Pass"]
    )
)
# ============================================================
# 12. PREDICT A NEW STUDENT
# ============================================================

# IMPORTANT:
# The values below must follow the SAME feature order
# as dataset.csv.

new_student = np.array([[
    85,     # attendance
    6.5,    # study_hours
    80,     # assignment_score
    75,     # previous_score
    4,      # absences
    70      # participation
]])

new_student_scaled = scaler.transform(new_student)

prediction_probability = model.predict(
    new_student_scaled,
    verbose=0
)[0][0]

print("\n================================")
print("NEW STUDENT PREDICTION")
print("================================")

print(
    f"Pass Probability: "
    f"{prediction_probability * 100:.2f}%"
)

if prediction_probability >= 0.5:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")