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
![Screenshot 2025-07-06 110437](https://github.com/user-attachments/assets/dd3c498a-2405-4c54-ad75-61c4ac

---

https://github.com/user-attachments/assets/1508e6fa-e050-48a7-8d00-c9de9ca9a93a

---

## Gemini Health App 🍎 - An AI-Powered Nutrition & Wellness Tracker
---
##### Project Overview
- The Gemini Health App is a cutting-edge, interactive web application designed to revolutionize personal health management. Built with Streamlit and powered by the Google Gemini-1.5-Flash API, this app provides users with instant, detailed nutritional analysis of their meals through a simple photo upload. It goes beyond basic calorie counting to offer a comprehensive, personalized health tracking experience.

- This project showcases expertise in multimodal AI applications, data persistence for stateful web apps, and the development of a clean, user-friendly interface. It's a complete end-to-end solution that demonstrates a strong foundation in modern web development and machine learning integration.
---
##### Key Features & Technical Highlights
###### ***This project stands out by integrating a powerful AI model into a practical, real-world application, showcasing a blend of front-end development, back-end logic, and AI model utilization.***

###### 1. Advanced Multimodal AI Integration (Gemini-1.5-Flash)
- **Visual Analysis**: The core of the app uses the Gemini-1.5-Flash Vision model to analyze images of food. The model intelligently identifies multiple food items, a task that requires sophisticated computer vision capabilities.
- **Comprehensive Nutritional Breakdown**: The app doesn't just count calories. It leverages a custom-engineered prompt to extract a detailed nutritional report, including macronutrients (protein, carbs, fats) for each item. This demonstrates a deep understanding of prompt engineering to get specific, structured data from a large language model.
- **Personalized Recommendations**: Based on the analysis, the app provides smart, context-aware suggestions for healthier alternatives or additions to a meal.

###### 2. User Profile & Data Persistence
- **Stateful Application Logic**: Unlike typical, stateless Streamlit apps, this project uses st.session_state to maintain user data across interactions. This is a crucial skill for building dynamic applications.
- **Personal Health Logging**: Users can log their weight over time, and the app visualizes this progress with a dynamic line chart. This feature demonstrates an understanding of data visualization and user-centric design.
- **Meal History**: Every meal analyzed is saved to a persistent session log, allowing users to review their dietary history. This shows an ability to build and manage simple databases or data logs.

###### 3. Clean & Intuitive User Interface
- **Streamlit Framework**: The entire application is built using Streamlit, highlighting proficiency in quickly building and deploying interactive data applications with pure Python.
- **Responsive Design**: The layout, with its use of st.columns and st.expander, is well-organized and easy to navigate, demonstrating an eye for UI/UX design.
- **Error Handling**: The code includes robust try-except blocks to gracefully handle potential issues like missing file uploads, providing a smooth user experience.
---
##### Project Stack
- **Framework**: Streamlit
- **AI Model**: Google Gemini-1.5-Flash (via google-generativeai)
- **Core Libraries**: PIL (Pillow), python-dotenv
- **Languages**: Python
---
##### How to Run Locally

- 1) Clone the Repository:
 <img width="1920" height="1000" alt="Screenshot 2025-08-31 032556" src="https://github.com/user-attachments/assets/76c589c7-5aa5-4979-b6a9-e780c809482c" />
 <img width="1920" height="779" alt="Screenshot 2025-08-31 032944" src="https://github.com/user-attachments/assets/ed96eb3d-273c-44bf-a746-583b6767e1ff" />

- 2) Set Up Virtual Environment and Install Dependencies:
  ```
  pip install -r requirements.txt
  ```

- 3) Configure API Key:
  - Create a .env file in the project's root directory.
  - Add your API key to the file:
```
GOOGLE_API_KEY="YOUR_API_KEY
```
- 4) Run the Application:

```
streamlit run app.py
```

https://github.com/user-attachments/assets/4a5f14a3-d80a-44b6-aa58-f08d1009f79f

---
Prajwal

