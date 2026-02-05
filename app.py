import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from io import StringIO

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("API_KEY not found in .env file. Please add your API key.")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
MODEL_NAME = "gemini-2.5-flash-lite"
model = genai.GenerativeModel(MODEL_NAME)

# Streamlit UI
st.title("Python Code Review App")
st.header("Powered by AI")
st.markdown("---")

st.subheader("Upload your Python file for review")
data = st.file_uploader("Upload .py file", type=".py")

if data:
    # Read the uploaded file
    stringio = StringIO(data.getvalue().decode('utf-8'))
    fetched_data = stringio.read()
    
    # Display the code
    with st.expander("📄 Uploaded Code", expanded=True):
        st.code(fetched_data, language="python")
    
    # Code review button
    if st.button("🔍 Review Code", type="primary", use_container_width=True):
        with st.spinner("AI is analyzing your code..."):
            try:
                # Create the prompt for code review
                system_prompt = """You are an expert Python code reviewer. Analyze the provided code and give detailed suggestions for improvement covering:

1. **Code Quality & Best Practices** - PEP 8 compliance, naming conventions, readability
2. **Potential Bugs & Issues** - Logic errors, edge cases, exception handling
3. **Performance Optimization** - Efficiency improvements, algorithmic complexity
4. **Security Concerns** - Input validation, injection risks, sensitive data handling
5. **Code Structure** - Modularity, function design, class organization
6. **Specific Recommendations** - Concrete code examples showing improvements

Format your response with clear headings and bullet points. Be constructive and educational."""

                full_prompt = f"{system_prompt}\n\n--- CODE TO REVIEW ---\n\n```python\n{fetched_data}\n```"
                
                # Call Gemini API
                response = model.generate_content(
                    full_prompt,
                    generation_config={
                        "temperature": 0.3,
                        "max_output_tokens": 4096,
                    }
                )
                
                # Display the review
                st.markdown("---")
                st.subheader("📝 Code Review Results")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error during code review: {str(e)}")
                st.info("Please check your GEMINI_API_KEY and try again.")