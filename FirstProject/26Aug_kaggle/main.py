import kagglehub
import tensorflow as tf
from tensorflow.keras import layers, models

print("Kaggle authentication:")
print(kagglehub.whoami())

print("\nTesting public dataset download...")

#path = kagglehub.dataset_download("yashdogra/cats-and-dogs")
path = r"C:\Users\RajDaily\.cache\kagglehub\datasets\yashdogra\cats-and-dogs\versions\1\images"
print("\nSUCCESS!")
print("Dataset downloaded to:")
print(path)

#Load images from the downloaded dataset
img_height = 128
img_width= 128
batch_size=32

training_dataset = tf.keras.utils.image_dataset_from_directory(
    path,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)

validation_dataset = tf.keras.utils.image_dataset_from_directory(
    path,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)
print("Classes: ", training_dataset.class_names)

model=models.Sequential([

    #input image
    layers.Input(shape=(img_height,img_width,3)),

    #image re-scaling convert pixels from 0-255 to 0-1
    layers.Rescaling(1./255),

    #Create CNN layer -1
    layers.Conv2D(32, (3,3), activation='relu'),

    layers.MaxPooling2D(),
    #create CNN layer -2
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D(),

    #Convert features maps into 1-dimensional data
    layers.Flatten(),
# fully connected input layer with 64 neurons
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='relu')

])


model.summary()
# COMPILE MODEL
# ============================================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
 #TRAIN MODEL
# ============================================================

epochs = 10

history = model.fit(
    training_dataset,
    validation_data=validation_dataset,
    epochs=epochs
)

print("\nEvaluating model...")

loss, accuracy = model.evaluate(validation_dataset)

print(f"Validation Loss: {loss:.4f}")
print(f"Validation Accuracy: {accuracy:.4f}")
print(f"Validation Accuracy: {accuracy * 100:.2f}%")


# ============================================================
# 13. PREDICT ONE IMAGE
# ============================================================

def predict_image(image_path):

    # Load image
    image = tf.keras.utils.load_img(
        image_path,
        target_size=(img_height, img_width)
    )

    # Convert image to NumPy array
    image_array = tf.keras.utils.img_to_array(image)

    # Add batch dimension
    image_array = tf.expand_dims(image_array, 0)

    # Make prediction
    prediction = model.predict(image_array, verbose=0)

    # Get probability
    probability = prediction[0][0]

    # Convert probability into class
    if probability >= 0.5:
        predicted_class = "dogs"
        confidence = probability
    else:
        predicted_class = "cats"
        confidence = 1 - probability

    print("\nPrediction Result")
    print("-----------------")
    print("Image:", image_path)
    print("Prediction:", predicted_class)
    print(f"Confidence: {confidence * 100:.2f}%")


# ============================================================
# 14. TEST A NEW IMAGE
# ============================================================

test_image = r"C:\Users\RajDaily\Desktop\test_cat.jpg"

predict_image(test_image)