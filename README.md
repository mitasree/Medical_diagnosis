🩺 VitalImage: Medical Diagnosis Image Analytics App

VitalImage is a Streamlit-based web application powered by Google's Gemini Pro Vision (1.5) model. It assists in analyzing medical images to generate diagnostic insights, findings, treatment suggestions, and next steps — acting as a virtual expert assistant for preliminary analysis.

🚀 Features

🖼️ Image Upload – Supports .jpg, .jpeg, and .png formats.

🤖 AI Analysis – Uses Google Gemini 1.5 Pro Vision model to analyze images.

📋 Detailed Output – Returns:

Observations and findings

Diagnosis suggestions

Possible treatment options

Recommended next steps

🧠 How It Works

The user uploads a medical image (e.g., X-ray, scan, etc.).

The app sends the image and a detailed system prompt to Gemini.

The model returns a structured diagnostic report based on the image.

🔧 Tech Stack

Frontend: Streamlit

Backend: Google Generative AI (Gemini 1.5 Pro Vision)

Language: Python

API Key Handling: Externalized securely via api_key.py

📂 File Structure
📁 project_root/
│
├── app.py               # Main Streamlit application
├── api_key.py           # Contains your Google API key (DO NOT SHARE)
└── README.md            # Project overview

⚙️ Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/vitalimage.git
cd vitalimage


Install dependencies:

pip install streamlit google-generativeai


Add your API key to api_key.py:

api_key = "your-google-api-key-here"


Run the app:

streamlit run app.py

⚠️ Disclaimer

This app is a prototype and not approved for clinical use. Always consult certified medical professionals before making any health-related decisions.



