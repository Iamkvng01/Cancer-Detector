import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# st.set_page_config(
#     page_title='DremDect',
#     layout="wide",
# )

# Load your model
model = tf.keras.models.load_model('/Users/godenaan/Documents/400L project/Model.h5')

# Function to preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((224, 224))  # Resize image to match model input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = image.reshape((1, 224, 224, 3))  # Reshape to match model input shape
    return image

# Function to predict the class of the uploaded image
def predict(image, model):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)
    predicted_class_index = np.argmax(prediction[0])
    class_labels = ["Melanoma", "Pigmented Benign Keratosis", "Vascular Lesion", "Actinic Keratosis", "Basal Cell Carcinoma", "Dermatofibroma", "Nevus", "Seborrheic Keratosis", "Squamous Cell Carcinoma"]
    predicted_class_label = class_labels[predicted_class_index]
    return predicted_class_label

# Function to explain the diagnosis
def explain_diagnosis(disease):
    # Define cancerous and non-cancerous categories
    cancerous_diseases = ["Melanoma", "Actinic Keratosis", "Basal Cell Carcinoma", "Squamous Cell Carcinoma"]
    non_cancerous_diseases = ["Pigmented Benign Keratosis", "Vascular Lesion", "Dermatofibroma", "Nevus", "Seborrheic Keratosis"]

    # Provide explanation based on classification
    if disease in cancerous_diseases:
        explanation = f"{disease} is a cancerous condition. It is important to consult a healthcare professional for further evaluation and management. Early detection and treatment are crucial to improving outcomes."
        advice = "Please schedule an appointment with a dermatologist or oncologist as soon as possible to discuss potential treatment options."
    elif disease in non_cancerous_diseases:
        explanation = f"{disease} is a non-cancerous condition. While it is generally not harmful, it is recommended to monitor the condition and consult a healthcare provider if there are any changes in size, shape, or color."
        advice = "No immediate action is required, but regular check-ups with your dermatologist are advisable."
    else:
        explanation = "The classification of this condition is not recognized. Please consult a healthcare professional for further advice."
        advice = "Consider seeking a second opinion or further diagnostic testing to confirm the nature of the condition."

    return explanation, advice

# Streamlit App
st.set_page_config(page_title="DremDect Skin Cancer Detection", layout="wide")

# Sidebar Navigation with Buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Cancer Detector"):
    selected_page = "Cancer Detector"
elif st.sidebar.button("Application Guide"):
    selected_page = "Application Guide"
else:
    selected_page = "Cancer Detector"  # Default page

if selected_page == "Cancer Detector":
    # Main application code
    st.title("DremDect Skin Cancer Detection")
    st.write("Upload an image to assess potential skin cancer risk.")

    # File uploader
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the image
        image = Image.open(uploaded_file)
        
        # Show a success message instead of displaying the image
        success_message = st.success("Image uploaded successfully.")
        
        # Prediction button
        if st.button('Analyze Image'):
            with st.spinner('Analyzing the image...'):
                result = predict(image, model)
            # Clear the success message
            success_message.empty()
            # Display prediction result
            st.success(f"Analysis Complete: The image is classified as {result}")

            # Get explanation and advice
            explanation, advice = explain_diagnosis(result)
            
            # Display explanation and advice
            st.write(f"**Explanation:** {explanation}")
            st.write(f"**Advice:** {advice}")

elif selected_page == "Application Guide":
    # Application Guide content
    st.title("DremDect Application Guide")
    st.write("""
    Welcome to the DremDect Skin Cancer Detection App. Follow the steps below to use the app effectively:
    
    1. **Upload an Image**: Use the 'Upload Image' button to upload an image in JPG, JPEG, or PNG format.
    2. **Analyze Image**: After uploading, click on 'Analyze Image' to start the detection process.
    3. **View Results**: The app will process the image and display the predicted classification on the screen.
    
    This app is designed to assist in early diagnosis by providing a preliminary analysis of skin conditions. 
    """)
    st.write("""
    **Tips for Best Results:**
    - Ensure the image is clear and focused.
    - Avoid images with excessive shadows or poor lighting.
    - Use high-resolution images for more accurate analysis.
    """)

# Footer section
st.markdown("""
    <style>
    footer {
        visibility: hidden;
    }
    .footer-text {
        font-size: 0.8rem;
        text-align: center;
        color: #555;
        padding: 10px 0;
    }
    </style>
    <div class="footer-text">
        &copy; 2024 DremDect. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
