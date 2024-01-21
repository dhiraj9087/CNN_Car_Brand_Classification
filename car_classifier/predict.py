# car_classifier/predict.py
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import requests
import io
from io import BytesIO
from PIL import Image
import uuid  
import os


model = load_model('/Users/dhirajmarathe/model_resnet50.h5')
# def predict_car_brand(image_url):
#     image_url = 'https://unsplash.com/s/photos/audi-car'
#     print(f"Received image URL: {image_url}")

#     # Download the image from the URL
#     response = requests.get(image_url)
    
#     # Open the image using PIL's Image.open
#     img = Image.open(BytesIO(response.content)).convert('RGB')
#     img = img.resize((224, 224))  # Resize the image to the target size
#     print("Image loaded successfully.")

#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0

#     prediction = model.predict(img_array)
#     brand_names = ['Audi', 'Lamborghini', 'Mercedes']
#     predicted_brand = brand_names[np.argmax(prediction)]

#     return predicted_brand

def predict_car_brand(image_path):
    # image_path='https://unsplash.com/s/photos/audi-car'
    print(f"Received image_path: {image_path}")

    img = image.load_img(image_path, target_size=(224, 224))
    print("Image loaded successfully.")

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)
    brand_names = ['Audi', 'Lamborghini', 'Mercedes']
    predicted_brand = brand_names[np.argmax(prediction)]

    return predicted_brand
# def predict_car_brand(image_file):
#     print("Received image_file.")

#     # Convert InMemoryUploadedFile to bytes-like object
#     image_content = image_file.read()
#     image_path = io.BytesIO(image_content)
#     print("Image content converted to bytes-like object.")

#     # Generate a unique filename
#     unique_filename = f"{uuid.uuid4().hex[:10]}.jpg"  # Example: a1b2c3d4e5.jpg
#     save_path = os.path.join('media/uploads/', unique_filename)
    
#     # Save the image with the unique filename
#     with open(save_path, 'wb') as f:
#         f.write(image_content)
#     print(f"Image saved successfully at: {save_path}")

#     img = image.load_img(image_path, target_size=(224, 224))
#     print("Image loaded successfully.")

#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0

#     prediction = model.predict(img_array)
#     brand_names = ['Audi', 'Lamborghini', 'Mercedes']
#     predicted_brand = brand_names[np.argmax(prediction)]

#     return predicted_brand