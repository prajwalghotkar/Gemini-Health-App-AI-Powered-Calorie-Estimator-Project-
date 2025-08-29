# Health Management App

## 🩺 Gemini Health App – AI-Powered Calorie Estimator

### The Gemini Health App is a Streamlit-based web application that leverages Google's Gemini Pro Vision API to analyze images of food and estimate total calorie content. Built with Python, this tool helps users stay aware of their dietary intake by simply uploading an image of their meal.

## 🚀 Features

### 🔍 Upload any food image (JPG/PNG) to analyze

### 🤖 Uses Gemini Pro Vision to recognize food items

### 🔢 Provides estimated total calories for the meal

### 🧾 Gives individual item-wise calorie breakdown

### 🛡️ Environment-safe setup using dotenv for API key security

### 🧠 Smart prompt system simulates a professional nutritionist's response

## 🛠️ Tech Stack

### Frontend: https://streamlit.io/

### AI Model: https://ai.google.dev/

### Image Processing: Pillow (PIL)

### Environment Management: python-dotenv

## 📷 Sample Output
### 1)Paneer Tikka – 290 calories

### 2)Butter Naan – 200 calories

### 3)Mixed Salad – 80 calories , Total: ~570 calories

## 💻 How to Run
### Clone the repository
http://localhost:8502/

## Install dependencies

### pip install -r requirements2.txt
##### ----> streamlit
##### ----> google-generativeai
##### ----> python-dotenv
##### ----> langchain
##### ----> PyPDF2
##### ----> chromadb
##### ----> pdf2image
##### ----> faiss-cpu
##### ----> langchain_google_genai

### Set up your .env file

#### Create a file named .env in the project root and add:
##### GOOGLE_API_KEY=your_api_key_here

### Run the Streamlit app

##### streamlit run HealthManagementApp.py

## 📂 Folder Structure

### 📦health-management-app
 ┣ 📄HealthManagementApp.py
 ┣ 📄.env (you create this)
 ┣ 📄requirements2.txt


## 🧠 Prompt Used

### You are an expert nutritionist. Look at the food items in the image and calculate the total calories. Also, provide details of each item with calorie counts in the following format:
#### 1. Item 1 - number of calories
#### 2. Item 2 - number of calories
...

![Screenshot 2025-07-06 110424](https://github.com/user-attachments/assets/ed3727f9-e39c-48e6-8f4b-611967531c1f)
![Screenshot 2025-07-06 110437](https://github.com/user-attachments/assets/dd3c498a-2405-4c54-ad75-61c4acbba12e)


👨‍💻 Prajwal 


