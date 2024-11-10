from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PredictSerializer
import pandas as pd
import numpy as np
from tensorflow import keras
import keras

# Load the model once when the server starts
loaded_model = keras.models.load_model('predict/final_shopper_model.h5')

def finding_type(x):
    if x == 1:
        return [1,0,0]
    elif x == 2:
        return [0,0,1]
    else:
        return [0,1,0]

class PredictAPIView(APIView):
    def post(self, request):
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Prepare the input data
            type_visitor = finding_type(data['VisitorType'])
            df = pd.DataFrame([{
                'Administrative_Duration': data['Administrative'],
                'Informational_Duration': data['Informational'],
                'ProductRelated': data['ProductRelated'],
                'BounceRates': data['BounceRates'],
                'ExitRates': data['ExitRates'],
                'PageValues': data['PageValues'],
                'SpecialDay': data['SpecialDay'],
                'OperatingSystems': data['OperatingSystems'],
                'Browser': data['Browser'],
                'Region': data['Region'],
                'TrafficType': data['TrafficType'],
                'Weekend': data['Weekend'],
                'New_Visitor': type_visitor[0],
                'Other': type_visitor[1],
                'Returning_Visitor': type_visitor[2]
            }])

            # Make the prediction
            prediction = np.argmax(loaded_model.predict(df), axis=-1)
            result = "True" if prediction[0] == 1 else "False"

            # Return the response
            return Response(
                {"message": f"The customer will generate Revenue: {result}"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

import cv2 # ? For linux please install first --> sudo apt update && sudo apt install libgl1-mesa-glx
from rest_framework.parsers import MultiPartParser

# Load the model when the server starts
plantModel = keras.models.load_model('predict/plant_disease.h5')

# Define the class names for the predictions
CLASS_NAMES = ['Corn-Common_rust', 'Potato-Early_blight', 'Tomato-Bacterial_spot']

class PredictPlantDisease(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        # Handle the image upload
        image = request.FILES.get('image')
        if not image:
            return Response({"error": "No image uploaded"}, status=400)

        # Read the image content directly as bytes
        file_bytes = np.frombuffer(image.read(), np.uint8)

        # Decode the image file using OpenCV
        opencv_image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        # Check if the image was decoded properly
        if opencv_image is None:
            return Response({"error": "Invalid image format"}, status=400)
        
        # Resize the image to the model input size and prepare it for prediction
        opencv_image = cv2.resize(opencv_image, (256, 256))
        opencv_image = np.expand_dims(opencv_image, axis=0)

        # Make prediction
        prediction = plantModel.predict(opencv_image)
        result = CLASS_NAMES[np.argmax(prediction)]

        # Parse the result to make it user-friendly
        plant, disease = result.split('-')
        response_message = f"This is a {plant} leaf with {disease}."

        # Return the result as JSON response
        return Response({"message": response_message})