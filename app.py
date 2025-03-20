import streamlit as st
import os

# Set upload directory
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_file(uploaded_file, file_type):
    """Saves the uploaded file locally."""
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"{file_type} file saved: {file_path}")
    else:
        st.warning(f"No {file_type} file uploaded.")

# Streamlit UI
st.title("Health Care Insurance Claim")
st.subheader("Upload Files")

# File Upload
appeal_pdf = st.file_uploader("Upload Appeal PDF", type=["pdf"])
x12_txt = st.file_uploader("Upload X12.txt File", type=["txt"])

if st.button("Save Files"):
    save_file(appeal_pdf, "Appeal PDF")
    save_file(x12_txt, "X12.txt")
