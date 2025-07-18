### Health Management App

from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini Pro Vision
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')  # Fixed model name
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to prepare image data
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Fixed key: 'mine_type' → 'mime_type'
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("Prajwal, no file uploaded!")  # Fixed exception name

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Health App")
st.header("Gemini Health App")

# Input fields
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Fixed typo: 'umploaded_file' → 'uploaded_file'
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell me the total calories")

# Pre-defined prompt for calorie estimation
input_prompt = """
You are an expert nutritionist. Look at the food items in the image and calculate the total calories. 
Also, provide details of each item with calorie counts in the following format:

1. Item 1 - number of calories  
2. Item 2 - number of calories  
...
"""

# When button is clicked
if submit:
    if uploaded_file is not None:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_text, image_data, input_prompt)
        st.write(response)
    else:
        st.error("Please upload an image first.")
