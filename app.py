import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key

genai.configure(api_key=api_key)

system_prompt="""
As a highly skilled medical practioner specialization in image analysis,

Responsibilty includes:

1. Detailed Analysis
2. Findings Report
3. Recommendation and next steps
4. Treatment suggestions
"""
model = genai.GenerativeModel(model_name="gemini-1.5-pro-002")

st.set_page_config(page_title="Vitalimage", page_icon=":robot:")

#st.image("path",width=200)  if logo

st.title("Image Analytics")

st.subheader("An application that can help identify and diagnose")

upload_file=st.file_uploader("Upload image",type=["png","jpg","jpeg"])

submit_button=st.button("Generate")

if submit_button:
    image_data=upload_file.getvalue()
    image_parts=[
        {
            "mime_type":"image/jpeg",
            "data": image_data
        },
    ]

    prompt_parts =[
        image_parts[0],
        system_prompt,
    ]

    response= model.generate_content(prompt_parts)
    st.write(response.text)





 