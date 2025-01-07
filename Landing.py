import json
import requests
from requests.exceptions import RequestException
import streamlit as st
from streamlit_lottie import st_lottie
import base64
from PIL import Image
import time

st.set_page_config(
    page_title='DremDect',
    layout="wide",
)

# Function to add a background image from local file
def add_bg_from_local(image_file):
    with open(image_file, "abdulai.jpg") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# add_bg_from_local('abdulai.jpg')

# Function to load a Lottie animation from URL
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except RequestException:
        return None

# Function to add a fade-in effect for content
def fade_in_content(content, delay=0.2):
    st.markdown(f"""
        <style>
        @keyframes fadeIn {{
            from {{opacity: 0;}}
            to {{opacity: 1;}}
        }}
        .fade-in {{
            animation: fadeIn {delay}s ease-in;
        }}
        </style>
        <div class="fade-in">
            {content}
        </div>
        """, unsafe_allow_html=True)

# Function to display a welcome animation
def display_welcome_animation():
    with st.spinner('Loading...'):
        time.sleep(2)
    st.write('Welcome to DremDect!')

# # Display the welcome animation when the page loads
# display_welcome_animation()

# Title with custom styling and fade-in effect
fade_in_content('<h2 style="color: #003D4D; text-align: left; font-size: 36px;">Welcome to DremDect ⚕️</h2>', delay=1)


# Two columns for content
col1, col2 = st.columns(2)

# Left column with description and buttons
with col1:
    fade_in_content('<p style="font-size: 20px; color: #2C3E50; line-height: 1.6;">DremDect is an innovative online tool designed to help detect skin cancer early. By uploading a photo of your skin, our app can help identify whether a spot or lesion might be harmful or benign.</p>', delay=1.5)
    fade_in_content('<p style="font-size: 20px; color: #2C3E50; line-height: 1.6;">The goal of DremDect is to provide you with a quick, easy, and reliable way to get an initial assessment of your skin. Whether you are concerned about a new spot or monitoring an existing one, our tool can give you some peace of mind and help guide you on whether you should seek further medical advice.</p>', delay=1.5)
    fade_in_content('<p style="font-size: 20px; color: #2C3E50; line-height: 1.6;">Remember, while DremDect is a helpful tool, it does not replace a visit to your healthcare provider. Always consult with a doctor or dermatologist for a comprehensive evaluation.</p>', delay=1.5)
    
    st.markdown("""
    <style>
    .custom-button {
        background-color: #005F73;  /* Deep teal */
        color: white;
        padding: 12px 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        border-radius: 8px;
        margin-top: 20px;
    }
    .custom-button:hover {
        background-color: #003D4D;  /* Dark navy */
    }
    </style>
    <a href="http://localhost:8502/" class="custom-button">Get Started 🩺 </a>
    """, unsafe_allow_html=True)


# Right column with an image
with col2:
        # Add Lottie animation to the left column
    lottie_url = "https://assets10.lottiefiles.com/packages/lf20_zrqthn6o.json"  # Example URL
    lottie_animation = load_lottieurl(lottie_url)
    if lottie_animation:
        st_lottie(lottie_animation, height=300, key="animation")
        
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