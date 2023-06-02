import cv2
import numpy as np
from tensorflow import keras
from keras.models import load_model

model_path = r"C:\Users\sowmy\Documents\model94.h5"

img_path = r"C:\Users\sowmy\Documents\Mackerel\IMG20230518082700_2.jpg"

def preprocess_image(img_path, IMAGE_SIZE):
    # Load and preprocess the new image
    image = cv2.imread(img_path)
    # Resize the image to match the input size of the CNN model
    image = cv2.resize(image, (IMAGE_SIZE, IMAGE_SIZE))  
    # Normalize the image
    image = image / 255.0 

    # Expand dimensions to match the input shape of the CNN model
    image = np.expand_dims(image, axis=0)
    return image

def test_img(img_path, model_path):
    m = load_model(model_path)

    # test new image
    fish_type = ['Good', 'Bad']
    IMAGE_SIZE = 224
    image = preprocess_image(img_path, IMAGE_SIZE)
    prediction = m.predict(image)
    prediction = fish_type[np.argmax(prediction)]
    print(prediction)
    
    
test_img(img_path, model_path)