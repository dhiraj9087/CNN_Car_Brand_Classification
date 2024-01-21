# # from django.shortcuts import render

# # Create your views here.
# # car_classifier/views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from .forms import CarImageForm
# from .predict import predict_car_brand  # You need to implement this function
# import os
# def upload_image(request):
#     if request.method == 'POST':
#         form = CarImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             print("valid______")
#             form.save()
#             image_path = form.cleaned_data['image']
#             # if image_path=='25.jpg':
#             #     image_path='/Users/dhirajmarathe/Datasets_car/Test/audi'
#             # dirc='/Users/dhirajmarathe/Datasets_car/Test/audi/25.jpg'
#             # print(os.listdir(dirc))
#             # brand_prediction = predict_car_brand('/Users/dhirajmarathe/Datasets_car/Test/audi')
#             brand_prediction = predict_car_brand(image_path)
#             return render(request, 'result.html', {'brand_prediction': brand_prediction})
#     else:
#         form = CarImageForm()
#     return render(request, 'upload.html', {'form': form})
# car_classifier/views.py
from django.shortcuts import render
from .forms import CarImageForm
from .predict import predict_car_brand
from .models import *
import os
def upload_image(request):
    if request.method == 'POST':
        form = CarImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_instance = form.save() 
            image_file = uploaded_file_instance.image.path
            # image_file = form.cleaned_data['image']
            # base_path = os.path.dirname(__file__)
            # file_path = os.path.join(base_path, 'uploads', secure_filename(f.filename))
            brand_prediction = predict_car_brand(image_file)
            return render(request, 'result.html', {'brand_prediction': brand_prediction})
    else:
        form = CarImageForm()
    return render(request, 'upload.html', {'form': form})
