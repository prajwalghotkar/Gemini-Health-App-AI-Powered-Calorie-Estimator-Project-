from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini Pro Vision with a more detailed prompt
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to prepare image data
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("Prajwal, no file uploaded!")

# Initialize Streamlit app and session state for data persistence
st.set_page_config(page_title="Gemini Health App")

# Initialize user data in session state if it doesn't exist
if 'user_data' not in st.session_state:
    st.session_state.user_data = {
        'meals': [],
        'weight_history': []
    }

st.header("Gemini Health App")
st.markdown("---")

## User Profile and Logging
st.subheader("Your Profile & Daily Log")

# Input for logging weight
col1, col2 = st.columns(2)
with col1:
    current_weight = st.number_input("Enter your current weight (kg):", min_value=1.0, format="%f")
with col2:
    if st.button("Log Weight"):
        st.session_state.user_data['weight_history'].append({
            'date': datetime.now().strftime("%Y-%m-%d"),
            'weight': current_weight
        })
        st.success(f"Weight of {current_weight} kg logged successfully!")

# Display logged data
st.write("### Your Progress")
st.write("---")
if st.session_state.user_data['weight_history']:
    st.write("#### Weight History")
    st.line_chart(
        data=[item['weight'] for item in st.session_state.user_data['weight_history']],
        x=[item['date'] for item in st.session_state.user_data['weight_history']],
        height=300
    )
    st.dataframe(st.session_state.user_data['weight_history'])
    
st.markdown("---")

## Enhanced Nutritional Analysis
st.subheader("Nutritional Breakdown of Your Meal")

# Input fields for the meal
input_text = st.text_input("Input Prompt (e.g., 'What is in this meal?'):", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:
        st.error(f"Error opening image: {e}")

submit = st.button("Analyze Meal")

# Pre-defined prompt for comprehensive analysis
input_prompt = """
You are an expert nutritionist. Analyze the food items in the image and provide a detailed nutritional breakdown.
Calculate the total calories for the meal.
Provide a breakdown for each item in the following format:
1. **Item Name** (e.g., Grilled Chicken)
   - **Calories:** [number] kcal
   - **Protein:** [number] g
   - **Carbohydrates:** [number] g
   - **Fats:** [number] g
Also, summarize the nutritional benefits and suggest a healthy alternative or addition to the meal.
"""

# When button is clicked
if submit:
    if uploaded_file is not None:
        try:
            image_data = input_image_setup(uploaded_file)
            st.spinner("Analyzing your meal...")
            response = get_gemini_response(input_text, image_data, input_prompt)
            st.subheader("Nutritional Report")
            st.write(response)
            
            # Simple meal logging
            st.session_state.user_data['meals'].append({
                'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'prompt': input_text,
                'report': response
            })
            
        except FileNotFoundError as e:
            st.error(f"{e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image first.")

st.markdown("---")
st.subheader("Your Meal Log")
if st.session_state.user_data['meals']:
    for meal in st.session_state.user_data['meals']:
        with st.expander(f"Meal on {meal['date']}"):
            st.write(f"**Your Prompt:** {meal['prompt']}")
            st.write(meal['report'])